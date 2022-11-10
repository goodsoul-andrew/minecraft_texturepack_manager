import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from my_functions import *
from my_dialogs import *


class TexturepackManager(QMainWindow):
    def __init__(self):
        super(TexturepackManager, self).__init__()
        uic.loadUi('TexturepackManagerUI.ui', self)
        self.title = "Texturepack manager"
        self.createActions()
        self.connectActions()
        self.createMenuBar()
        self.model = QFileSystemModel()
        self.path, self.version, self.description = "", "", ""

    def createActions(self):
        self.newAction = QAction("New", self)
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.setStatusTip("Create a new texturepack")

        self.openAction = QAction("Open", self)
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.setStatusTip("Open folder as texturepack")

        #self.saveAction = QAction("Save", self)
        #self.saveAction.setShortcut("Ctrl+S")
        #self.saveAction.setStatusTip("Save texturepack")

    def createMenuBar(self):
        menuBar = self.menuBar()
        fileMenu = QMenu("File", self)
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        #fileMenu.addAction(self.saveAction)
        editMenu = QMenu("Edit", self)
        helpMenu = QMenu("Help", self)
        menuBar.addMenu(fileMenu)
        editMenu = menuBar.addMenu("Edit")
        helpMenu = menuBar.addMenu("Help")

    #def createStatusBar(self):
        #self.statusbar = self.statusBar()

    def connectActions(self):
        self.newAction.triggered.connect(self.open_newDialog)
        self.openAction.triggered.connect(self.open_openDialog)

    def open_newDialog(self):
        newDialog = NewDialog()
        newDialog.exec()
        self.path = newDialog.path
        self.version = newDialog.version
        self.description = newDialog.description
        self.model.setRootPath(newDialog.directory.currentPath())
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(newDialog.path))

    def open_openDialog(self):
        dirpath = QFileDialog.getExistingDirectory(self, "Choose texturepack", "C:/Users")
        # print(dirpath)
        self.directory = QDir(dirpath)
        # print(self.directory.currentPath())
        self.model.setRootPath(self.directory.currentPath())
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(dirpath))






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TexturepackManager()
    ex.show()
    sys.exit(app.exec_())
