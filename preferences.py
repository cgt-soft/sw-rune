from ui_files.preferences_ui import Ui_preferencesDialog
from PyQt5 import QtGui, QtCore, QtWidgets
import json

default_settings = {'rune_sets': ['Energy', 'Guard', 'Swift', 'Blade', 'Rage', 'Focus', 'Endure', 'Fatal', 'Despair',
                                  'Vampire', 'Violent', 'Nemesis', 'Will', 'Shield', 'Revenge', 'Destroy', 'Fight',
                                  'Determination', 'Enhance', 'Accuracy', 'Tolerance'],
                    'substat_weights': {'HP': 1.0, 'DEF': 1.0, 'SPD': 1.2, 'CR': 1.8, 'CD': 1.8, 'ATK': 1.0,
                                        'RES': 0.6, 'ACC': 0.6},
                    'classes': { 'TNK' : 'Tank', 'PDD' : 'Pure Damage Dealer', 'VDD' : 'Violent Damage Dealer',
                                 'SDD' : 'Speed Damage Dealer', 'ADD' : 'Accuracy Damage Dealer',
                                 'RDD' : 'Raids Damage Dealer', 'HDD' : 'HP Damage Dealer', 'DDD' : 'DEF Damage Dealer',
                                 'SSP' : 'Speed Support', 'RSP' : 'Raid Support', 'SDM' : 'Speed Demon',
                                 'SCC' : 'Suport Crowd Control', 'DCC' : 'Damage Crowd Control', 'BMB' : 'Bomber'},
                    'monster_types': {'TNK': {'SETS': ['Energy', 'Guard', 'Endure', 'Shield', 'Revenge', 'Will',
                                                       'Nemesis', 'Focus', 'Fight', 'Determination', 'Enhance',
                                                       'Accuracy', 'Tolerance'],
                                              'SUBS': ['HP', 'DEF', 'RES']},
                                      'PDD': {'SETS': ['Fatal', 'Rage', 'Blade', 'Will', 'Nemesis', 'Vampire',
                                                       'Destroy', 'Fight', 'Determination', 'Enhance', 'Accuracy',
                                                       'Tolerance'],
                                              'SUBS': ['ATK', 'CR', 'CD']},
                                      'VDD': {'SETS': ['Violent', 'Blade', 'Will', 'Nemesis', 'Vampire', 'Destroy',
                                                       'Fight', 'Determination', 'Enhance', 'Accuracy', 'Tolerance'],
                                              'SUBS': ['ATK', 'CR', 'CD']},
                                      'SDD': {'SETS': ['Violent', 'Fatal', 'Rage', 'Will', 'Blade', 'Will',
                                                       'Nemesis', 'Vampire', 'Destroy', 'Swift', 'Revenge',
                                                       'Fight', 'Determination', 'Enhance', 'Accuracy', 'Tolerance'],
                                              'SUBS': ['ATK', 'CR', 'CD', 'SPD']},
                                      'ADD': {'SETS': ['Violent', 'Blade', 'Will', 'Nemesis', 'Vampire', 'Destroy',
                                                       'Revenge', 'Focus', 'Revenge', 'Fight', 'Determination',
                                                       'Enhance', 'Accuracy', 'Tolerance'],
                                              'SUBS': ['ATK', 'CR', 'CD', 'ACC']},
                                      'RDD': {'SETS' : ['Violent', 'Fatal', 'Rage', 'Vampire', 'Blade', 'Will',
                                                               'Nemesis', 'Revenge', 'Endure', 'Fight', 'Determination',
                                                               'Enhance', 'Accuracy', 'Tolerance'],
                                              'SUBS' : ['ATK', 'CR', 'CD', 'RES']},
                                      'HDD': {'SETS' : ['Violent', 'Fatal', 'Blade', 'Rage', 'Will', 'Nemesis',
                                                               'Vampire', 'Revenge', 'Energy', 'Destroy', 'Shield',
                                                               'Fight', 'Determination', 'Enhance', 'Accuracy', 'Tolerance'],
                                              'SUBS' : ['HP', 'CR', 'CD']},
                                      'DDD': {'SETS': ['Violent', 'Fatal', 'Blade', 'Rage', 'Will', 'Nemesis',
                                                              'Vampire', 'Revenge', 'Guard', 'Destroy', 'Fight',
                                                              'Determination', 'Enhance', 'Accuracy', 'Tolerance'],
                                              'SUBS': ['DEF', 'CR', 'CD']},
                                      'SSP': {'SETS': ['Violent', 'Swift', 'Energy', 'Will', 'Nemesis', 'Guard',
                                                              'Shield', 'Fight', 'Determination', 'Enhance', 'Accuracy',
                                                              'Tolerance'],
                                              'SUBS': ['DEF', 'HP', 'SPD']},
                                      'RSP': {'SETS': ['Violent', 'Swift', 'Energy', 'Will', 'Nemesis', 'Guard',
                                                              'Endure', 'Shield', 'Revenge', 'Fight', 'Determination',
                                                              'Enhance', 'Accuracy', 'Tolerance'],
                                              'SUBS': ['DEF', 'HP', 'SPD', 'RES']},
                                      'SDM': {'SETS': ['Swift', 'Energy', 'Will', 'Nemesis', 'Guard', 'Shield',
                                                              'Endure', 'Blade', 'Fight', 'Determination', 'Enhance',
                                                              'Accuracy', 'Tolerance'],
                                              'SUBS': ['SPD']},
                                      'SCC': {'SETS': ['Despair', 'Energy', 'Will', 'Nemesis', 'Guard', 'Shield',
                                                              'Endure', 'Focus', 'Fight', 'Determination', 'Enhance',
                                                              'Accuracy', 'Tolerance'],
                                              'SUBS': ['DEF', 'HP', 'SPD', 'ACC']},
                                      'DCC': {'SETS': ['Despair', 'Blade', 'Will', 'Nemesis', 'Vampire',
                                                              'Destroy', 'Fight', 'Determination', 'Enhance',
                                                              'Accuracy', 'Tolerance'],
                                                     'SUBS': ['ATK', 'CR', 'CD', 'SPD', 'ACC']},
                                      'BMB': {'SETS': ['Fatal', 'Violent', 'Energy', 'Will', 'Nemesis', 'Guard',
                                                              'Shield', 'Endure', 'Fight', 'Determination', 'Enhance',
                                                              'Accuracy', 'Tolerance'],
                                              'SUBS': ['ATK', 'SPD', 'ACC']},
                                      'TOTAL': {'SETS': ['Energy', 'Swift', 'Blade', 'Fatal', 'Despair', 'Violent',
                                                              'Focus', 'Guard', 'Endure', 'Shield', 'Revenge', 'Rage',
                                                              'Will', 'Nemesis', 'Vampire', 'Destroy', 'Fight',
                                                              'Determination', 'Enhance', 'Accuracy', 'Tolerance'],
                                                'SUBS': ['DEF', 'HP', 'SPD', 'ACC', 'RES', 'ATK', 'CD', 'CR']}},
                    'sub_trans': {'SPD': 'SPD', 'HP': 'HP', 'DEF': 'DEF', 'ATK': 'ATK', 'CRI Rate': 'CR',
                                  'CRI Dmg': 'CD', 'Accuracy': 'ACC', 'Resistance': 'RES'},
                    'stat_compensation': {'PERC': {'HP': 12, 'ATK': 12, 'DEF': 12, 'RES': 13, 'ACC': 13, 'CR': 11,'CD': 15},
                                          'FLAT': {'SPD': 3, 'HP': 360, 'ATK': 25, 'DEF': 25}},
                    'max_value': {'SPD': 42, 'HP': 63, 'ATK': 63, 'DEF': 63, 'RES': 64, 'ACC': 64, 'CR': 58,'CD': 80},
                    'level_compensation': [28,28,28,21,21,21,14,14,14,7,7,7],
                    'average_base_stats': {'HP' : 9900, 'DEF' : 580, 'ATK' : 690, 'SPD' : 102}
}


