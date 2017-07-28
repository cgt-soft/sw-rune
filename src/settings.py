__author__ = 'CGT'
import pickle

RUNE_SETS = ['Energy', 'Swift', 'Blade', 'Fatal', 'Despair',
             'Violent', 'Focus', 'Guard', 'Endure', 'Shield', 'Revenge',
             'Rage', 'Will', 'Nemesis', 'Vampire', 'Destroy',
             '???']
PERC_SLOTS = [2, 4, 6]
FLAT_SLOTS = [1, 3, 5]
SPD_SLOT = [2]
AV_BASE_STATS = {'HP' : 9900, 'DEF' : 580, 'ATK' : 690, 'SPD' : 102}
SUB_WEIGHTS = {'HP' : 1.0, 'DEF' : 1.0, 'SPD' : 1.2,
               'CR' : 1.8, 'CD' : 1.8, 'ATK': 1.0,
               'RES' : 0.6, 'ACC' : 0.6}
SUB_INCREMENT = {'FLAT' : 5, 'PERC' : 11}
# TYPES = {'SUP' : {'SETS' : ['Energy', 'Swift', 'Despair',
#                   'Violent', 'Focus', 'Guard', 'Endure', 'Shield', 'Revenge',
#                   'Will', 'Nemesis', '???'],
#                   'SUBS' : ['HP', 'SPD', 'DEF', 'RES', 'ACC']},
#          'ATK' : {'SETS' : ['Energy', 'Swift', 'Blade', 'Fatal', 'Despair',
#                   'Violent', 'Focus', 'Guard', 'Endure', 'Shield', 'Revenge',
#                   'Rage', 'Will', 'Nemesis', 'Vampire', 'Destroy', '???'],
#                   'SUBS' : ['ATK', 'CR', 'CD', 'SPD', 'ACC', 'RES']}}
ABBREVIATIONS = { 'TNK' : 'Tank', 'PDD' : 'Pure Damage Dealer', 'VDD' : 'Violent Damage Dealer',
                  'SDD' : 'Speed Damage Dealer', 'ADD' : 'Accuracy Damage Dealer', 'RDD' : 'Raids Damage Dealer',
                  'HDD' : 'HP Damage Dealer', 'DDD' : 'DEF Damage Dealer', 'SSP' : 'Speed Support',
                  'RSP' : 'Raid Support', 'SDM' : 'Speed Demon', 'SCC' : 'Suport Crowd Control',
                  'DCC' : 'Damage Crowd Control', 'BMB' : 'Bomber'}
TYPES = {   'TNK': {    'SETS' : ['Energy', 'Guard', 'Endure', 'Shield', 'Revenge', 'Will', 'Nemesis', 'Focus', '???'],
                        'SUBS' : ['HP', 'DEF', 'RES']},
            'PDD': {    'SETS' : ['Fatal', 'Rage', 'Blade', 'Will', 'Nemesis', 'Vampire', 'Destroy', '???'],
                        'SUBS' : ['ATK', 'CR', 'CD']},
            'VDD': {    'SETS' : ['Violent', 'Blade', 'Will', 'Nemesis', 'Vampire', 'Destroy', '???'],
                        'SUBS' : ['ATK', 'CR', 'CD']},
            'SDD': {    'SETS' : ['Violent', 'Fatal', 'Rage', 'Will', 'Blade', 'Will', 'Nemesis', 'Vampire',
                                  'Destroy', 'Swift', 'Revenge', '???'],
                        'SUBS' : ['ATK', 'CR', 'CD', 'SPD']},
            'ADD': {    'SETS' : ['Violent', 'Blade', 'Will', 'Nemesis', 'Vampire', 'Destroy', 'Revenge',
                                  'Focus', 'Revenge', '???'],
                        'SUBS' : ['ATK', 'CR', 'CD', 'ACC']},
            'RDD': {    'SETS' : ['Violent', 'Fatal', 'Rage', 'Vampire', 'Blade', 'Will', 'Nemesis',
                                  'Revenge', 'Endure', '???'],
                        'SUBS' : ['ATK', 'CR', 'CD', 'RES']},
            'HDD': {    'SETS' : ['Violent', 'Fatal', 'Blade', 'Rage', 'Will', 'Nemesis', 'Vampire',
                                  'Energy', 'Destroy', 'Shield', '???'],
                        'SUBS' : ['HP', 'CR', 'CD']},
            'DDD': {    'SETS': ['Violent', 'Fatal', 'Blade', 'Rage', 'Will', 'Nemesis', 'Vampire',
                                 'Guard', 'Destroy', '???'],
                        'SUBS': ['DEF', 'CR', 'CD']},
            'SSP': {    'SETS': ['Violent', 'Swift', 'Energy', 'Will', 'Nemesis', 'Guard', 'Shield', '???'],
                        'SUBS': ['DEF', 'HP', 'SPD']},
            'RSP': {    'SETS': ['Violent', 'Swift', 'Energy', 'Will', 'Nemesis', 'Guard', 'Endure', 'Shield',
                                 'Revenge', '???'],
                        'SUBS': ['DEF', 'HP', 'SPD', 'RES']},
            'SDM': {    'SETS': ['Swift', 'Energy', 'Will', 'Nemesis', 'Guard', 'Shield', 'Endure', 'Blade', '???'],
                        'SUBS': ['SPD']},
            'SCC': {    'SETS': ['Despair', 'Energy', 'Will', 'Nemesis', 'Guard', 'Shield', 'Endure', 'Focus', '???'],
                        'SUBS': ['DEF', 'HP', 'SPD', 'ACC']},
            'DCC': {    'SETS': ['Despair', 'Blade', 'Will', 'Nemesis', 'Vampire', 'Destroy', '???'],
                        'SUBS': ['ATK', 'CR', 'CD', 'SPD', 'ACC']},
            'BMB': {    'SETS': ['Fatal', 'Violent', 'Energy', 'Will', 'Nemesis', 'Guard', 'Shield', 'Endure', '???'],
                        'SUBS': ['ATK', 'SPD', 'ACC']},
            'TOTAL': {  'SETS': RUNE_SETS,
                        'SUBS': ['DEF', 'HP', 'SPD', 'ACC', 'RES', 'ATK', 'CD', 'CR']}
}

