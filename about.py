from ui_files.about_ui import Ui_aboutDialog
from PyQt5 import QtCore, QtWidgets


class AboutDialog(QtWidgets.QDialog, Ui_aboutDialog):
    def __init__(self, parent=None):
        super(AboutDialog, self).__init__(parent)
        self.setupUi(self)
        flags = QtCore.Qt.Drawer | QtCore.Qt.WindowStaysOnTopHint
        self.setWindowFlags(flags)
        self.closeAbout.clicked.connect(self.close_about_window)

    def close_about_window(self):
        self.close()