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
        self.buttonBox.accepted.connect(self.accept)
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
            copy_file(self.icon_path, self.path + "/pack.png")
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

            if (self.c_anim.isChecked() or self.c_bettergrass.isChecked() or self.c_cem.isChecked()
                    or self.c_ctm.isChecked() or self.c_dynamic_light.isChecked() or self.c_emissive.isChecked()
                    or self.c_gui_o.isChecked() or self.c_lightmap.isChecked() or self.c_loading.isChecked() or self.c_panoramas.isChecked()
                    or self.c_random_entities.isChecked() or self.c_random_paintings.isChecked() or self.c_sky.isChecked()):
                self.directory.mkdir("optifine")
                optifine_dir = QDir(self.path + "/assets/minecraft/optifine")
                if self.c_anim.isChecked():
                    optifine_dir.mkdir("anim")
                if self.c_cem.isChecked():
                    optifine_dir.mkdir("cem")
                if self.c_ctm.isChecked():
                    optifine_dir.mkdir("ctm")
                if self.c_gui_o.isChecked():
                    optifine_dir.mkdir("gui")
                if self.c_loading.isChecked():
                    optifine_dir.mkdir("loading")
                if self.c_random_entities.isChecked() or self.c_random_paintings.isChecked():
                    optifine_dir.mkdir("random")
                    if self.c_random_entities.isChecked():
                        optifine_dir.mkdir("random/entity")
                    if self.c_random_paintings.isChecked():
                        optifine_dir.mkdir("random/paintings")

                if self.c_bettergrass.isChecked():
                    create_bettergrass(self.path + "/assets/minecraft/optifine")

            self.close()

    def hello(self):
        print("Hello")


class BetterGrassDialog(QDialog):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.open_path = convert_pack_path(path + "/textures")
        uic.loadUi("BetterGrassDialogUI.ui", self)
        self.setWindowTitle("Edit bettergrass.properties")
        self.setup_checkboxes()
        self.setup_labels()
        self.grass_pathbutton.clicked.connect(self.change_grass_path)
        self.grass_side_pathbutton.clicked.connect(self.change_grass_side_path)
        self.dirt_path_pathbutton.clicked.connect(self.change_dirt_path_path)
        self.dirt_path_side_pathbutton.clicked.connect(self.change_dirt_path_side_path)
        self.mycelium_pathbutton.clicked.connect(self.change_mycelium_path)
        self.podzol_pathbutton.clicked.connect(self.change_podzol_path)
        self.crimson_nylium_pathbutton.clicked.connect(self.change_crimson_nylium_path)
        self.warped_nylium_pathbutton.clicked.connect(self.change_warped_nylium_path)
        self.snow_pathbutton.clicked.connect(self.change_snow_path)
        self.buttonBox.accepted.connect(self.change_bettergrass)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.accepted.connect(self.reject)

    def setup_checkboxes(self):
        path = self.path
        print(path)
        bg = parse_bettergrass(path)
        print(bg)
        if bg["grass"] == True:
            self.c_grass.setCheckState(2)
        else:
            self.c_grass.setCheckState(0)
        if bg["dirt_path"] == True:
            self.c_dirt_path.setCheckState(2)
        else:
            self.c_dirt_path.setCheckState(0)
        if bg["mycelium"] == True:
            self.c_mycelium.setCheckState(2)
        else:
            self.c_mycelium.setCheckState(0)
        if bg["podzol"] == True:
            self.c_podzol.setCheckState(2)
        else:
            self.c_podzol.setCheckState(0)
        if bg["crimson_nylium"] == True:
            self.c_crimson_nylium.setCheckState(2)
        else:
            self.c_crimson_nylium.setCheckState(0)
        if bg["warped_nylium"] == True:
            self.c_warped_nylium.setCheckState(2)
        else:
            self.c_warped_nylium.setCheckState(0)
        if bg["grass_snow"] == True:
            self.c_grass_snow.setCheckState(2)
        else:
            self.c_grass_snow.setCheckState(0)
        if bg["mycelium_snow"] == True:
            self.c_mycelium_snow.setCheckState(2)
        else:
            self.c_mycelium_snow.setCheckState(0)
        if bg["podzol_snow"] == True:
            self.c_podzol_snow.setCheckState(2)
        else:
            self.c_podzol_snow.setCheckState(0)

    def setup_labels(self):
        path = self.path
        bg = parse_bettergrass(path)
        self.grass_pathview.setText(bg["texture.grass"])
        self.grass_side_pathview.setText(bg["texture.grass_side"])
        self.dirt_path_pathview.setText(bg["texture.dirt_path"])
        self.dirt_path_side_pathview.setText(bg["texture.dirt_path_side"])
        self.mycelium_pathview.setText(bg["texture.mycelium"])
        self.podzol_pathview.setText(bg["texture.podzol"])
        self.crimson_nylium_pathview.setText(bg["texture.crimson_nylium"])
        self.warped_nylium_pathview.setText(bg["texture.warped_nylium"])
        self.snow_pathview.setText(bg["texture.snow"])

    def change_grass_path(self):
        new = QFileDialog.getOpenFileName(self, 'Choose icon', self.open_path)[0]
        self.grass_pathview.setText(convert_texture_path(new))

    def change_grass_side_path(self):
        new = QFileDialog.getOpenFileName(self, 'Choose icon', self.open_path)[0]
        self.grass_side_pathview.setText(convert_texture_path(new))

    def change_dirt_path_path(self):
        new = QFileDialog.getOpenFileName(self, 'Choose icon', self.open_path)[0]
        self.dirt_path_pathview.setText(convert_texture_path(new))

    def change_dirt_path_side_path(self):
        new = QFileDialog.getOpenFileName(self, 'Choose icon', self.open_path)[0]
        self.dirt_path_side_pathview.setText(convert_texture_path(new))

    def change_mycelium_path(self):
        new = QFileDialog.getOpenFileName(self, 'Choose icon', self.open_path)[0]
        self.mycelium_pathview.setText(convert_texture_path(new))

    def change_podzol_path(self):
        new = QFileDialog.getOpenFileName(self, 'Choose icon', self.open_path)[0]
        self.podzol_pathview.setText(convert_texture_path(new))

    def change_crimson_nylium_path(self):
        new = QFileDialog.getOpenFileName(self, 'Choose icon', self.open_path)[0]
        self.crimson_nylium_pathview.setText(convert_texture_path(new))

    def change_warped_nylium_path(self):
        new = QFileDialog.getOpenFileName(self, 'Choose icon', self.open_path)[0]
        self.warped_nylium_pathview.setText(convert_texture_path(new))

    def change_snow_path(self):
        new = QFileDialog.getOpenFileName(self, 'Choose icon', self.open_path)[0]
        self.snow_nylium_pathview.setText(convert_texture_path(new))

    def change_bettergrass(self):
        pass

    def hello(self):
        print("hello")

