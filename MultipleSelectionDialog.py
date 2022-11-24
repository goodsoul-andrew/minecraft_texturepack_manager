from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from my_functions import *
from MultipleSelectionDialogUI import Ui_MultipleSelectionDialog


class MultipleSelectionDialog(QDialog, Ui_MultipleSelectionDialog):
    def __init__(self, table, already_selected):
        super().__init__()
        # uic.loadUi("MultipleSelectionDialogUI.ui", self)
        self.setupUi(self)
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