class PreferencesDialog(QtWidgets.QDialog, Ui_preferencesDialog):

    apply_signal = QtCore.pyqtSignal(object)

    def __init__(self, parent=None, settings=default_settings):
        super(PreferencesDialog, self).__init__(parent)
        self.setupUi(self)
        flags = QtCore.Qt.Drawer | QtCore.Qt.WindowStaysOnTopHint
        self.setWindowFlags(flags)
        self.settings = settings
        self.set_connections()
        self.restore_settings()

    def set_connections(self):
        self.buttonBox.clicked.connect(self.button_box_clicked)
        self.addsetButton.clicked.connect(self.add_set_button_clicked)
        self.removesetButton.clicked.connect(self.remove_set_button_clicked)

    def add_set_button_clicked(self):
        text = self.setEdit.toPlainText()
        item = QtWidgets.QListWidgetItem(text)
        self.setslistWidget.addItem(item)

    def remove_set_button_clicked(self):
        for item in self.setslistWidget.selectedItems():
            self.setslistWidget.takeItem(self.setslistWidget.row(item))

    def restore_settings(self):
        # Set spin boxes
        self.hp_doubleSpinBox.setValue(self.settings['substat_weights']['HP'])
        self.def_doubleSpinBox.setValue(self.settings['substat_weights']['DEF'])
        self.atk_doubleSpinBox.setValue(self.settings['substat_weights']['ATK'])
        self.spd_doubleSpinBox.setValue(self.settings['substat_weights']['SPD'])
        self.cr_doubleSpinBox.setValue(self.settings['substat_weights']['CR'])
        self.cd_doubleSpinBox.setValue(self.settings['substat_weights']['CD'])
        self.acc_doubleSpinBox.setValue(self.settings['substat_weights']['ACC'])
        self.res_doubleSpinBox.setValue(self.settings['substat_weights']['RES'])
        # Set list with rune sets
        self.setslistWidget.clear()
        for rune_set in self.settings['rune_sets']:
            item = QtWidgets.QListWidgetItem(rune_set)
            self.setslistWidget.addItem(item)
        # Set json monster types (Advanzed Tab9
        txt = json.dumps(self.settings['monster_types'], sort_keys=True, indent=4)
        self.textEdit.clear()
        self.textEdit.insertPlainText(txt)

    def button_box_clicked(self, button):
        sb = self.buttonBox.standardButton(button)
        if sb == QtWidgets.QDialogButtonBox.Apply:
            self.apply_button_clicked()
        elif sb == QtWidgets.QDialogButtonBox.Cancel:
            print('Cancel Clicked')
        elif sb == QtWidgets.QDialogButtonBox.Ok:
            self.close()
        elif sb == QtWidgets.QDialogButtonBox.RestoreDefaults:
            self.settings = default_settings
            self.restore_settings()

    def apply_button_clicked(self):
        self.settings['substat_weights']['HP'] = self.hp_doubleSpinBox.value()
        self.settings['substat_weights']['DEF'] = self.def_doubleSpinBox.value()
        self.settings['substat_weights']['ATK'] = self.atk_doubleSpinBox.value()
        self.settings['substat_weights']['SPD'] = self.spd_doubleSpinBox.value()
        self.settings['substat_weights']['CD'] = self.cd_doubleSpinBox.value()
        self.settings['substat_weights']['CR'] = self.cr_doubleSpinBox.value()
        self.settings['substat_weights']['ACC'] = self.acc_doubleSpinBox.value()
        self.settings['substat_weights']['RES'] = self.res_doubleSpinBox.value()
        self.settings['rune_sets'].clear()
        for item in self.setslistWidget.findItems("", QtCore.Qt.MatchContains):
            self.settings['rune_sets'].append(item.text())
        txt = self.textEdit.toPlainText()
        obj = json.loads(txt.strip())
        self.settings['monster_types'] = obj
        self.apply_signal.emit(self.settings)
        # self.close()

    def default_button_clicked(self):
        pass