import sys
from ui.main_window import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from src.rune_database import RuneDatabase


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

    def open_csv(self):
        # file_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',"All Files (*);;CSV Files (*.csv)")
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        print(file_name)
        self.statusBar().showMessage('reading file {}'.format(file_name))
        self.rune_database.read_from_csv(file_name)
        self.statusBar().showMessage('{} runes read'.format(str(len(self.rune_database.rune_list))))
        self.rune_database.to_objects()
        self.rune_database.statistics()
        self.rune_database.check_to_sell()
        self.populate_list()

    def populate_list(self):
        for rune in self.rune_database.rune_objects:
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
            self.listWidget.addItem(item)

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