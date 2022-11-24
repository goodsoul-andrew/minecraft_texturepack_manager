from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from my_functions import *
from RandomEntityDialogUI import Ui_RandomEntityDialog
from my_classes import RandomEntityParagraph
from MultipleSelectionDialog import MultipleSelectionDialog


class RandomEntityDialog(QDialog, Ui_RandomEntityDialog):
    def __init__(self, path):
        super().__init__()
        # uic.loadUi("RandomEntityDialog2UI.ui", self)
        self.setupUi(self)
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