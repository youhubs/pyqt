import sys
import lasio
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTreeView, QSplitter
from PySide6.QtCore import Qt, QAbstractItemModel, QModelIndex
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

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
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(PlotCanvas, self).__init__(self.fig)
        self.setParent(parent)
    
    def plot_curves(self, curves_to_plot):
        # Clear the figure for fresh plots
        self.fig.clear()

        # Number of curves
        n_curves = len(curves_to_plot)
        
        # Create subplots that share the y-axis (depth)
        # Adjust 'width_ratios' if needed to give more space to certain curves
        gs = self.fig.add_gridspec(1, n_curves, wspace=0, hspace=0, width_ratios=[1]*n_curves)
        shared_ax = None
        las_data = lasio.read(r'/Users/tigerhu/Downloads/LAS Files/example.las')
        
        for i, curve_name in enumerate(curves_to_plot):
            if i == 0:
                ax = self.fig.add_subplot(gs[0, i])
                shared_ax = ax
            else:
                ax = self.fig.add_subplot(gs[0, i], sharey=shared_ax)
            
            data = las_data[curve_name]
            depth = las_data.curves.DEPT.data
            max_depth = depth.max()
            min_depth = depth.min()
            ax.set_ylim(min_depth,max_depth)

            ax.plot(data, depth)
            ax.set_title(curve_name)
            ax.invert_yaxis()  # Make depth increase downwards

            # Hide y labels and ticks for subplots that are not the first one
            if i > 0:
                ax.tick_params(labelleft=False, left=False)
            
            # Optionally, rotate x-axis labels if they overlap
            ax.tick_params(axis='x', labelrotation=45)

        self.fig.tight_layout()  # Adjust layout to make room for all subplots
        self.draw()

class LasViewer(QWidget):
    def __init__(self, lasfile, parent=None):
        super(LasViewer, self).__init__(parent)

        self.splitter = QSplitter(Qt.Horizontal, self)

        self.treeView = QTreeView(self.splitter)
        self.treeView.setSelectionMode(QTreeView.MultiSelection)
        self.plotCanvas = PlotCanvas(self.splitter)  # Replace QTextEdit with PlotCanvas
        self.model = None
        self.loadLasFile(lasfile)

        layout = QVBoxLayout(self)
        layout.addWidget(self.splitter)
        self.setLayout(layout)

        self.treeView.selectionModel().selectionChanged.connect(self.onSelectionChanged)

    def loadLasFile(self, lasfile):
        las_data = lasio.read(lasfile)
        lasfiles = self.parseLasData(las_data)
        self.model = LasTreeModel(lasfiles)
        self.treeView.setModel(self.model)

    def parseLasData(self, las_data):
        # Adjust according to the structure of your LAS files
        project_name = las_data.well.WELL.value  # Example to get project name from the LAS file
        wells = [{
            'name': project_name,  # Assuming single well per LAS file for simplicity
            'curves': [curve.mnemonic for curve in las_data.curves if curve.mnemonic not in ['DEPTH','DEPT']]
        }]
        return [{
            'project': project_name,  # Use the well name as the project name for simplicity
            'wells': wells
        }]

    def onSelectionChanged(self):
        indexes = self.treeView.selectionModel().selectedIndexes()
        curves_to_plot = []
        for index in indexes:
            node = index.internalPointer()
            # Ensure a curve is selected (check based on your tree structure)
            if node and node.parent and node.parent.name != "Projects":
                curve_name = node.name
                if curve_name not in curves_to_plot:
                    curves_to_plot.append(curve_name)
        if curves_to_plot:
            self.plotCanvas.plot_curves(curves_to_plot)

def main():
    app = QApplication(sys.argv)
    lasfile_path = r'/Users/tigerhu/Downloads/LAS Files/example.las'  # Corrected path to the uploaded LAS file
    viewer = LasViewer(lasfile_path)
    viewer.resize(800, 600)
    viewer.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
