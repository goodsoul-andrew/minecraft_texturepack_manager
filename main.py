import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.Qt import *
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
        # self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.tree.customContextMenuRequested.connect(self.show_context_menu)
        self.tree.doubleClicked.connect(self.edit_file)

    def createActions(self):
        self.newAction = QAction("New", self)
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.setStatusTip("Create a new texturepack")

        self.openAction = QAction("Open", self)
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.setStatusTip("Open folder as texturepack")

        self.editTexturepackAction = QAction("Edit texturepack", self)
        self.editTexturepackAction.setShortcut("Ctrl+E")
        self.editTexturepackAction.setStatusTip("Edit texturepack")

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

    def connectActions(self):
        self.newAction.triggered.connect(self.open_newDialog)
        self.openAction.triggered.connect(self.open_openDialog)

    def open_newDialog(self):
        newDialog = NewDialog()
        print(newDialog.exec())
        if newDialog.result():
            self.path = newDialog.path
            self.version = newDialog.version
            self.description = newDialog.description
            self.directory = newDialog.directory
            self.model.setRootPath(newDialog.directory.currentPath())
            self.tree.setModel(self.model)
            self.tree.setRootIndex(self.model.index(newDialog.path))

    def open_openDialog(self):
        dirpath = QFileDialog.getExistingDirectory(self, "Choose texturepack", "C:/Users")
        # print(dirpath)
        self.directory = QDir(dirpath)
        self.path = dirpath
        self.model.setRootPath(self.directory.currentPath())
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(dirpath))

    def show_context_menu(self, position):
        file_path = self.model.filePath(self.tree.currentIndex())
        file_name = self.model.fileName(self.tree.currentIndex())
        editFileAction = QAction("Edit")
        editFileMenu = QMenu(self.tree)
        editFileMenu.addAction(editFileAction)
        editFileMenu.exec_(self.tree.mapToGlobal(position))
        if file_name == "bettergrass.properties":
            editFileAction.triggered.connect(self.open_bettergrassDialog)

    def edit_file(self, index):
        file_path = self.model.filePath(index)
        file_name = self.model.fileName(index)
        if file_name == "bettergrass.properties":
            print("bettergrass")
            self.open_bettergrassDialog()

    def open_bettergrassDialog(self):
        print("bettergrass")
        # self.path + "/assets/minecraft/optifine/bettergrass.properties"
        # bg = parse_bettergrass(self.path + "/assets/minecraft/optifine/bettergrass.properties")
        # print(bg)
        bettergrassDialog = BetterGrassDialog(self.path + "/assets/minecraft/optifine/bettergrass.properties")
        return(bettergrassDialog.exec())







if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TexturepackManager()
    ex.show()
    sys.exit(app.exec_())
