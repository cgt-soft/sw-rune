import sys
from ui.main_window import Ui_MainWindow
from ui.about import Ui_aboutDialog
from ui.prefrences import Ui_preferencesDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from src.rune_database import RuneDatabase
import src.settings as st
import logging
import pickle

__author__ = 'CGT'

logger = logging.getLogger(__name__)


class PreferencesDialog(QtWidgets.QDialog, Ui_preferencesDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_preferencesDialog.__init__(self)
        self.setupUi(self)
        flags = QtCore.Qt.Drawer | QtCore.Qt.WindowStaysOnTopHint
        self.setWindowFlags(flags)
        self.cancelButton.clicked.connect(self.close_preferences_window)

    def close_preferences_window(self):
        self.close()

class AboutDialog(QtWidgets.QDialog, Ui_aboutDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_aboutDialog.__init__(self)
        self.setupUi(self)
        flags = QtCore.Qt.Drawer | QtCore.Qt.WindowStaysOnTopHint
        self.setWindowFlags(flags)
        self.closeAbout.clicked.connect(self.close_about_window)

    def close_about_window(self):
        self.close()

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.rune_database = RuneDatabase()
        self.about_window = AboutDialog()
        self.preferences_window = PreferencesDialog()
        self.set_connections()
        self.load_from_pickle()

    def set_connections(self):
        self.actionQuit.triggered.connect(self.close)
        self.actionOpen.triggered.connect(self.open_csv)
        self.filtersButton.clicked.connect(self.apply_filters)
        self.actionAbout.triggered.connect(self.open_about_dialog)
        self.actionPreferences.triggered.connect(self.open_preferences_dialog)

    def open_preferences_dialog(self):
        self.preferences_window.show()

    def load_from_pickle(self):
        try:
            with open('data.pk', 'rb') as f:
                self.rune_database.rune_objects = pickle.load(f)
            self.populate_list(self.rune_database.rune_objects)
        except:
            pass

    def save_to_pickle(self):
        with open('data.pk','wb') as f:
            pickle.dump(self.rune_database.rune_objects, f)

    def open_about_dialog(self):
        self.about_window.show()

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
        if self.mainstatComboBox.currentText() == 'All':
            pass
        else:
            filtered_runes = [rune for rune in filtered_runes if self.mainstatComboBox.currentText() in rune.main_stat]
        self.statusBar().showMessage('{} runes filtered'.format(len(filtered_runes)))
        self.runeTableWidget.setRowCount(0)
        self.populate_list(filtered_runes)

    def open_csv(self):
        # file_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',"All Files (*);;CSV Files (*.csv)")
        options = QtWidgets.QFileDialog.Options()
        # options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',"",
                                                             "Comma Separated Values file(*.csv);;All Files (*)",
                                                             options=options)
        if file_name:
            self.statusBar().showMessage('reading file {}'.format(file_name))
            self.rune_database.read_from_csv(file_name)
            self.statusBar().showMessage('{} runes read'.format(str(len(self.rune_database.rune_list))))
            self.rune_database.to_objects()
            self.rune_database.statistics()
            self.rune_database.check_to_sell()
            self.populate_list(self.rune_database.rune_objects)

    def populate_list(self, rune_list):
        rune_id = 0
        for rune in rune_list:
            # tag = '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(rune.id, rune.equipped, rune.slot,
            #                                                       rune.rune_set, rune.level, rune.main_stat,
            #                                                       rune.sub_fixed, rune.subs, rune.mons_type,
            #                                                       rune.sums[rune.mons_type])
            # item = QtWidgets.QListWidgetItem()
            # item.setText(tag)
            data = [rune.equipped, rune.slot, rune.rune_set, rune.level, rune.main_stat,
                    rune.sub_fixed, rune.subs, rune.mons_type, float(round(rune.sums[rune.mons_type], 2))]
            position = self.runeTableWidget.rowCount()
            self.runeTableWidget.insertRow(position)
            for index, d in enumerate(data):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setText(str(d))
                if rune.sell:
                    item.setBackground(QtGui.QColor(200, 0, 0))
                else:
                    item.setBackground(QtGui.QColor(0, 200, 0))
                self.runeTableWidget.setItem(position, index, item)
        self.runeTableWidget.resizeColumnsToContents()

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QtWidgets.QMessageBox.Yes |
                                               QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            self.save_to_pickle()
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