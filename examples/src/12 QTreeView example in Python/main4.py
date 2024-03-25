import sys
import lasio
from PySide6.QtWidgets import QApplication, QTreeView, QWidget, QVBoxLayout
from PySide6.QtCore import QAbstractItemModel, QModelIndex, Qt

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

# Example usage
class LasViewer(QWidget):
    def __init__(self, lasfiles, parent=None):
        super(LasViewer, self).__init__(parent)
        self.treeView = QTreeView(self)
        self.model = LasTreeModel(lasfiles)
        self.treeView.setModel(self.model)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.treeView)
        self.setLayout(self.layout)

def main():
    app = QApplication(sys.argv)

    # Simulate loading LAS files
    # Replace this part with actual LAS file loading and parsing
    lasfiles = [{
        'project': 'Project 1',
        'wells': [
            {'name': 'Well 1', 'curves': ['GR', 'RHOB']},
            {'name': 'Well 2', 'curves': ['NPHI', 'DT']},
        ]
    }, {
        'project': 'Project 2',
        'wells': [
            {'name': 'Well 3', 'curves': ['GR', 'RHOB', 'NPHI']},
        ]
    }]

    viewer = LasViewer(lasfiles)
    viewer.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
