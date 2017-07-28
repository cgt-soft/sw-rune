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
        self.max_efficiency = float(data_list[14].replace(' %', ''))
        self.stats = {key: {'Value': 0, 'Grinded': False} for key in self.settings['SUB_WEIGHTS'].keys()}
        if self.level == 15:
            self.max_stats = self.stats
        else:
            self.max_stats = {key: {'MIN': 0, 'MAX': 0} for key in self.settings['SUB_WEIGHTS'].keys()}
        self.converted = False
        self.sums = {key: 0 for key in self.settings['MONS_TYPES'].keys()}
        self.sell = True
        self.n_subs = len([sub for sub in self.subs if sub])
        self.mons_type = None
        self.vpm_efficiency = {key: 0.0 for key in self.settings['MONS_TYPES'].keys()}

    def get_stat(self, stat):
        [key, val, grinded, perc] = [None, None, None, None]
        logger.debug('get_stat: %s',stat)
        if len(stat) > 0:
            grinded = False
            if '%' in stat:
                perc = True
            else:
                perc = False
            splitted = stat.split()
            if splitted[0] == 'CRI':
                s = " ".join(splitted[0:2])
            else:
                s = splitted[0]
            if splitted[-1] == '(Converted)':
                val = int(splitted[-2].replace('%', ''))
            else:
                val = int(splitted[-1].replace('%', ''))
            key = self.settings['SUB_TRANS'][s]
            if '->' in splitted[-2]:
                grinded = True
        logger.debug('key = %s, val = %s, grinded = %s, perc = %s', key, val, grinded, perc)
        return [key, val, grinded, perc]

    def check_converted(self):
        for stat in self.subs:
            if '(Converted)' in stat:
                self.converted = True

    def process(self):
        logger.debug('Processing rune id=%s', self.id)
        self.check_converted()
        logger.debug('Converted = %s', self.converted)
        subs_to_check = [self.sub_fixed] + self.subs
        for substat in subs_to_check:
            if len(substat) > 0:
                key, val, grinded, perc = self.get_stat(substat)
                self.stats[key]['Grinded'] = grinded
                if perc:
                    self.stats[key]['Value'] += val
                else:
                    if key == 'SPD':
                        self.stats[key]['Value'] += val
                    else:
                        self.stats[key]['Value'] += val / self.settings['AV_BASE_STATS'][key] * 100
        logger.debug('stats = %s', self.stats)
        main_stat, _, _, perc = self.get_stat(self.main_stat)
        for rune_type in self.settings['MONS_TYPES'].keys():
            # Calculate VPM efficiency
            for stat in self.stats.keys():
                logger.debug('set: %s, type: %s, stat: %s, main: %s',self.rune_set, rune_type, stat, main_stat)
                # if stat in self.settings['MONS_TYPES'][rune_type]['SUBS'] and self.rune_set in self.settings['MONS_TYPES'][rune_type]['SETS'] and main_stat in self.settings['MONS_TYPES'][rune_type]['SUBS']:
                if stat in self.settings['MONS_TYPES'][rune_type]['SUBS'] and \
                                self.rune_set in self.settings['MONS_TYPES'][rune_type]['SETS'] and \
                                ((self.slot in st.PERC_SLOTS and main_stat in self.settings['MONS_TYPES'][rune_type]['SUBS']) or
                                self.slot not in st.PERC_SLOTS):
                    self.vpm_efficiency[rune_type] += self.settings['SUB_WEIGHTS'][stat] * \
                                                      self.stats[stat]['Value'] / \
                                                      self.settings['MAX_VALUE'][stat]
                    logger.debug(self.vpm_efficiency[rune_type])
                else:
                    logger.debug('Rune is not suitable for %s', rune_type)

            # Stars compensation
            if self.stars <= 5:
                if perc:
                    self.vpm_efficiency[rune_type] -= self.settings['SUB_WEIGHTS'][main_stat] * \
                                                      self.settings['STAT_COMP']['PERC'][main_stat] / \
                                                      self.settings['MAX_VALUE'][main_stat]
                else:
                    if key == 'SPD':
                        self.vpm_efficiency[rune_type] -= self.settings['SUB_WEIGHTS'][main_stat] * \
                                                          self.settings['STAT_COMP']['FLAT'][main_stat] / \
                                                          self.settings['MAX_VALUE'][main_stat]
                    else:
                        self.vpm_efficiency[rune_type] -= self.settings['SUB_WEIGHTS'][main_stat] * \
                                                          self.settings['STAT_COMP']['FLAT'][main_stat] /\
                                                          self.settings['AV_BASE_STATS'][main_stat] * 100 / \
                                                          self.settings['MAX_VALUE'][main_stat]
            # Level compensation
            if self.level < 12:
                self.vpm_efficiency[rune_type] += self.settings['LEVEL_COMP'][self.level] / 100
        # for rune_type in self.settings['MONS_TYPES'].keys():
        #     for stat in self.stats.keys():
        #         if stat in self.settings['MONS_TYPES'][rune_type]['SUBS'] \
        #                 and self.rune_set in self.settings['MONS_TYPES'][rune_type]['SETS']:
        #             self.sums[rune_type] += self.settings['SUB_WEIGHTS'][stat] * self.stats[stat]['Value']
        # if self.level < 15:
        #     self.simulate_powerup()
        logger.debug('PROCESSED RUNE ID %s, set %s', self.id, self.rune_set)
        logger.debug(self.vpm_efficiency)
        # logger.debug(self.sums)
        # self.mons_type = max(self.sums, key= self.sums.get)
        efficiencies = {x: self.vpm_efficiency[x] for x in self.vpm_efficiency if x != 'TOTAL'}
        self.mons_type = max(efficiencies, key= efficiencies.get)

        logger.debug(self.mons_type)

    def simulate_powerup(self):
        pass
        # if self.level >=12:
        #     if self.slot in st.PERC_SLOTS:
        #         splitted = self.main_stat.split()
        #         self.stats['MAIN_INC']

    def check_to_sell(self, averages):
        # n_upgrades = int((15 - self.level) / 3)
        # if n_upgrades > 0: n_upgrades -= 1
        # logger.debug('n_upgrades %s, level %s', n_upgrades, self.level)
        if self.slot in st.PERC_SLOTS:
            slot_type = 'PERC'
        else:
            slot_type = 'FLAT'
        # for rune_type in self.settings['MONS_TYPES'].keys():
        #     if self.sums[rune_type] + st.SUB_INCREMENT[slot_type]*n_upgrades > averages[rune_type][slot_type]:
        #         self.sell = False
        for rune_type in self.settings['MONS_TYPES'].keys():
            if self.vpm_efficiency[rune_type] > averages[rune_type][slot_type]:
                self.sell = False
