import sys
from PySide6.QtWidgets import QApplication, QTreeView, QFileSystemModel
from PySide6.QtCore import QDir


def main():
    app = QApplication(sys.argv)

    # Create the model
    model = QFileSystemModel()
    model.setRootPath(QDir.rootPath())

    # Create the view and set the model
    view = QTreeView()
    view.setModel(model)

    # Optionally, set the initial directory
    view.setRootIndex(model.index(QDir.rootPath()))

    # Show the view
    view.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
