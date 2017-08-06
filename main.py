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

colors = {'Sell': QtGui.QColor(255, 122, 122),
          'Keep': QtGui.QColor(130, 244, 107),
          'Power Up': QtGui.QColor(255, 171, 68),
          'Reappraise': QtGui.QColor(142, 226, 255),
          'Check': QtGui.QColor(249, 247, 97)
}

# Make directory in %APPDATA%
appdata_path = os.path.join(os.environ['APPDATA'], __app_name__)
print(appdata_path)
if not os.path.exists(appdata_path):
    os.makedirs(appdata_path)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)

        logging.getLogger(__name__).addHandler(logging.NullHandler())
        self.logger = logging.getLogger(__name__)
        self.logger.info('Starting app: %s', __app_name__)

        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('swrc-icon.png'))
        # self.runeTableWidget.
        self.settings = QtCore.QSettings(QtCore.QSettings.IniFormat, QtCore.QSettings.UserScope, __app_name__, __app_name__)
        if not self.settings.value('Preferences'):
            self.settings.setValue('Preferences', default_settings)
        self.classification = self.settings.value('Preferences')['classification']
        self.classComboBox.clear()
        if self.classification == 'Custom':
            classes = ['All'] + list(self.settings.value('Preferences')[self.classification]['monster_types'].keys())
        else:
            classes = ['All'] + list(self.settings.value('Preferences')[self.classification]['classes'].values())
        # print(classes)
        self.classComboBox.addItems(classes)
        self.setComboBox.clear()
        self.setComboBox.addItems(['All'] + self.settings.value('Preferences')['rune_sets'])
        self.rune_database = RuneDatabase(self.settings.value('Preferences'))
        self.worker_thread = WorkerThread(rune_database=self.rune_database)
        self.set_connections()


    def set_connections(self):
        self.actionExit.triggered.connect(self.close)
        self.actionOpen.triggered.connect(self.open_action_triggered)
        self.actionAbout.triggered.connect(self.about_action_triggered)
        self.actionPreferences.triggered.connect(self.preferrences_action_triggered)
        self.filtersButton.clicked.connect(self.apply_filters_button_clicked)
        self.classifyButton.clicked.connect(self.classify_button_clicked)
        self.worker_thread.data_signal.connect(self.worker_thread_finished)
        self.worker_thread.progress_signal.connect(self.update_progress_bar)
        # self.thread.signal.connect(self.finished)

    def update_progress_bar(self, val):
        self.progressBar.setValue(val)

    def worker_thread_finished(self, rune_database=None):
        self.rune_database = rune_database
        self.classComboBox.clear()
        if self.classification == 'Custom':
            classes = ['All'] + list(self.settings.value('Preferences')[self.classification]['monster_types'].keys())
        else:
            classes = ['All'] + list(self.settings.value('Preferences')[self.classification]['classes'].values())
        self.classComboBox.addItems(classes)
        self.populate_list(self.rune_database.rune_objects)

    def classify_button_clicked(self):
        self.rune_database.settings = self.settings.value('Preferences')
        # print(self.rune_database.settings)
        self.statusBar().showMessage('Processing {} runes...'.format(len(self.rune_database.rune_objects)))
        self.worker_thread.start()
        # self.rune_database = self.worker_thread.rune_database
        # self.populate_list(self.rune_database.rune_objects)

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
        filters = [set_filter, slot_filter, stars_filter]
        self.logger.debug(filters)
        self.logger.debug(len(self.rune_database.rune_objects))
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
            filtered_runes = [rune for rune in filtered_runes if rune.status == 'Sell']
        elif self.statusComboBox.currentText() == 'Check':
            filtered_runes = [rune for rune in filtered_runes if rune.status == 'Check']
        elif self.statusComboBox.currentText() == 'Keep':
            filtered_runes = [rune for rune in filtered_runes if rune.status == 'Keep']
        elif self.statusComboBox.currentText() == 'Reappraise':
            filtered_runes = [rune for rune in filtered_runes if rune.status == 'Reappraise']
        elif self.statusComboBox.currentText() == 'Power Up':
            filtered_runes = [rune for rune in filtered_runes if rune.status == 'Power Up']
        if self.mainstatComboBox.currentText() == 'All':
            pass
        else:
            filtered_runes = [rune for rune in filtered_runes if
                              self.mainstatComboBox.currentText() in rune.main_stat]
        class_filter = self.classComboBox.currentText()
        if class_filter == 'All':
            pass
        else:
            if self.classification == 'Custom':
                filtered_runes = [rune for rune in filtered_runes if
                                  rune.mons_type == class_filter]
            else:
                c = self.settings.value('Preferences')[self.classification]['classes']
                key = list(c.keys())[list(c.values()).index(class_filter)]
                filtered_runes = [rune for rune in filtered_runes if
                                  rune.mons_type == key]
        if self.qualityComboBox.currentText() == 'All':
            pass
        else:
            filtered_runes = [rune for rune in filtered_runes if
                              rune.original_quality == self.qualityComboBox.currentText()]
        self.logger.debug(filtered_runes)
        self.populate_list(filtered_runes)
        self.statusBar().showMessage('{} runes filtered'.format(len(filtered_runes)))

    def preferrences_action_triggered(self):
        preferences_dialog = PreferencesDialog(settings=self.settings.value('Preferences'))
        signal = preferences_dialog.apply_signal
        signal.connect(self.apply_preferences)
        preferences_dialog.exec_()

    def apply_preferences(self, preferences):
        self.settings.setValue('Preferences', preferences)
        self.classification = self.settings.value('Preferences')['classification']

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
                                                             "JSON file (*.json);;Comma Separated Values file (*.csv);;All Files (*)",
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
            self.worker_thread.rune_database = self.rune_database
            self.worker_thread.start()
            # self.rune_database = self.worker_thread.rune_database
            # self.populate_list(self.rune_database.rune_objects)

    def populate_list(self, rune_list):
        self.runeTableWidget.setRowCount(0)
        self.runeTableWidget.setSortingEnabled(False)
        self.statusBar().showMessage('Populating list...')
        for rune in rune_list:
            if rune.mons_type in self.settings.value('Preferences')[self.classification]['classes']:
                mons_type = self.settings.value('Preferences')[self.classification]['classes'][rune.mons_type]
            else:
                mons_type = rune.mons_type
            data = [rune.equipped, rune.original_quality, rune.slot, rune.rune_set, rune.level, rune.stars, rune.main_stat,
                    rune.sub_fixed, rune.subs, mons_type, "{0:.2f}".format(rune.vpm_efficiency[rune.mons_type]),
                    "{0:.2f}".format(rune.barion_efficiency)]
            position = self.runeTableWidget.rowCount()
            self.runeTableWidget.insertRow(position)
            for index, d in enumerate(data):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                font = QtGui.QFont()
                font.setBold(True)
                item.setFont(font)
                # item.setTextColor(QtGui.QColor(0, 0, 0))
                item.setText(str(d))
                item.setBackground(colors[rune.status])
                self.runeTableWidget.setItem(position, index, item)
        self.runeTableWidget.resizeColumnsToContents()
        self.runeTableWidget.setSortingEnabled(True)
        self.statusBar().showMessage(
            '{} runes to sell, {} runes to reappraise, {} runes to check, {} to power up, {} to keep'.format(
            len(self.rune_database.runes_to_sell()), len(self.rune_database.runes_to_reappraise()),
            len(self.rune_database.runes_to_check()), len(self.rune_database.runes_to_power_up()),
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


class WorkerThread(QtCore.QThread):
    data_signal = QtCore.pyqtSignal(object)
    progress_signal = QtCore.pyqtSignal(int)

    def __init__(self, parent=None, rune_database=object):
        super(WorkerThread, self).__init__(parent)
        logging.getLogger(__name__).addHandler(logging.NullHandler())
        logger = logging.getLogger(__name__)
        logger.info('Starting app: %s', __app_name__)

        self.rune_database = rune_database

    def run(self):
        maxval = len(self.rune_database.rune_objects)
        val = 0
        for rune in self.rune_database.rune_objects:
            rune.settings = self.rune_database.settings
            rune.process()
            val += 1
            self.progress_signal.emit(int(val/maxval*100))
        # self.rune_database.process_runes()
        self.rune_database.statistics()
        self.rune_database.check_to_sell()
        self.data_signal.emit(self.rune_database)

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