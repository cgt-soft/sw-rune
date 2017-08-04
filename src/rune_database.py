import csv
from src.rune import Rune
import src.mapping as mp
import src.settings as st
from preferences import default_settings
import numpy
# import src.pickle_settings as ps
import json

import logging

__author__ = 'CGT'

logger = logging.getLogger(__name__)


class RuneDatabase(object):

    # settings = ps.load_settings('Custom')

    def __init__(self, settings= default_settings):
        self.rune_list = []
        self.json_data = {}
        self.rune_objects = []
        self.efficiency_averages = {}
        self.barion_averages = {}
        self.settings = settings
        Rune.settings = settings
        # logger.debug('__init__:')
        # logger.debug(self.settings)

    def read_from_json(self,json_file):
        logger.info('Reading json data from %s', json_file)
        with open(json_file) as f:
            self.json_data = json.load(f)
            self.parse_json()

    def parse_json(self):
        self.rune_objects = []
        count = 1
        # Unequiped runes
        for json_rune in self.json_data['runes']:
            rune = Rune()
            rune.id = count
            rune.map_json_rune(json_rune)
            self.rune_objects.append(rune)
            count += 1
        # Equipped runes
        for monster in self.json_data['unit_list']:
            monster_name = mp.get_monster_name(monster['unit_master_id'])
            for json_rune in monster['runes']:
                rune = Rune()
                rune.id = count
                rune.map_json_rune(json_rune, monster_name)
                self.rune_objects.append(rune)
                count += 1

    def read_from_csv(self,csv_file):
        logger.info('Reading csv data from %s', csv_file)
        with open(csv_file) as f:
            data = list(csv.reader(f))
        self.rune_list = data[1:-3]
        self.rune_objects = []
        for data in self.rune_list:
            rune = Rune(data_list=data)
            self.rune_objects.append(rune)

    def process_runes(self):
        # Rune.settings = ps.load_settings('Custom')
        logger.debug(Rune.settings)
        # print(Rune.settings)
        for rune in self.rune_objects:
            rune.process()

    def statistics(self):
        perc_list = [rune for rune in self.rune_objects if (rune.level >= 12 and rune.slot in [2, 4, 6])]
        flat_list = [rune for rune in self.rune_objects if (rune.level >= 12 and rune.slot in [1, 3, 5])]
        # spd_list = [rune for rune in self.rune_objects if (rune.stats['SPD']['Value'] > 0 and rune.level >= 12 and
        #                                                    rune.slot not in [2])]
        for rune_type in self.settings['monster_types'].keys():
            vpm_av_perc = numpy.median([rune.vpm_efficiency[rune_type] for rune in perc_list if
                                        rune.vpm_efficiency[rune_type] > 0])
            vpm_av_flat = numpy.median([rune.vpm_efficiency[rune_type] for rune in flat_list if
                                        rune.vpm_efficiency[rune_type] > 0])

            self.efficiency_averages[rune_type] = {'PERC': vpm_av_perc, 'FLAT': vpm_av_flat}
            barion_av_perc = numpy.median([rune.barion_efficiency for rune in perc_list if
                                           rune.vpm_efficiency[rune_type] > 0])
            barion_av_flat = numpy.median([rune.barion_efficiency for rune in flat_list if
                                           rune.vpm_efficiency[rune_type] > 0])
            self.barion_averages[rune_type] = {'PERC': barion_av_perc, 'FLAT': barion_av_flat}

    def check_to_sell(self):
        for rune in self.rune_objects:
            rune.check_to_sell(self.efficiency_averages, self.barion_averages)

    def runes_to_sell(self):
        return [rune for rune in self.rune_objects if rune.status == 'Sell']

    def runes_to_check(self):
        return [rune for rune in self.rune_objects if rune.status == 'Check']

    def runes_to_keep(self):
        return [rune for rune in self.rune_objects if rune.status == 'Keep']