from ui_files.main_window_ui import Ui_MainWindow
from src.rune_database import RuneDatabase
from about import AboutDialog
from preferences import PreferencesDialog, default_settings
from PyQt5 import QtCore, QtWidgets, QtGui
import pickle, os, sys

__author__ = 'cgt'
__web__ = 'https://cgt-soft.github.io/'
__app_name__ = 'SWRuneClassifier'
__version__ = '0.1'

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

# Make directory in %APPDATA%
appdata_path = os.path.join(os.environ['APPDATA'], __app_name__)
print(appdata_path)
if not os.path.exists(appdata_path):
    os.makedirs(appdata_path)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)

        logging.getLogger(__name__).addHandler(logging.NullHandler())
        logger = logging.getLogger(__name__)
        logger.info('Starting app: %s', __app_name__)

        self.setupUi(self)
        self.settings = QtCore.QSettings(QtCore.QSettings.IniFormat, QtCore.QSettings.UserScope, __app_name__, __app_name__)
        if not self.settings.value('Preferences'):
            self.settings.setValue('Preferences', default_settings)
        self.rune_database = RuneDatabase(self.settings.value('Preferences'))
        self.set_connections()


    def set_connections(self):
        self.actionExit.triggered.connect(self.close)
        self.actionOpen.triggered.connect(self.open_action_triggered)
        self.actionAbout.triggered.connect(self.about_action_triggered)
        self.actionPreferences.triggered.connect(self.preferrences_action_triggered)
        self.filtersButton.clicked.connect(self.apply_filters_button_clicked)
        self.classifyButton.clicked.connect(self.classify_button_clicked)

    def classify_button_clicked(self):
        self.rune_database.settings = self.settings.value('Preferences')
        self.statusBar().showMessage('Processing {} runes...'.format(len(self.rune_database.rune_objects)))
        self.rune_database.process_runes()
        self.statusBar().showMessage('Calculating statistics...')
        self.rune_database.statistics()
        self.statusBar().showMessage('Classifying...')
        self.rune_database.check_to_sell()
        self.populate_list(self.rune_database.rune_objects)

    def apply_filters_button_clicked(self):
        self.statusBar().showMessage('Applying filters...')
        if self.setComboBox.currentText() == 'All':
            # set_filter = st.RUNE_SETS
            set_filter = self.settings.value('Preferences')['rune_sets']
        else:
            set_filter = self.setComboBox.currentText()
        if self.slotComboBox.currentText() == 'All':
            slot_filter = [x for x in range(1, 7)]
        elif self.slotComboBox.currentText() == 'Even':
            slot_filter = [x for x in range(2, 7, 2)]
        elif self.slotComboBox.currentText() == 'Odd':
            slot_filter = [x for x in range(1, 7, 2)]
        else:
            slot_filter = [int(self.slotComboBox.currentText())]
        if self.starsComboBox.currentText() == 'All':
            stars_filter = [x for x in range(1, 7)]
        else:
            stars_filter = [int(self.starsComboBox.currentText())]
        filtered_runes = [
            rune for rune in self.rune_database.rune_objects if (rune.rune_set in set_filter and
                                                                 rune.slot in slot_filter and
                                                                 rune.stars in stars_filter and
                                                                 rune.level >= int(self.minLevelComboBox.currentText()) and
                                                                 rune.level <= int(self.maxLevelComboBox.currentText()))
                          ]
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
            filtered_runes = [rune for rune in filtered_runes if
                              self.mainstatComboBox.currentText() in rune.main_stat]
        self.populate_list(filtered_runes)
        self.statusBar().showMessage('{} runes filtered'.format(len(filtered_runes)))

    def preferrences_action_triggered(self):
        preferences_dialog = PreferencesDialog(settings=self.settings.value('Preferences'))
        signal = preferences_dialog.apply_signal
        signal.connect(self.apply_preferences)
        preferences_dialog.exec_()

    def apply_preferences(self, preferences):
        self.settings.setValue('Preferences', preferences)

    def load_from_pickle(self):
        path = os.path.join(appdata_path,'data.pk')
        try:
            with open(path, 'rb') as f:
                self.rune_database.rune_objects = pickle.load(f)
            self.populate_list(self.rune_database.rune_objects)
        except:
            self.open_action_triggered()

    def save_to_pickle(self):
        path = os.path.join(appdata_path, 'data.pk')
        with open(path,'wb') as f:
            pickle.dump(self.rune_database.rune_objects, f)

    def about_action_triggered(self):
        about_window = AboutDialog()
        about_window.exec_()

    def open_action_triggered(self):
        options = QtWidgets.QFileDialog.DontUseNativeDialog
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',"",
                                                             "Comma Separated Values file (*.csv);;JSON file (*.json);;All Files (*)",
                                                             options=options)
        if file_name:
            extension = os.path.splitext(file_name)[1]
            if extension == '.csv':
                self.statusBar().showMessage('Opening csv file {}'.format(file_name))
                self.rune_database.read_from_csv(file_name)
            elif extension == '.json':
                self.statusBar().showMessage('Opening json file {}'.format(file_name))
                self.rune_database.read_from_json(file_name)
            else:
                QtWidgets.QMessageBox.warning(self, "Warning!", "Invalid file format {}".format(extension))
                return
            self.rune_database.process_runes()
            self.rune_database.statistics()
            self.rune_database.check_to_sell()
            self.populate_list(self.rune_database.rune_objects)

    def populate_list(self, rune_list):
        self.runeTableWidget.setRowCount(0)
        self.statusBar().showMessage('Populating list...')
        for rune in rune_list:
            data = [rune.equipped, rune.slot, rune.rune_set, rune.level, rune.stars, rune.main_stat,
                    rune.sub_fixed, rune.subs, rune.mons_type,
                    "{0:.2f}".format(100*rune.vpm_efficiency[rune.mons_type]), rune.barion_efficiency]
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
        self.statusBar().showMessage('{} runes to sell, {} to keep'.format(len(self.rune_database.runes_to_sell()),
                                                                           len(self.rune_database.runes_to_keep())))

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Message',
                                               'Are you sure to quit?', QtWidgets.QMessageBox.Yes |
                                               QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            self.save_to_pickle()
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    import logging.config
    logging.basicConfig(filename=os.path.join(appdata_path,'logging.log'), filemode='w', level=logging.DEBUG,
                        format="%(asctime)-15s: %(name)-18s - %(levelname)-8s - %(module)-15s - %(funcName)-20s - %(lineno)-6d - %(message)s")

    QtCore.QCoreApplication.setApplicationName(__app_name__)
    QtCore.QCoreApplication.setApplicationVersion(__version__)
    QtCore.QCoreApplication.setOrganizationName(__author__)
    QtCore.QCoreApplication.setOrganizationDomain(__web__)

    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.setWindowTitle(__app_name__)
    window.show()
    window.load_from_pickle()
    sys.exit(app.exec_())