SUB_INC = {'SPD': {'5': {'MIN': 3, 'MAX': 5},
                   '6': {'MIN': 4, 'MAX': 6}},
           'CR': {'5': {'MIN': 3, 'MAX': 5},
                  '6': {'MIN': 4, 'MAX': 6}},
           'CD': {'5': {'MIN': 3, 'MAX': 5},
                  '6': {'MIN': 4, 'MAX': 7}},
           'ATK': {'5': {'MIN': 4, 'MAX': 7},
                   '6': {'MIN': 5, 'MAX': 8}},
           'HP': {'5': {'MIN': 4, 'MAX': 7},
                  '6': {'MIN': 5, 'MAX': 8}},
           'DEF': {'5': {'MIN': 4, 'MAX': 7},
                   '6': {'MIN': 5, 'MAX': 8}},
           'ACC': {'5': {'MIN': 3, 'MAX': 7},
                   '6': {'MIN': 4, 'MAX': 8}},
           'RES': {'5': {'MIN': 3, 'MAX': 7},
                   '6': {'MIN': 4, 'MAX': 8}},
           }

MAIN_INC = {'HP': 16, 'ATK': 16, 'DEF': 16}

SUB_TRANS = {'SPD': 'SPD', 'HP': 'HP', 'DEF': 'DEF', 'ATK': 'ATK',
             'CRI Rate': 'CR', 'CRI Dmg': 'CD', 'Accuracy': 'ACC',
             'Resistance': 'RES'}

STAT_COMP = {'PERC': {'HP': 12, 'ATK': 12, 'DEF': 12, 'RES': 13, 'ACC': 13, 'CR': 11,'CD': 15},
             'FLAT': {'SPD': 3, 'HP': 360, 'ATK': 25, 'DEF': 25}}

MAX_VALUE = {'SPD': 42, 'HP': 63, 'ATK': 63, 'DEF': 63, 'RES': 64, 'ACC': 64, 'CR': 58,'CD': 80}

LEVEL_COMP = [28,28,28,21,21,21,14,14,14,7,7,7]

EFF_MODELS = ['Barion', 'VPM']

MODEL = ['VPM']



if __name__ == '__main__':
    settings = {'Default': {'SUB_WEIGHTS': SUB_WEIGHTS, 'RUNE_SETS' : RUNE_SETS, 'MONS_TYPES': TYPES,
                            'SUB_TRANS': SUB_TRANS, 'AV_BASE_STATS': AV_BASE_STATS, 'STAT_COMP': STAT_COMP,
                            'LEVEL_COMP': LEVEL_COMP, 'MAX_VALUE': MAX_VALUE}}
    print(settings)
    with open('settings.pk','wb') as f:
        pickle.dump(settings, f)