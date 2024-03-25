import sys
import lasio
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTreeView, QSplitter, QTextEdit
from PySide6.QtCore import Qt, QAbstractItemModel, QModelIndex

# TreeNode class remains the same as in the previous example
# LasTreeModel class remains mostly the same as in the previous example
# Minor adjustments might be necessary based on how you structure TreeNode objects and their data
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

class LasViewer(QWidget):
    def __init__(self, lasfile, parent=None):
        super(LasViewer, self).__init__(parent)

        self.splitter = QSplitter(Qt.Horizontal, self)

        self.treeView = QTreeView(self.splitter)
        self.textEdit = QTextEdit(self.splitter)
        self.model = None
        self.loadLasFile(lasfile)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.splitter)
        self.setLayout(self.layout)

        self.treeView.selectionModel().selectionChanged.connect(self.onSelectionChanged)

    def loadLasFile(self, lasfile):
        # Simulate loading an LAS file
        # Replace this with actual LAS file loading and parsing
        las_data = lasio.read(lasfile)
        lasfiles = self.parseLasData(las_data)
        self.model = LasTreeModel(lasfiles)
        self.treeView.setModel(self.model)

    def parseLasData(self, las_data):
        # Parse the LAS data into a structure suitable for LasTreeModel
        # This is a placeholder function; implement according to your LAS data structure
        return [{
            'project': 'Project 1',  # This could be dynamically determined from las_data
            'wells': [
                {'name': 'Well 1', 'curves': ['GR', 'RHOB']},
                {'name': 'Well 2', 'curves': ['NPHI', 'DT']},
            ]
        }]

    def onSelectionChanged(self):
        indexes = self.treeView.selectionModel().selectedIndexes()
        if indexes:
            index = indexes[0]  # Assuming the first selection for simplicity
            node = index.internalPointer()
            if node:
                # Display something relevant in the textEdit based on the selected node
                # Adjust this logic based on your TreeNode structure and what you want to display
                self.textEdit.setText(node.name)

def main():
    app = QApplication(sys.argv)

    # Specify the path to your LAS file
    lasfile_path = r'/Users/tigerhu/Downloads/LAS Files/example.las'

    viewer = LasViewer(lasfile_path)
    viewer.resize(800, 600)
    viewer.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
