# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        aboutDialog.setObjectName("aboutDialog")
        aboutDialog.resize(430, 320)
        aboutDialog.setMinimumSize(QtCore.QSize(430, 320))
        aboutDialog.setMaximumSize(QtCore.QSize(430, 320))
        self.gridLayout = QtWidgets.QGridLayout(aboutDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(aboutDialog)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.closeAbout = QtWidgets.QPushButton(aboutDialog)
        self.closeAbout.setObjectName("closeAbout")
        self.gridLayout.addWidget(self.closeAbout, 1, 0, 1, 1)

        self.retranslateUi(aboutDialog)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

    def retranslateUi(self, aboutDialog):
        _translate = QtCore.QCoreApplication.translate
        aboutDialog.setWindowTitle(_translate("aboutDialog", "About"))
        self.label.setText(_translate("aboutDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Developed by cgt-soft</span></p><p align=\"center\"><br/></p><p align=\"center\"><a href=\"https://github.com/cgt-soft/\"><span style=\" text-decoration: underline; color:#0000ff;\">github.com/cgt-soft/</span></a></p></body></html>"))
        self.closeAbout.setText(_translate("aboutDialog", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aboutDialog = QtWidgets.QDialog()
    ui = Ui_aboutDialog()
    ui.setupUi(aboutDialog)
    aboutDialog.show()
    sys.exit(app.exec_())

