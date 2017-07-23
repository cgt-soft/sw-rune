__author__ = 'CGT'
RUNE_SETS = ['Energy', 'Swift', 'Blade', 'Fatal', 'Despair',
             'Violent', 'Focus', 'Guard', 'Endure', 'Shield', 'Revenge',
             'Rage', 'Will', 'Nemesis', 'Vampire', 'Destroy',
             '???']
PERC_SLOTS = [2, 4, 6]
FLAT_SLOTS = [1, 3, 5]
SPD_SLOT = [2]
AV_BASE_STATS = {'HP' : 9900, 'DEF' : 580, 'ATK' : 690, 'SPD' : 102}
SUB_WEIGHTS = {'HP' : 1, 'DEF' : 1, 'SPD' : 1.2,
               'CR' : 1.8, 'CD' : 1.8, 'ATK': 1,
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
                  'RSP' : 'Raid Support', 'SDM' : 'Speed Demon', 'CCT' : 'Crowd Control', 'BMB' : 'Bomber'}
TYPES = {   'TNK': {    'SETS' : ['Energy', 'Guard', 'Endure', 'Shield', 'Revenge', 'Will', 'Nemesis', '???'],
                        'SUBS' : ['HP', 'DEF', 'RES']},
            'PDD': {    'SETS' : ['Fatal', 'Rage', 'Blade', 'Will', 'Nemesis', 'Vampire', 'Destroy', '???'],
                        'SUBS' : ['ATK', 'CR', 'CD']},
            'VDD': {    'SETS' : ['Violent', 'Blade', 'Will', 'Nemesis', 'Vampire', 'Destroy', '???'],
                        'SUBS' : ['ATK', 'CR', 'CD']},
            'SDD': {    'SETS' : ['Violent', 'Fatal', 'Rage', 'Will', 'Blade', 'Will', 'Nemesis', 'Vampire',
                                  'Destroy', '???'],
                        'SUBS' : ['ATK', 'CR', 'CD', 'SPD']},
            'ADD': {    'SETS' : ['Violent', 'Blade', 'Will', 'Nemesis', 'Vampire', 'Destroy', 'Revenge',
                                  'Focus', '???'],
                        'SUBS' : ['ATK', 'CR', 'CD', 'ACC']},
            'RDD': {    'SETS' : ['Violent', 'Fatal', 'Rage', 'Vampire', 'Blade', 'Will', 'Nemesis',
                                  'Revenge', 'Destroy', '???'],
                        'SUBS' : ['ATK', 'CR', 'CD', 'RES']},
            'HDD': {    'SETS' : ['Violent', 'Fatal', 'Blade', 'Rage', 'Will', 'Nemesis', 'Vampire',
                                  'Energy', 'Destroy', 'Shield', '???'],
                        'SUBS' : ['HP', 'CR', 'CD']},
            'DDD': {    'SETS': ['Violent', 'Fatal', 'Blade', 'Rage', 'Will', 'Nemesis', 'Vampire',
                                 'Guard', 'Destroy', '???'],
                        'SUBS': ['DEF', 'CR', 'CD']},
            'SSP': {    'SETS': ['Violent', 'Swift', 'Energy', 'Will', 'Nemesis', 'Guard', 'Shield', '???'],
                        'SUBS': ['DEF', 'HP', 'SPD']},
            'RSP': {    'SETS': ['Violent', 'Swift', 'Energy', 'Will', 'Nemesis', 'Guard', 'Endure', 'Shield', '???'],
                        'SUBS': ['DEF', 'HP', 'SPD', 'RES']},
            'SDM': {    'SETS': ['Swift', 'Energy', 'Will', 'Nemesis', 'Guard', 'Shield', 'Endure', 'Blade', '???'],
                        'SUBS': ['SPD']},
            'CCT': {    'SETS': ['Despair', 'Energy', 'Will', 'Nemesis', 'Guard', 'Shield', 'Endure', '???'],
                        'SUBS': ['DEF', 'HP', 'SPD', 'ACC']},
            'BMB': {    'SETS': ['Fatal', 'Violent', 'Energy', 'Will', 'Nemesis', 'Guard', 'Shield', 'Endure', '???'],
                        'SUBS': ['ATK', 'SPD', 'ACC']},
}