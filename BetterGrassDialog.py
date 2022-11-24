from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from BetterGrassDialogUI import UI_BetterGrassDialor
from my_functions import *


class BetterGrassDialog(QDialog, UI_BetterGrassDialor):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.open_path = convert_pack_path(path + "/textures")
        # uic.loadUi("BetterGrassDialogUI.ui", self)
        self.setupUi(self)
        self.setWindowTitle("Edit bettergrass.properties")
        self.bg = parse_bettergrass(self.path)
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
        if self.bg["grass"] == True:
            self.c_grass.setCheckState(2)
        else:
            self.c_grass.setCheckState(0)
        if self.bg["dirt_path"] == True:
            self.c_dirt_path.setCheckState(2)
        else:
            self.c_dirt_path.setCheckState(0)
        if self.bg["mycelium"] == True:
            self.c_mycelium.setCheckState(2)
        else:
            self.c_mycelium.setCheckState(0)
        if self.bg["podzol"] == True:
            self.c_podzol.setCheckState(2)
        else:
            self.c_podzol.setCheckState(0)
        if self.bg["crimson_nylium"] == True:
            self.c_crimson_nylium.setCheckState(2)
        else:
            self.c_crimson_nylium.setCheckState(0)
        if self.bg["warped_nylium"] == True:
            self.c_warped_nylium.setCheckState(2)
        else:
            self.c_warped_nylium.setCheckState(0)
        if self.bg["grass.snow"] == True:
            self.c_grass_snow.setCheckState(2)
        else:
            self.c_grass_snow.setCheckState(0)
        if self.bg["mycelium.snow"] == True:
            self.c_mycelium_snow.setCheckState(2)
        else:
            self.c_mycelium_snow.setCheckState(0)
        if self.bg["podzol.snow"] == True:
            self.c_podzol_snow.setCheckState(2)
        else:
            self.c_podzol_snow.setCheckState(0)

    def setup_labels(self):
        self.grass_pathview.setText(self.bg["texture.grass"])
        self.grass_side_pathview.setText(self.bg["texture.grass_side"])
        self.dirt_path_pathview.setText(self.bg["texture.dirt_path"])
        self.dirt_path_side_pathview.setText(self.bg["texture.dirt_path_side"])
        self.mycelium_pathview.setText(self.bg["texture.mycelium"])
        self.podzol_pathview.setText(self.bg["texture.podzol"])
        self.crimson_nylium_pathview.setText(self.bg["texture.crimson_nylium"])
        self.warped_nylium_pathview.setText(self.bg["texture.warped_nylium"])
        self.snow_pathview.setText(self.bg["texture.snow"])

    def change_grass_path(self):
        new = QFileDialog.getOpenFileName(self, 'Choose icon', self.open_path)[0]
        if "assets/minecraft" in new:
            self.grass_pathview.setText(convert_texture_path(new))

    def change_grass_side_path(self):
        new = QFileDialog.getOpenFileName(self, 'Choose icon', self.open_path)[0]
        if "assets/minecraft" in new:
            self.grass_side_pathview.setText(convert_texture_path(new))

    def change_dirt_path_path(self):
        new = QFileDialog.getOpenFileName(self, 'Choose icon', self.open_path)[0]
        if "assets/minecraft" in new:
            self.dirt_path_pathview.setText(convert_texture_path(new))

    def change_dirt_path_side_path(self):
        new = QFileDialog.getOpenFileName(self, 'Choose icon', self.open_path)[0]
        if "assets/minecraft" in new:
            self.dirt_path_side_pathview.setText(convert_texture_path(new))

    def change_mycelium_path(self):
        new = QFileDialog.getOpenFileName(self, 'Choose icon', self.open_path)[0]
        if "assets/minecraft" in new:
            self.mycelium_pathview.setText(convert_texture_path(new))

    def change_podzol_path(self):
        new = QFileDialog.getOpenFileName(self, 'Choose icon', self.open_path)[0]
        if "assets/minecraft" in new:
            self.podzol_pathview.setText(convert_texture_path(new))

    def change_crimson_nylium_path(self):
        new = QFileDialog.getOpenFileName(self, 'Choose icon', self.open_path)[0]
        if "assets/minecraft" in new:
            self.crimson_nylium_pathview.setText(convert_texture_path(new))

    def change_warped_nylium_path(self):
        new = QFileDialog.getOpenFileName(self, 'Choose icon', self.open_path)[0]
        if "assets/minecraft" in new:
            self.warped_nylium_pathview.setText(convert_texture_path(new))

    def change_snow_path(self):
        new = QFileDialog.getOpenFileName(self, 'Choose icon', self.open_path)[0]
        if "assets/minecraft" in new:
            self.snow_nylium_pathview.setText(convert_texture_path(new))

    def change_bettergrass(self):
        self.bg["grass"] = convert_bool_str(self.c_grass.isChecked(), case="lowercase")
        self.bg["dirt_path"] = convert_bool_str(self.c_dirt_path.isChecked(), case="lowercase")
        self.bg["mycelium"] = convert_bool_str(self.c_mycelium.isChecked(), case="lowercase")
        self.bg["podzol"] = convert_bool_str(self.c_podzol.isChecked(), case="lowercase")
        self.bg["crimson_nylium"] = convert_bool_str(self.c_crimson_nylium.isChecked(), case="lowercase")
        self.bg["warped_nylium"] = convert_bool_str(self.c_warped_nylium.isChecked(), case="lowercase")
        self.bg["grass.snow"] = convert_bool_str(self.c_grass_snow.isChecked(), case="lowercase")
        self.bg["mycelium.snow"] = convert_bool_str(self.c_mycelium_snow.isChecked(), case="lowercase")
        self.bg["podzol.snow"] = convert_bool_str(self.c_podzol_snow.isChecked(), case="lowercase")

        self.bg["texture.grass"] = self.grass_pathview.text()
        self.bg["texture.grass_side"] = self.grass_side_pathview.text()
        self.bg["texture.dirt_path"] = self.dirt_path_pathview.text()
        self.bg["texture.dirt_path_side"] = self.dirt_path_side_pathview.text()
        self.bg["texture.mycelium"] = self.mycelium_pathview.text()
        self.bg["texture.podzol"] = self.podzol_pathview.text()
        self.bg["texture.crimson_nylium"] = self.crimson_nylium_pathview.text()
        self.bg["texture.warped_nylium"] = self.warped_nylium_pathview.text()
        self.bg["texture.snow"] = self.snow_pathview.text()
        new_path = self.path[:self.path.rfind("/")]
        create_bettergrass(new_path, self.bg)


    def hello(self):
        print("hello")
