import sys
from welly import Well
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTreeView, QSplitter
from PySide6.QtCore import Qt, QAbstractItemModel, QModelIndex
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# Assume TreeNode and LasTreeModel classes are provided earlier remain unchanged
class TreeNode:
    def __init__(self, name, data=None, parent=None):
        self.name = name
        self.data = data
        self.parent = parent
        self.children = []

    def appendChild(self, child):
        self.children.append(child)

    def child(self, row):
        if row < 0 or row >= len(self.children):
            return None
        return self.children[row]

    def childCount(self):
        return len(self.children)

    def row(self):
        if self.parent:
            return self.parent.children.index(self)
        return 0

    def columnCount(self):
        return 2

class LasTreeModel(QAbstractItemModel):
    def __init__(self, lasfiles, parent=None):
        super(LasTreeModel, self).__init__(parent)
        self.rootNode = TreeNode("Projects")
        for lasfile in lasfiles:
            projectNode = TreeNode(lasfile['project'], parent=self.rootNode)
            self.rootNode.appendChild(projectNode)
            for well in lasfile['wells']:
                wellNode = TreeNode(well['name'], parent=projectNode)
                projectNode.appendChild(wellNode)
                for curve in well['curves']:
                    curveNode = TreeNode(curve, parent=wellNode)
                    wellNode.appendChild(curveNode)

    def index(self, row, column, parent=QModelIndex()):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()
        if not parent.isValid():
            parentItem = self.rootNode
        else:
            parentItem = parent.internalPointer()
        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        return QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QModelIndex()
        childItem = index.internalPointer()
        parentItem = childItem.parent
        if parentItem == self.rootNode:
            return QModelIndex()
        return self.createIndex(parentItem.row(), 0, parentItem)

    def rowCount(self, parent=QModelIndex()):
        if parent.column() > 0:
            return 0
        if not parent.isValid():
            parentItem = self.rootNode
        else:
            parentItem = parent.internalPointer()
        return parentItem.childCount()

    def columnCount(self, parent=QModelIndex()):
        return 2

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or role != Qt.DisplayRole:
            return None
        item = index.internalPointer()
        if index.column() == 0:
            return item.name
        elif index.column() == 1 and item.data is not None:
            return item.data
        return None

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return ["Name", "Data"][section]
        return None

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(PlotCanvas, self).__init__(fig)
        self.setParent(parent)

    def plot(self, curve):
        self.axes.clear()
        if curve is not None:
            curve.plot(ax=self.axes)  # Use Welly's plot method
        self.draw()

class LasViewer(QWidget):
    def __init__(self, lasfile_path, parent=None):
        super(LasViewer, self).__init__(parent)

        self.well = Well.from_las(lasfile_path)  # Load LAS file using Welly

        self.splitter = QSplitter(Qt.Horizontal, self)
        self.treeView = QTreeView(self.splitter)
        self.plotCanvas = PlotCanvas(self.splitter)
        
        # Generate model data from Welly Well object
        lasfiles = self.parseWellData(self.well)
        self.model = LasTreeModel(lasfiles)
        self.treeView.setModel(self.model)

        layout = QVBoxLayout(self)
        layout.addWidget(self.splitter)
        self.setLayout(layout)

        self.treeView.selectionModel().selectionChanged.connect(self.onSelectionChanged)

    def parseWellData(self, well):
        # Simplified example of parsing well data with Welly
        curves = [{'name': mnemonic, 'data': list(well.data)} for mnemonic in well.data.keys()]
        wells = [{'name': well.name, 'curves': curves}]
        return [{'project': well.name, 'wells': wells}]

    def onSelectionChanged(self):
        indexes = self.treeView.selectionModel().selectedIndexes()
        if indexes:
            index = indexes[0]
            node = index.internalPointer()
            if node and node.parent and node.parent.name != "Projects":
                curve_name = node.name
                curve = self.well.data.get(curve_name)
                self.plotCanvas.plot(curve)

def main():
    app = QApplication(sys.argv)
    lasfile_path = r'/Users/tigerhu/Downloads/LAS Files/example.las'  # Update this path to your LAS file
    viewer = LasViewer(lasfile_path)
    viewer.resize(800, 600)
    viewer.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
