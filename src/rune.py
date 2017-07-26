import logging
import src.settings as st
import src.pickle_settings as ps


__author__ = 'CGT'

logger = logging.getLogger(__name__)


class Rune(object):
    settings = ps.load_settings('Custom')
    # print(settings)

    def __init__(self, data_list=None):
        if data_list is None:
            logger.warning('Initializing rune with None type data_list')
        else:
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
            # self.sub_1 = data_list[9]
            # self.sub_2 = data_list[10]
            # self.sub_3 = data_list[11]
            # self.sub_4 = data_list[12]
            self.subs = data_list[9:13]
            self.current_efficiency = data_list[13]
            self.max_efficiency = data_list[14]
        # self.stats = {'HP' : 0, 'CR' : 0, 'CD' : 0, 'ATK' : 0, 'ACC': 0, 'RES' : 0, 'SPD': 0, 'DEF': 0}
        # self.stats = {key: 0 for key in st.SUB_WEIGHTS.keys()}
        self.stats = {key: 0 for key in self.settings.keys()}
        self.grinded = False
        self.sums = {key: 0 for key in st.TYPES.keys()}
        self.sell = True
        self.n_subs = len([sub for sub in self.subs if sub])
        self.mons_type = None

    def process(self):
        logger.debug('Processing rune id=%s', self.id)
        # print(self.settings)
        self.stats = {key: 0 for key in self.settings.keys()}
        self.sums = {key: 0 for key in st.TYPES.keys()}
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
                    if '(Converted)' in splitted:
                        splitted.pop()
                        self.grinded = True
                    if splitted[0] == 'CRI':
                        if splitted[1] == 'Rate':
                            # self.cr += int(splitted[-1][0:-1])
                            self.stats['CR'] += int(splitted[-1][0:-1])
                        elif splitted[1] == 'Dmg':
                            # self.cd += int(splitted[-1][0:-1])
                            self.stats['CD'] += int(splitted[-1][0:-1])
                        else:
                            logger.warning('Unknonw CRI substat %s', substat)
                    elif splitted[0] == 'HP':
                        # self.hp += int(splitted[-1][0:-1])
                        self.stats['HP'] += int(splitted[-1][0:-1])
                    elif splitted[0] == 'ATK':
                        # self.atk += int(splitted[-1][0:-1])
                        self.stats['ATK'] += int(splitted[-1][0:-1])
                    elif splitted[0] == 'DEF':
                        # self.df += int(splitted[-1][0:-1])
                        self.stats['DEF'] += int(splitted[-1][0:-1])
                    elif splitted[0] == 'Resistance':
                        # self.res += int(splitted[-1][0:-1])
                        self.stats['RES'] += int(splitted[-1][0:-1])
                    elif splitted[0] == 'Accuracy':
                        # self.acc += int(splitted[-1][0:-1])
                        self.stats['ACC'] += int(splitted[-1][0:-1])
                    else:
                        logger.warning('Unknown substat %s', substat)
                else:
                    splitted = substat.split()
                    if '(Converted)' in splitted:
                        splitted.pop()
                        self.grinded = True
                    if splitted[0] == 'SPD':
                        # self.spd += int(splitted[-1])
                        self.stats['SPD'] = self.stats['SPD'] + int(splitted[-1])
                    else:
                        logger.debug('No PERC or SPD in substat: %s', substat)
                if '->' in splitted[-2]:
                    self.grinded = True
        # self.atk_sum =  st.SUB_WEIGHTS['ATK']*self.atk + \
        #                 st.SUB_WEIGHTS['CR'] *self.cr + \
        #                 st.SUB_WEIGHTS['CD'] *self.cd + \
        #                 st.SUB_WEIGHTS['SPD'] *self.spd + \
        #                 st.SUB_WEIGHTS['RES'] *self.res + \
        #                 st.SUB_WEIGHTS['ACC'] *self.acc
        # self.sup_sum =  st.SUB_WEIGHTS['HP']*self.hp + \
        #                 st.SUB_WEIGHTS['DEF'] *self.df + \
        #                 st.SUB_WEIGHTS['SPD'] * self.spd + \
        #                 st.SUB_WEIGHTS['RES'] * self.res + \
        #                 st.SUB_WEIGHTS['ACC'] * self.acc
        # logger.debug('PROCESSED RUNE \n ID  SUP_SUM ATK_SUM \n %s %s %s', self.id, self.sup_sum, self.atk_sum)
        for rune_type in st.TYPES.keys():
            for stat in self.stats.keys():
                if stat in st.TYPES[rune_type]['SUBS'] and self.rune_set in st.TYPES[rune_type]['SETS']:
                    self.sums[rune_type] += self.settings[stat] * self.stats[stat]
                    # self.sums[rune_type] += self.settings[stat] * self.stats[stat]
        logger.debug('PROCESSED RUNE ID %s, set %s', self.id, self.rune_set)
        logger.debug(self.stats)
        logger.debug(self.sums)
        self.mons_type = max(self.sums, key= self.sums.get)
        logger.debug(self.mons_type)
        print(self.id, self.sums)

    def check_to_sell(self, averages):
        n_upgrades = int((15 - self.level) / 3)
        if n_upgrades > 0: n_upgrades -= 1
        logger.debug('n_upgrades %s, level %s', n_upgrades, self.level)
        if self.slot in st.PERC_SLOTS:
            slot_type = 'PERC'
        else:
            slot_type = 'FLAT'
        for rune_type in st.TYPES.keys():
            if self.sums[rune_type] + st.SUB_INCREMENT[slot_type]*n_upgrades > averages[rune_type][slot_type]:
                self.sell = False

        # if self.slot in st.PERC_SLOTS:
        #     slot_type = 'PERC'
        # else:
        #     slot_type = 'FLAT'
        # n_upgrades = int((15 - self.level) / 3)
        # if n_upgrades > 0: n_upgrades -= 1
        # if self.atk_sum + st.SUB_INCREMENT[slot_type]*n_upgrades > averages[self.rune_set]['ATK'][slot_type] \
        #         or self.sup_sum + st.SUB_INCREMENT[slot_type]*n_upgrades > averages[self.rune_set]['SUP'][slot_type] \
        #         or self.spd + st.SUB_INCREMENT[slot_type]*n_upgrades > averages[self.rune_set]['SPD']:
        #     logger.debug('RUNE TO KEEP id: %s \n %s\n',self.id,
        #                  [self.main_stat,self.sub_fixed, self.sub_1, self.sub_2, self.sub_3, self.sub_4])
        # else:
        #     logger.debug('RUNE TO SELL id: %s \n %s\n', self.id,
        #                  [self.main_stat, self.sub_fixed, self.sub_1, self.sub_2, self.sub_3, self.sub_4])
        #     self.sell = True