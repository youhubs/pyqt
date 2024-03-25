import sys
import lasio
from PySide6.QtWidgets import QApplication, QTreeView, QWidget, QVBoxLayout
from PySide6.QtCore import QAbstractItemModel, QModelIndex, Qt


class LasTreeModel(QAbstractItemModel):
    def __init__(self, lasfile, parent=None):
        super(LasTreeModel, self).__init__(parent)
        self.lasfile = lasfile
        self.rootData = ["Item", "Value"]
        self.treeData = self.parseLasFile()

    def parseLasFile(self):
        # Using the .get method to safely access attributes
        # It returns None if a key doesn't exist instead of raising an AttributeError
        treeData = [
            ("Project/File", "N/A"),  # Example, replace as needed
            ("Well", [
                ("Name", self.lasfile.well.get('WELL', 'N/A')),
                ("Depth", "{} to {}".format(self.lasfile.well.get('STRT', 'N/A'), self.lasfile.well.get('STOP', 'N/A')))
            ]),
            ("Curves", [(curve.mnemonic, curve.unit) for curve in self.lasfile.curves])
        ]
        return treeData

    def index(self, row, column, parent=QModelIndex()):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()
        if not parent.isValid():
            parentData = self.treeData
        else:
            parentData = parent.internalPointer()
        return self.createIndex(row, column, parentData[row])

    def parent(self, index):
        return QModelIndex()

    def rowCount(self, parent=QModelIndex()):
        if parent.column() > 0:
            return 0
        if not parent.isValid():
            parentData = self.treeData
        else:
            parentData = parent.internalPointer()
        if isinstance(parentData, list):
            return len(parentData)
        return 0

    def columnCount(self, parent=QModelIndex()):
        return 2  # Item and Value

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        if role != Qt.DisplayRole:
            return None

        item = index.internalPointer()

        if index.column() == 0:
            return item[0]  # Item name
        elif index.column() == 1:
            return item[1]  # Value

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.rootData[section]

class LasViewer(QWidget):
    def __init__(self, lasfile, parent=None):
        super(LasViewer, self).__init__(parent)
        self.treeView = QTreeView(self)
        self.model = LasTreeModel(lasfile)
        self.treeView.setModel(self.model)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.treeView)
        self.setLayout(self.layout)

def main():
    app = QApplication(sys.argv)

    # Load LAS file
    lasfile = lasio.read(r'/Users/tigerhu/Downloads/LAS Files/Bean/Bean_A.las')  # Specify your LAS file path here
    print(lasfile)
    viewer = LasViewer(lasfile)
    viewer.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
