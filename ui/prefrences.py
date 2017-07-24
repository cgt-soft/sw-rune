# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_preferencesDialog(object):
    def setupUi(self, preferencesDialog):
        preferencesDialog.setObjectName("preferencesDialog")
        preferencesDialog.resize(583, 434)
        self.widget = QtWidgets.QWidget(preferencesDialog)
        self.widget.setGeometry(QtCore.QRect(170, 390, 239, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.defaultButton = QtWidgets.QPushButton(self.widget)
        self.defaultButton.setObjectName("defaultButton")
        self.horizontalLayout.addWidget(self.defaultButton)
        self.saveButton = QtWidgets.QPushButton(self.widget)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.cancelButton = QtWidgets.QPushButton(self.widget)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)

        self.retranslateUi(preferencesDialog)
        QtCore.QMetaObject.connectSlotsByName(preferencesDialog)

    def retranslateUi(self, preferencesDialog):
        _translate = QtCore.QCoreApplication.translate
        preferencesDialog.setWindowTitle(_translate("preferencesDialog", "Prefrences"))
        self.defaultButton.setText(_translate("preferencesDialog", "Default"))
        self.saveButton.setText(_translate("preferencesDialog", "Save"))
        self.cancelButton.setText(_translate("preferencesDialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    preferencesDialog = QtWidgets.QDialog()
    ui = Ui_preferencesDialog()
    ui.setupUi(preferencesDialog)
    preferencesDialog.show()
    sys.exit(app.exec_())

