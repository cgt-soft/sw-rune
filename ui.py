import sys
from ui.main_window import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from src.rune_database import RuneDatabase
import src.settings as st
import logging

__author__ = 'CGT'

logger = logging.getLogger(__name__)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.rune_database = RuneDatabase()
        self.set_connections()

    def set_connections(self):
        self.actionQuit.triggered.connect(self.close)
        self.actionOpen.triggered.connect(self.open_csv)
        self.filtersButton.clicked.connect(self.apply_filters)

    def apply_filters(self):
        if self.setComboBox.currentText() == 'All':
            set_filter = st.RUNE_SETS
        else:
            set_filter = self.setComboBox.currentText()
        if self.slotComboBox.currentText() == 'All':
            slot_filter = [x for x in range(1,7)]
        elif self.slotComboBox.currentText() == 'Even':
            slot_filter = [x for x in range(2, 7, 2)]
        elif self.slotComboBox.currentText() == 'Odd':
            slot_filter = [x for x in range(1, 7, 2)]
        else:
            slot_filter = [int(self.slotComboBox.currentText())]
        if self.starsComboBox.currentText() == 'All':
            stars_filter = [x for x in range(1,7)]
        else:
            stars_filter = [int(self.starsComboBox.currentText())]
        print(stars_filter)
        filtered_runes = [rune for rune in self.rune_database.rune_objects
                          if rune.rune_set in set_filter and rune.slot in slot_filter
                          and rune.stars in stars_filter
                          and rune.level >= int(self.minLevelComboBox.currentText())
                          and rune.level <= int(self.maxLevelComboBox.currentText())]
        if self.equippedComboBox.currentText() == 'All':
            pass
        elif self.equippedComboBox.currentText() == 'Yes':
            filtered_runes = [rune for rune in filtered_runes if rune.equipped != '0']
        else:
            filtered_runes = [rune for rune in filtered_runes if rune.equipped == '0']
        if self.statusComboBox.currentText() == 'All':
            pass
        elif self.statusComboBox.currentText() == 'Sell':
            filtered_runes = [rune for rune in filtered_runes if rune.sell]
        else:
            filtered_runes = [rune for rune in filtered_runes if not rune.sell]
        #TODO mainstat filter
        self.statusBar().showMessage('{} runes filtered'.format(len(filtered_runes)))
        self.runeListWidget.clear()
        self.populate_list(filtered_runes)

    def open_csv(self):
        # file_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',"All Files (*);;CSV Files (*.csv)")
        options = QtWidgets.QFileDialog.Options()
        # options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',"",
                                                             "Comma Separated Values file(*.csv);;All Files (*)",
                                                             options=options)
        if file_name:
            print(file_name)
            self.statusBar().showMessage('reading file {}'.format(file_name))
            self.rune_database.read_from_csv(file_name)
            self.statusBar().showMessage('{} runes read'.format(str(len(self.rune_database.rune_list))))
            self.rune_database.to_objects()
            self.rune_database.statistics()
            self.rune_database.check_to_sell()
            self.populate_list(self.rune_database.rune_objects)

    def populate_list(self, rune_list):
        for rune in rune_list:
            tag = '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(rune.id, rune.equipped, rune.slot,
                                                                  rune.rune_set, rune.level, rune.main_stat,
                                                                  rune.sub_fixed, rune.subs, rune.mons_type,
                                                                  rune.sums[rune.mons_type])
            item = QtWidgets.QListWidgetItem()
            item.setText(tag)
            if rune.sell:
                item.setBackground(QtGui.QColor(200, 0, 0))
            else:
                item.setBackground(QtGui.QColor(0, 200, 0))
            self.runeListWidget.addItem(item)

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QtWidgets.QMessageBox.Yes |
                                               QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    import logging.config
    logging.basicConfig(filename="test.log", filemode='w', level=logging.DEBUG)
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())