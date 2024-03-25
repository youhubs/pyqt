from os.path import expanduser
# from PyQt6.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QTreeView
from PyQt5.QtWidgets import QDirModel

home_directory = expanduser('~')

app = QApplication([])
model = QDirModel()
view = QTreeView()
view.setModel(model)
view.setRootIndex(model.index(home_directory))
view.show()
app.exec()