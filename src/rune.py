import logging
import src.settings as st
from preferences import default_settings
import src.mapping as mp


__author__ = 'CGT'

logger = logging.getLogger(__name__)


class Rune(object):
    # settings = ps.load_settings('Custom')
    # print(settings)
    settings = default_settings

    def __init__(self, data_list = None):
        # logger.debug('Initialize rune, id = %s', data_list[0])
        self.id = data_list[0] if data_list else None
        self.equipped = data_list[1] if data_list else None
        self.rune_set = data_list[2] if data_list else None
        self.slot = int(data_list[3]) if data_list else None
        self.stars = int(data_list[4]) if data_list else None
        self.level = int(data_list[5]) if data_list else None
        self.price = data_list[6] if data_list else None
        self.main_stat = data_list[7] if data_list else None
        self.sub_fixed = data_list[8] if data_list else None
        self.subs = data_list[9:13] if data_list else []
        self.current_efficiency = float(data_list[13].replace(' %', '')) if data_list else None
        self.max_efficiency = float(data_list[14].replace(' %', '')) if data_list else None
        self.barion_efficiency = float(data_list[15].replace(' %', '')) if data_list else None
        self.original_quality = 'Unknown' if data_list else None
        self.stats = {key: {'Value': 0, 'Grinded': False} for key in self.settings['substat_weights'].keys()}
        if self.level == 15:
            self.max_stats = self.stats
        else:
            self.max_stats = {key: {'MIN': 0, 'MAX': 0} for key in self.settings['substat_weights'].keys()}
        self.converted = False
        self.sums = {key: 0 for key in self.settings['monster_types'].keys()}
        self.sell = {'VPM': True, 'Barion': True}
        self.sell_final = True
        self.n_subs = len([sub for sub in self.subs if sub])
        self.mons_type = None
        self.vpm_efficiency = {key: 0.0 for key in self.settings['monster_types'].keys()}
        self.status = 'Sell'

    def map_json_rune(self, json_rune, monster=None):
        if monster:
            self.equipped = monster
        else:
            self.equipped = '0'
            # Set
        self.rune_set = mp.exports['rune']['sets'][json_rune['set_id']]
        # Slot
        self.slot = json_rune['slot_no']
        # Stars??
        self.stars = json_rune['class']
        # level
        self.level = json_rune['upgrade_curr']
        # Sell price
        self.price = json_rune['sell_value']
        # Pimary effect = Main stat
        self.main_stat = mp.get_rune_effect(json_rune['pri_eff'])
        # Fixed effect
        self.sub_fixed = mp.get_rune_effect(json_rune['prefix_eff'])
        # Substats
        self.n_subs = 0
        for eff in json_rune['sec_eff']:
            self.subs.append(mp.get_rune_effect(eff))
            self.n_subs += 1
        for i in range(self.n_subs,4):
            self.subs.append('')
        # Potentials
        efficiencies = mp.get_rune_efficiency(json_rune)
        self.current_efficiency = float("{0:.2f}".format(efficiencies['current']))
        self.max_efficiency = float("{0:.2f}".format(efficiencies['max']))
        # Barion efficiency
        self.barion_efficiency = float("{0:.2f}".format(100*mp.barion_rune_efficiency(json_rune)))
        # Original quality (Legend, hero, etc)
        self.original_quality = mp.exports['rune']['quality'][json_rune['rank']]
        log = [self.equipped, self.rune_set, self.slot, self.stars, self.level, self.main_stat, self.sub_fixed,
                     self.subs[0], self.subs[1], self.subs[2], self.subs[3], self.barion_efficiency]
        logger.debug(log)


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
            key = self.settings['sub_trans'][s]
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
        self.stats = {key: {'Value': 0, 'Grinded': False} for key in self.settings['substat_weights'].keys()}
        self.vpm_efficiency = {key: 0.0 for key in self.settings['monster_types'].keys()}
        self.mons_type = None
        self.sell = {'VPM': True, 'Barion': True}
        self.converted = False
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
                        self.stats[key]['Value'] += val / self.settings['average_base_stats'][key] * 100
        logger.debug('stats = %s', self.stats)
        main_stat, _, _, perc = self.get_stat(self.main_stat)
        for rune_type in self.settings['monster_types'].keys():
            # Calculate VPM efficiency
            for stat in self.stats.keys():
                logger.debug('set: %s, type: %s, stat: %s, main: %s',self.rune_set, rune_type, stat, main_stat)
                # if stat in self.settings['MONS_TYPES'][rune_type]['SUBS'] and self.rune_set in self.settings['MONS_TYPES'][rune_type]['SETS'] and main_stat in self.settings['MONS_TYPES'][rune_type]['SUBS']:
                if stat in self.settings['monster_types'][rune_type]['SUBS'] and \
                                self.rune_set in self.settings['monster_types'][rune_type]['SETS'] and \
                                ((self.slot in st.PERC_SLOTS and main_stat in self.settings['monster_types'][rune_type]['SUBS']) or
                                self.slot not in st.PERC_SLOTS):
                    self.vpm_efficiency[rune_type] += self.settings['substat_weights'][stat] * \
                                                      self.stats[stat]['Value'] / \
                                                      self.settings['max_value'][stat]
                    logger.debug(self.vpm_efficiency[rune_type])
                else:
                    logger.debug('Rune is not suitable for %s', rune_type)

            # Stars compensation
            if self.stars <= 5:
                if perc:
                    self.vpm_efficiency[rune_type] -= self.settings['substat_weights'][main_stat] * \
                                                      self.settings['stat_compensation']['PERC'][main_stat] / \
                                                      self.settings['max_value'][main_stat]
                else:
                    if key == 'SPD':
                        self.vpm_efficiency[rune_type] -= self.settings['substat_weights'][main_stat] * \
                                                          self.settings['stat_compensation']['FLAT'][main_stat] / \
                                                          self.settings['max_value'][main_stat]
                    else:
                        self.vpm_efficiency[rune_type] -= self.settings['substat_weights'][main_stat] * \
                                                          self.settings['stat_compensation']['FLAT'][main_stat] /\
                                                          self.settings['average_base_stats'][main_stat] * 100 / \
                                                          self.settings['max_value'][main_stat]
            # Level compensation
            if self.level < 12:
                self.vpm_efficiency[rune_type] += self.settings['level_compensation'][self.level] / 100
            self.vpm_efficiency[rune_type] = 100*self.vpm_efficiency[rune_type]
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

    def check_to_sell(self, vpm_averages, barion_averages):
        self.sell = {'VPM': True, 'Barion': True}
        self.sell_final = True
        if self.slot in st.PERC_SLOTS:
            slot_type = 'PERC'
        else:
            slot_type = 'FLAT'
        # for rune_type in self.settings['MONS_TYPES'].keys():
        #     if self.sums[rune_type] + st.SUB_INCREMENT[slot_type]*n_upgrades > averages[rune_type][slot_type]:
        #         self.sell = False
        for rune_type in self.settings['monster_types'].keys():
            if self.vpm_efficiency[rune_type] > vpm_averages[rune_type][slot_type]:
                self.sell['VPM'] = False
            if self.barion_efficiency > barion_averages[rune_type][slot_type]:
                self.sell['Barion'] = False

        self.sell_final = self.sell['VPM'] or self.sell['Barion']

        if self.sell['VPM'] and self.sell['Barion']:
            self.status = 'Sell'
        elif self.sell['VPM'] or self.sell['Barion']:
            self.status = 'Check'
        else:
            self.status = 'Keep'