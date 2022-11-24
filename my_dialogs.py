import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from my_functions import *
from sqlite3 import connect
from my_classes import RandomEntityParagraph


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


class RandomEntityDialog(QDialog):
    def __init__(self, path):
        super().__init__()
        uic.loadUi("RandomEntityDialog2UI.ui", self)
        self.setup_entityinput()
        self.paragraphs = dict()
        self.path = path
        self.current = 0
        self.biomesbutton.clicked.connect(self.open_biomeinput)
        self.professionsbutton.clicked.connect(self.open_professionsinput)
        self.colorsbutton.clicked.connect(self.open_colorsinput)
        self.weatherbutton.clicked.connect(self.open_weatherinput)
        self.addbutton.clicked.connect(self.add_paragraph)
        self.commitbutton.clicked.connect(self.edit_current_paragraph)
        self.deletebutton.clicked.connect(self.delete_last_paragraph)
        self.paragraphsview.itemClicked.connect(self.setup_current_paragraph)
        self.buttonBox.accepted.connect(self.create_random_entity_properties)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)


    def setup_entityinput(self):
        entities = entities_list()
        self.entityinput.addItems(entities)

    def add_paragraph(self):
        n = len(self.paragraphs) + 1
        self.paragraphs[n] = RandomEntityParagraph(n, [])
        self.paragraphsview.addItem(str(n))
        print(self.paragraphs)

    def delete_last_paragraph(self):
        n = int(self.paragraphsview.takeItem(len(self.paragraphs) - 1).text())
        self.paragraphs.pop(n)

    def setup_current_paragraph(self):
        self.current = int(self.paragraphsview.currentItem().text())
        # print(self.paragraphs[self.current])
        # print(self.current)
        self.texturesinput.setText(self.paragraphs[self.current].textures_str())
        self.weightsinput.setText(self.paragraphs[self.current].weights)
        self.heightsinput.setText(self.paragraphs[self.current].heights)
        self.nameinput.setText(self.paragraphs[self.current].name)
        if self.paragraphs[self.current].baby:
            self.c_baby.setCheckState(2)
        else:
            self.c_baby.setCheckState(0)
        self.healthinput.setText(self.paragraphs[self.current].health)
        self.mooninput.setText(self.paragraphs[self.current].moon_phase)
        self.timeinput.setText(self.paragraphs[self.current].day_time)
        self.sizesinput.setText(self.paragraphs[self.current].sizes)

    def edit_current_paragraph(self):
        self.current = int(self.paragraphsview.currentItem().text())
        c = self.current
        self.paragraphs[c].textures = self.texturesinput.text()
        self.paragraphs[c].weights = self.weightsinput.text()
        self.paragraphs[c].heights = self.heightsinput.text()
        self.paragraphs[c].name = self.nameinput.text()
        self.paragraphs[c].moon_phase = self.mooninput.text()
        self.paragraphs[c].day_time = self.timeinput.text()
        self.paragraphs[c].health = self.healthinput.text()
        self.paragraphs[c].sizes = self.sizesinput.text()
        self.paragraphs[c].baby = self.c_baby.isChecked()

    def open_biomeinput(self):
        # print(self.current, self.paragraphs[self.current].biomes)
        biomeinput = MultipleSelectionDialog("biomes", self.paragraphs[self.current].biomes)
        biomeinput.exec()
        self.paragraphs[self.current].biomes += biomeinput.selected.copy()

    def open_professionsinput(self):
        if "villager" in self.entityinput.currentText():
            professionsinput = MultipleSelectionDialog("professions", self.paragraphs[self.current].professions)
            professionsinput.exec()
            p = professionsinput.selected.copy()
            for el in p:
                el += ":" + self.levelinput.text()
            self.paragraphs[self.current].professions += p
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Parameter is not available for this entity")
            dlg.setText("Only villagers have professions!")
            dlg.exec()

    def open_colorsinput(self):
        text = self.entityinput.currentText()
        if "cat" in text or "wolf" in text or "shulker" in text or "llama" in text:
            colorsinput = MultipleSelectionDialog("colors", self.paragraphs[self.current].colors)
            colorsinput.exec()
            c = colorsinput.selected.copy()
            self.paragraphs[self.current].colors += c
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Parameter is not available for this entity")
            dlg.setText("Only cats, tamed wolves, llamas and shulkers have colors!")
            dlg.exec()

    def open_weatherinput(self):
        weatherinput = MultipleSelectionDialog("weather", self.paragraphs[self.current].weather)
        weatherinput.exec()
        self.paragraphs[self.current].weather += weatherinput.selected

    def create_random_entity_properties(self):
        for el in self.paragraphs:
            print(str(self.paragraphs[el]))
        new_path = self.path + get_entity_path(self.entityinput.currentText())
        create_random_entity(new_path, self.paragraphs)

class MultipleSelectionDialog(QDialog):
    def __init__(self, table, already_selected):
        super().__init__()
        uic.loadUi("MultipleSelectionDialogUI.ui", self)
        data = data_list(table)
        self.selected = []
        for el in data:
            self.listWidget.addItem(QListWidgetItem(el))
        if already_selected:
            for i in range(self.listWidget.count() - 1):
                if self.listWidget.item(i).text() in already_selected:
                    self.listWidget.item(i).setSelected(True)
        self.buttonBox.accepted.connect(self.end)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def end(self):
        items = self.listWidget.selectedItems()
        x = []
        for i in range(len(items)):
            x.append(str(self.listWidget.selectedItems()[i].text()))
        self.selected += x
        print(self.selected)



