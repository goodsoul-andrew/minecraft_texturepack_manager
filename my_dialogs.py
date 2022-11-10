import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from my_functions import *


class NewDialog(QDialog):
    def __init__(self):
        super().__init__()
        # self.setupUi(self)
        uic.loadUi("NewDialogUI.ui", self)
        self.setWindowTitle("Create a new texturepack")
        self.path, self.outer_path, self.version, self.description = "", "", "", ""
        v = ["1.18", "1.17 - 1.17.1", "1.16.2 - 1.16.5", "1.15 - 1.16.1",
             "1.13 - 1.14.4", "1.11 - 1.12.2", "1.9 - 1.10.2", "1.6.1 - 1.8.9"]
        for el in v:
            self.versioninput.addItem(el)
        self.pathbutton.clicked.connect(self.choose_folder)
        self.chooseicon.clicked.connect(self.choose_icon)
        self.nameinput.textChanged.connect(self.change_text_pathview)
        self.buttonBox.accepted.connect(self.create_new_texturepack)
        self.buttonBox.rejected.connect(self.reject)

    def choose_folder(self):
        self.outer_path = QFileDialog.getExistingDirectory(self, "Choose folder", "C:/Users")
        self.name = self.nameinput.text()
        self.path = self.outer_path + "/" + self.name
        self.outer_directory = QDir(self.outer_path)
        self.pathview.setText(self.path)
        self.directory = QDir(self.path)

    def choose_icon(self):
        self.icon_path = QFileDialog.getOpenFileName(self, 'Choose icon', 'C:/Users')[0]
        # print(icon_path)
        pixmap = QPixmap(self.icon_path)
        self.iconview.setPixmap(pixmap)

    def change_text_pathview(self):
        if self.outer_path:
            self.name = self.nameinput.text()
            self.path = self.outer_path + "/" + self.name
            self.pathview.setText(self.path)

    def create_new_texturepack(self):
        if self.outer_path:
            self.outer_directory.mkdir(self.name)
            self.directory.mkdir("assets")
            copy_icon(self.icon_path, self.path + "/pack.png")
            current_path = self.path + "/assets"
            self.directory.cd("assets")
            self.directory.mkdir("minecraft")

            self.version = self.versioninput.currentText()
            self.description = self.descriptioninput.toPlainText()
            create_pack_mcmeta(self.path, self.version, self.description)

            self.directory.cd("minecraft")

            if self.c_blockstates.isChecked():
                self.directory.mkdir("models")
            if self.c_fonts.isChecked():
                self.directory.mkdir("font")
            if self.c_models.isChecked():
                self.directory.mkdir("models")
                p = self.directory.currentPath() + "/assets/minecraft/models"
                models_dir = QDir(p)
                models_dir.mkdir("block")
                models_dir.mkdir("item")
            if self.c_lang.isChecked():
                self.directory.mkdir("lang")
            if self.c_splashes.isChecked() or self.c_end.isChecked():
                self.directory.mkdir("texts")

            if (self.c_block.isChecked() or self.c_armor_models.isChecked() or self.c_colormap.isChecked() or self.c_entity.isChecked()
                    or self.c_environment.isChecked() or self.c_font_textures.isChecked() or self.c_gui.isChecked() or self.c_item.isChecked()
                    or self.c_map.isChecked() or self.c_misc.isChecked() or self.c_mob_effect.isChecked() or self.c_painting.isChecked()
                    or self.c_particle.isChecked()):
                self.directory.mkdir("textures")
                textures_dir = QDir(self.path + "/assets/minecraft/textures")
                if self.c_block.isChecked():
                    textures_dir.mkdir("block")

                if self.c_colormap.isChecked():
                    textures_dir.mkdir("colormap")
                if self.c_entity.isChecked():
                    textures_dir.mkdir("entity")
                if self.c_environment.isChecked():
                    textures_dir.mkdir("environment")
                if self.c_font_textures.isChecked():
                    textures_dir.mkdir("font")
                if self.c_gui.isChecked():
                    textures_dir.mkdir("gui")
                if self.c_item.isChecked():
                    textures_dir.mkdir("item")
                if self.c_armor_models.isChecked():
                    textures_dir.mkdir("models")
                if self.c_map.isChecked():
                    textures_dir.mkdir("map")
                if self.c_misc.isChecked():
                    textures_dir.mkdir("misc")
                if self.c_mob_effect.isChecked():
                    textures_dir.mkdir("mob_effect")
                if self.c_painting.isChecked():
                    textures_dir.mkdir("painting")
                if self.c_particle.isChecked():
                    textures_dir.mkdir("particle")
            self.close()

    def cancel(self):
        print("cancelled")
        self.close()

    def hello(self):
        print("Hello")