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
        preferencesDialog.resize(350, 225)
        self.gridLayout_3 = QtWidgets.QGridLayout(preferencesDialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.buttonBox = QtWidgets.QDialogButtonBox(preferencesDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_3.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(preferencesDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.hp_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.hp_doubleSpinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.hp_doubleSpinBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.hp_doubleSpinBox.setSingleStep(0.1)
        self.hp_doubleSpinBox.setProperty("value", 1.0)
        self.hp_doubleSpinBox.setObjectName("hp_doubleSpinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.hp_doubleSpinBox)
        self.def_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.def_doubleSpinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.def_doubleSpinBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.def_doubleSpinBox.setSingleStep(0.1)
        self.def_doubleSpinBox.setProperty("value", 1.0)
        self.def_doubleSpinBox.setObjectName("def_doubleSpinBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.def_doubleSpinBox)
        self.atk_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.atk_doubleSpinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.atk_doubleSpinBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.atk_doubleSpinBox.setSingleStep(0.1)
        self.atk_doubleSpinBox.setProperty("value", 1.0)
        self.atk_doubleSpinBox.setObjectName("atk_doubleSpinBox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.atk_doubleSpinBox)
        self.spd_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.spd_doubleSpinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.spd_doubleSpinBox.setMaximumSize(QtCore.QSize(50, 50))
        self.spd_doubleSpinBox.setSingleStep(0.1)
        self.spd_doubleSpinBox.setProperty("value", 1.2)
        self.spd_doubleSpinBox.setObjectName("spd_doubleSpinBox")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spd_doubleSpinBox)
        self.gridLayout_2.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.cr_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.cr_doubleSpinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.cr_doubleSpinBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.cr_doubleSpinBox.setSingleStep(0.1)
        self.cr_doubleSpinBox.setProperty("value", 1.8)
        self.cr_doubleSpinBox.setObjectName("cr_doubleSpinBox")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cr_doubleSpinBox)
        self.cd_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.cd_doubleSpinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.cd_doubleSpinBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.cd_doubleSpinBox.setSingleStep(0.1)
        self.cd_doubleSpinBox.setProperty("value", 1.8)
        self.cd_doubleSpinBox.setObjectName("cd_doubleSpinBox")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cd_doubleSpinBox)
        self.acc_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.acc_doubleSpinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.acc_doubleSpinBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.acc_doubleSpinBox.setSingleStep(0.1)
        self.acc_doubleSpinBox.setProperty("value", 0.6)
        self.acc_doubleSpinBox.setObjectName("acc_doubleSpinBox")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.acc_doubleSpinBox)
        self.res_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.res_doubleSpinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.res_doubleSpinBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.res_doubleSpinBox.setSingleStep(0.1)
        self.res_doubleSpinBox.setProperty("value", 0.6)
        self.res_doubleSpinBox.setObjectName("res_doubleSpinBox")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.res_doubleSpinBox)
        self.gridLayout_2.addLayout(self.formLayout_3, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        self.textEdit.raise_()
        self.textEdit.raise_()
        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_3.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.retranslateUi(preferencesDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(preferencesDialog)

    def retranslateUi(self, preferencesDialog):
        _translate = QtCore.QCoreApplication.translate
        preferencesDialog.setWindowTitle(_translate("preferencesDialog", "Preferences"))
        self.groupBox_2.setTitle(_translate("preferencesDialog", "Substat Weights"))
        self.label_5.setText(_translate("preferencesDialog", "HP"))
        self.label_6.setText(_translate("preferencesDialog", "DEF"))
        self.label_7.setText(_translate("preferencesDialog", "ATK"))
        self.label_8.setText(_translate("preferencesDialog", "SPD"))
        self.hp_doubleSpinBox.setSpecialValueText(_translate("preferencesDialog", "1.00"))
        self.label_9.setText(_translate("preferencesDialog", "CRI Rate"))
        self.label_10.setText(_translate("preferencesDialog", "CRI Dmg"))
        self.label_11.setText(_translate("preferencesDialog", "Accuracy"))
        self.label_12.setText(_translate("preferencesDialog", "Resistance"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("preferencesDialog", "General"))
        self.groupBox.setTitle(_translate("preferencesDialog", "Monster Types"))
        self.textEdit.setHtml(_translate("preferencesDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\">{\'TNK\': {    \'SETS\' : [\'Energy\', \'Guard\', \'Endure\', \'Shield\', \'Revenge\', \'Will\', \'Nemesis\', \'???\'],</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\">    \'SUBS\' : [\'HP\', \'DEF\', \'RES\']},</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\"> \'PDD\': {        \'SETS\' : [\'Fatal\', \'Rage\', \'Blade\', \'Will\', \'Nemesis\', \'Vampire\', \'Destroy\', \'???\'],</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\">    \'SUBS\' : [\'ATK\', \'CR\', \'CD\']},</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\"> \'VDD\': {        \'SETS\' : [\'Violent\', \'Blade\', \'Will\', \'Nemesis\', \'Vampire\', \'Destroy\', \'???\'],</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\">     \'SUBS\' : [\'ATK\', \'CR\', \'CD\']},</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\"> \'SDD\': {        \'SETS\' : [\'Violent\', \'Fatal\', \'Rage\', \'Will\', \'Blade\', \'Will\', \'Nemesis\', \'Vampire\',\'Destroy\', \'???\'],</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\">    \'SUBS\' : [\'ATK\', \'CR\', \'CD\', \'SPD\']},</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\"> \'ADD\': {        \'SETS\' : [\'Violent\', \'Blade\', \'Will\', \'Nemesis\', \'Vampire\', \'Destroy\', \'Revenge\', \'Focus\', \'???\'],</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\">    \'SUBS\' : [\'ATK\', \'CR\', \'CD\', \'ACC\']},</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\"> \'RDD\': {        \'SETS\' : [\'Violent\', \'Fatal\', \'Rage\', \'Vampire\', \'Blade\', \'Will\', \'Nemesis\', \'Revenge\', \'Destroy\', \'???\'],</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\">    \'SUBS\' : [\'ATK\', \'CR\', \'CD\', \'RES\']},</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\"> \'HDD\': {        \'SETS\' : [\'Violent\', \'Fatal\', \'Blade\', \'Rage\', \'Will\', \'Nemesis\', \'Vampire\', \'Energy\', \'Destroy\', \'Shield\', \'???\'],</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\">    \'SUBS\' : [\'HP\', \'CR\', \'CD\']},</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\"> \'DDD\': {        \'SETS\': [\'Violent\', \'Fatal\', \'Blade\', \'Rage\', \'Will\', \'Nemesis\', \'Vampire\', \'Guard\', \'Destroy\', \'???\'],</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\">    \'SUBS\': [\'DEF\', \'CR\', \'CD\']},</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\"> \'SSP\': {       \'SETS\': [\'Violent\', \'Swift\', \'Energy\', \'Will\', \'Nemesis\', \'Guard\', \'Shield\', \'???\'],</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\">    \'SUBS\': [\'DEF\', \'HP\', \'SPD\']},</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\"> \'RSP\': {        \'SETS\': [\'Violent\', \'Swift\', \'Energy\', \'Will\', \'Nemesis\', \'Guard\', \'Endure\', \'Shield\', \'???\'],</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\">     \'SUBS\': [\'DEF\', \'HP\', \'SPD\', \'RES\']},</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\"> \'SDM\': {        \'SETS\': [\'Swift\', \'Energy\', \'Will\', \'Nemesis\', \'Guard\', \'Shield\', \'Endure\', \'Blade\', \'???\'],</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\">    \'SUBS\': [\'SPD\']},</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\"> \'CCT\': {        \'SETS\': [\'Despair\', \'Energy\', \'Will\', \'Nemesis\', \'Guard\', \'Shield\', \'Endure\', \'???\'],</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\">    \'SUBS\': [\'DEF\', \'HP\', \'SPD\', \'ACC\']},</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\"> \'BMB\': {        \'SETS\': [\'Fatal\', \'Violent\', \'Energy\', \'Will\', \'Nemesis\', \'Guard\', \'Shield\', \'Endure\', \'???\'],</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\">    \'SUBS\': [\'ATK\', \'SPD\', \'ACC\']}}</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("preferencesDialog", "Advanced"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    preferencesDialog = QtWidgets.QDialog()
    ui = Ui_preferencesDialog()
    ui.setupUi(preferencesDialog)
    preferencesDialog.show()
    sys.exit(app.exec_())

