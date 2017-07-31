import sys
from ui.main_window import Ui_MainWindow
from ui.about import Ui_aboutDialog
from ui.preferences import Ui_preferencesDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from src.rune_database import RuneDatabase
import src.pickle_settings as ps
import logging
import pickle
import json

__author__ = 'CGT'

logger = logging.getLogger(__name__)

# Catch PyQt tracebacks with Pycharm https://stackoverflow.com/a/37837374
# Back up the reference to the exceptionhook
sys._excepthook = sys.excepthook
def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)
# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook

# style_sheet = 'resources/qss/style_blue.qss'

class PreferencesDialog(QtWidgets.QDialog, Ui_preferencesDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_preferencesDialog.__init__(self)
        self.setupUi(self)
        flags = QtCore.Qt.Drawer | QtCore.Qt.WindowStaysOnTopHint
        self.setWindowFlags(flags)
        # self.buttonBox.button(QtWidgets.QDialogButtonBox.Apply).clicked.connect(self.apply_preferences)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(self.close_preferences_window)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.close_preferences_window)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.RestoreDefaults).clicked.connect(self.restore_default)
        self.addsetButton.clicked.connect(self.add_set)
        self.removesetButton.clicked.connect(self.remove_set)
        self.restore_settings('Custom')

    def remove_set(self):
        for item in self.setslistWidget.selectedItems():
            self.setslistWidget.takeItem(self.setslistWidget.row(item))

    def add_set(self):
        self.setslistWidget.addItem(self.setEdit.text())

    def restore_settings(self, key='Default'):
        self.settings = ps.load_settings(key=key)
        self.hp_doubleSpinBox.setValue(self.settings['SUB_WEIGHTS']['HP'])
        self.def_doubleSpinBox.setValue(self.settings['SUB_WEIGHTS']['DEF'])
        self.spd_doubleSpinBox.setValue(self.settings['SUB_WEIGHTS']['SPD'])
        self.cr_doubleSpinBox.setValue(self.settings['SUB_WEIGHTS']['CR'])
        self.cd_doubleSpinBox.setValue(self.settings['SUB_WEIGHTS']['CD'])
        self.atk_doubleSpinBox.setValue(self.settings['SUB_WEIGHTS']['ATK'])
        self.res_doubleSpinBox.setValue(self.settings['SUB_WEIGHTS']['RES'])
        self.acc_doubleSpinBox.setValue(self.settings['SUB_WEIGHTS']['ACC'])
        self.setslistWidget.clear()
        for item in self.settings['RUNE_SETS']:
            self.setslistWidget.addItem(item)
        txt = json.dumps(self.settings['MONS_TYPES'], sort_keys=True, indent=4)
        self.textEdit.clear()
        self.textEdit.insertPlainText(txt)

    def restore_default(self):
        self.restore_settings()

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
        self.about_window = AboutDialog()
        self.preferences_window = PreferencesDialog()
        self.settings = self.preferences_window.settings
        logger.debug('MyApp.__init__:')
        logger.debug(self.settings)
        self.rune_database = RuneDatabase()
        self.set_connections()
        self.load_from_pickle()

    def set_connections(self):
        self.actionQuit.triggered.connect(self.close)
        self.actionOpen.triggered.connect(self.open_csv)
        self.filtersButton.clicked.connect(self.apply_filters)
        self.actionAbout.triggered.connect(self.open_about_dialog)
        self.actionPreferences.triggered.connect(self.open_preferences_dialog)
        self.preferences_window.buttonBox.button(QtWidgets.QDialogButtonBox.Apply).clicked.connect(self.apply_preferences)

    def apply_preferences(self):
        self.settings['SUB_WEIGHTS']['HP'] = self.preferences_window.hp_doubleSpinBox.value()
        self.settings['SUB_WEIGHTS']['DEF'] = self.preferences_window.def_doubleSpinBox.value()
        self.settings['SUB_WEIGHTS']['SPD'] = self.preferences_window.spd_doubleSpinBox.value()
        self.settings['SUB_WEIGHTS']['CR'] = self.preferences_window.cr_doubleSpinBox.value()
        self.settings['SUB_WEIGHTS']['CD'] = self.preferences_window.cd_doubleSpinBox.value()
        self.settings['SUB_WEIGHTS']['ATK'] = self.preferences_window.atk_doubleSpinBox.value()
        self.settings['SUB_WEIGHTS']['RES'] = self.preferences_window.res_doubleSpinBox.value()
        self.settings['SUB_WEIGHTS']['ACC'] = self.preferences_window.acc_doubleSpinBox.value()
        self.settings['RUNE_SETS'].clear()
        for item in self.preferences_window.setslistWidget.findItems("", QtCore.Qt.MatchContains):
            self.settings['RUNE_SETS'].append(item.text())
        txt = self.preferences_window.textEdit.toPlainText()
        obj = json.loads(txt.strip())
        self.settings['MONS_TYPES'] = obj
        self.statusBar().showMessage('Applying settings...')
        logger.debug('Aplying Settings and saving to settings.pk:')
        logger.debug(self.settings)
        with open('settings.pk', 'rb') as f:
            data = pickle.load(f)
            data['Custom'] = self.settings
        with open('settings.pk', 'wb') as f:
            pickle.dump(data, f)

        self.rune_database.process_runes()
        self.rune_database.statistics()
        self.rune_database.check_to_sell()
        self.populate_list(self.rune_database.rune_objects)
        self.statusBar().showMessage('{} runes to sell, {} to keep'.format(len(self.rune_database.runes_to_sell()),
                                                                           len(self.rune_database.runes_to_keep())))


    def open_preferences_dialog(self):
        self.preferences_window.show()

    def load_from_pickle(self):
        try:
            with open('data.pk', 'rb') as f:
                self.rune_database.rune_objects = pickle.load(f)
            self.populate_list(self.rune_database.rune_objects)
            self.statusBar().showMessage('{} runes read'.format(str(len(self.rune_database.rune_objects))))
        except:
            pass

    def save_to_pickle(self):
        with open('data.pk','wb') as f:
            pickle.dump(self.rune_database.rune_objects, f)

    def open_about_dialog(self):
        self.about_window.show()

    def apply_filters(self):
        self.statusBar().showMessage('Applying filters...')
        if self.setComboBox.currentText() == 'All':
            # set_filter = st.RUNE_SETS
            set_filter = self.settings['RUNE_SETS']
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
            filtered_runes = [rune for rune in filtered_runes if rune.sell_final]
        else:
            filtered_runes = [rune for rune in filtered_runes if not rune.sell_final]
        if self.mainstatComboBox.currentText() == 'All':
            pass
        else:
            filtered_runes = [rune for rune in filtered_runes if self.mainstatComboBox.currentText() in rune.main_stat]
        self.populate_list(filtered_runes)
        self.statusBar().showMessage('{} runes filtered'.format(len(filtered_runes)))

    def open_csv(self):
        # file_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',"All Files (*);;CSV Files (*.csv)")
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',"",
                                                             "Comma Separated Values file(*.csv);;All Files (*)",
                                                             options=options)
        if file_name:
            self.statusBar().showMessage('reading file {}'.format(file_name))
            self.rune_database.read_from_csv(file_name)
            self.statusBar().showMessage('Processing {} runes...'.format(str(len(self.rune_database.rune_list))))
            self.rune_database.to_objects()
            self.rune_database.process_runes()
            self.rune_database.statistics()
            self.rune_database.check_to_sell()
            self.populate_list(self.rune_database.rune_objects)
            self.statusBar().showMessage('{} runes to sell, {} to keep'.format(len(self.rune_database.runes_to_sell()),
                                                                               len(self.rune_database.runes_to_keep())))

    def populate_list(self, rune_list):
        self.runeTableWidget.setRowCount(0)
        self.statusBar().showMessage('Populating list...')
        for rune in rune_list:
            # tag = '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(rune.id, rune.equipped, rune.slot,
            #                                                       rune.rune_set, rune.level, rune.main_stat,
            #                                                       rune.sub_fixed, rune.subs, rune.mons_type,
            #                                                       rune.sums[rune.mons_type])
            # item = QtWidgets.QListWidgetItem()
            # item.setText(tag)
            data = [rune.equipped, rune.slot, rune.rune_set, rune.level, rune.stars, rune.main_stat,
                    # rune.sub_fixed, rune.subs, rune.mons_type, float(round(rune.sums[rune.mons_type], 2))]
                    # rune.sub_fixed, rune.subs, rune.mons_type, float(round(rune.vpm_efficiency[rune.mons_type], 3))]
                    rune.sub_fixed, rune.subs, rune.mons_type, rune.vpm_efficiency[rune.mons_type], rune.max_efficiency]
            position = self.runeTableWidget.rowCount()
            self.runeTableWidget.insertRow(position)
            for index, d in enumerate(data):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setText(str(d))
                if rune.sell['VPM'] and rune.sell['Barion']:
                    item.setBackground(QtGui.QColor(200, 0, 0))
                elif rune.sell['VPM'] or rune.sell['Barion']:
                    item.setBackground(QtGui.QColor(255, 140, 0))
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

    # with open(style_sheet, "r") as fh:
    #     app.setStyleSheet(fh.read())

    window.show()
    sys.exit(app.exec_())