import logging
import src.settings as st
import src.pickle_settings as ps


__author__ = 'CGT'

logger = logging.getLogger(__name__)


class Rune(object):
    settings = ps.load_settings('Custom')
    # print(settings)

    def __init__(self, data_list):
        logger.debug('Initialize rune, id = %s', data_list[0])
        self.id = data_list[0]
        self.equipped = data_list[1]
        self.rune_set = data_list[2]
        self.slot = int(data_list[3])
        self.stars = int(data_list[4])
        self.level = int(data_list[5])
        self.price = data_list[6]
        self.main_stat = data_list[7]
        self.sub_fixed = data_list[8]
        self.subs = data_list[9:13]
        self.current_efficiency = data_list[13]
        self.max_efficiency = data_list[14]
        self.stats = {key: 0 for key in self.settings['SUB_WEIGHTS'].keys()}
        if self.level == 15:
            self.max_stats = self.stats
        else:
            self.max_stats = {key: {'MIN': 0, 'MAX': 0} for key in self.settings['SUB_WEIGHTS'].keys()}
        self.grinded = False
        self.sums = {key: 0 for key in self.settings['MONS_TYPES'].keys()}
        self.sell = True
        self.n_subs = len([sub for sub in self.subs if sub])
        self.mons_type = None

    def process(self):
        logger.debug('Processing rune id=%s', self.id)
        self.stats = {key: 0 for key in self.settings['SUB_WEIGHTS'].keys()}
        self.sums = {key: 0 for key in self.settings['MONS_TYPES'].keys()}
        self.sell = True
        self.grinded = False
        if self.slot in st.PERC_SLOTS:
            subs_to_check = [self.main_stat, self.sub_fixed] + self.subs
        else:
            subs_to_check = [self.sub_fixed] + self.subs
        for substat in subs_to_check:
            if len(substat) > 0:
                if '%' in substat:
                    splitted = substat.split()
                    print(self.id, splitted)
                    if '(Converted)' in splitted:
                        splitted.pop()
                        self.grinded = True
                    # if splitted[0] == 'CRI':
                    #     if splitted[1] == 'Rate':
                    #         self.stats['CR'] += int(splitted[-1][0:-1])
                    #     elif splitted[1] == 'Dmg':
                    #         self.stats['CD'] += int(splitted[-1][0:-1])
                    #     else:
                    #         logger.warning('Unknonw CRI substat %s', substat)
                    # elif splitted[0] == 'HP':
                    #     self.stats['HP'] += int(splitted[-1][0:-1])
                    # elif splitted[0] == 'ATK':
                    #     self.stats['ATK'] += int(splitted[-1][0:-1])
                    # elif splitted[0] == 'DEF':
                    #     self.stats['DEF'] += int(splitted[-1][0:-1])
                    # elif splitted[0] == 'Resistance':
                    #     self.stats['RES'] += int(splitted[-1][0:-1])
                    # elif splitted[0] == 'Accuracy':
                    #     self.stats['ACC'] += int(splitted[-1][0:-1])
                    for sub in self.settings['SUB_TRANS'].keys():
                        key = self.settings['SUB_TRANS'][sub]
                        if key in ['CD', 'CR']:
                            s = " ".join(splitted[0:2])
                        else:
                            s = splitted[0]
                        if s == sub:
                            self.stats[key] += int(splitted[-1][0:-1])
                            print(key,self.stats[key])
                    else:
                        logger.warning('Unknown substat %s', substat)
                else:
                    splitted = substat.split()
                    if '(Converted)' in splitted:
                        splitted.pop()
                        self.grinded = True
                    if splitted[0] == 'SPD':
                        self.stats['SPD'] += int(splitted[-1])
                    else:
                        logger.debug('No PERC or SPD in substat: %s', substat)
                if '->' in splitted[-2]:
                    self.grinded = True
        for rune_type in self.settings['MONS_TYPES'].keys():
            for stat in self.stats.keys():
                if stat in self.settings['MONS_TYPES'][rune_type]['SUBS'] \
                        and self.rune_set in self.settings['MONS_TYPES'][rune_type]['SETS']:
                    self.sums[rune_type] += self.settings['SUB_WEIGHTS'][stat] * self.stats[stat]
        if self.level < 15:
            self.simulate_powerup()
        logger.debug('PROCESSED RUNE ID %s, set %s', self.id, self.rune_set)
        logger.debug(self.stats)
        logger.debug(self.sums)
        self.mons_type = max(self.sums, key= self.sums.get)
        logger.debug(self.mons_type)

    def simulate_powerup(self):
        pass
        # if self.level >=12:
        #     if self.slot in st.PERC_SLOTS:
        #         splitted = self.main_stat.split()
        #         self.stats['MAIN_INC']

    def check_to_sell(self, averages):
        n_upgrades = int((15 - self.level) / 3)
        if n_upgrades > 0: n_upgrades -= 1
        logger.debug('n_upgrades %s, level %s', n_upgrades, self.level)
        if self.slot in st.PERC_SLOTS:
            slot_type = 'PERC'
        else:
            slot_type = 'FLAT'
        for rune_type in self.settings['MONS_TYPES'].keys():
            if self.sums[rune_type] + st.SUB_INCREMENT[slot_type]*n_upgrades > averages[rune_type][slot_type]:
                self.sell = False
