import csv
from src.rune import Rune
import src.settings as st
import numpy
import src.pickle_settings as ps

import logging

__author__ = 'CGT'

logger = logging.getLogger(__name__)


class RuneDatabase(object):

    settings = ps.load_settings('Custom')

    def __init__(self):
        self.rune_list = []
        self.rune_objects = []
        self.efficiency_averages = {}
        self.barion_averages = {}
        # self.settings = settings
        # logger.debug('__init__:')
        # logger.debug(self.settings)

    def runes_to_sell(self):
        return [rune for rune in self.rune_objects if rune.sell_final]

    def runes_to_keep(self):
        return [rune for rune in self.rune_objects if not rune.sell_final]

    def read_from_csv(self,csv_file):
        logger.info('Reading csv data from %s', csv_file)
        with open(csv_file) as f:
            data = list(csv.reader(f))
        self.rune_list = data[1:-3]

    def to_objects(self):
        self.rune_objects = []
        for data in self.rune_list:
            rune = Rune(data_list=data)
            self.rune_objects.append(rune)

    def process_runes(self):
        Rune.settings = ps.load_settings('Custom')
        logger.debug(Rune.settings)
        # print(Rune.settings)
        for rune in self.rune_objects:
            rune.process()

    def statistics(self):
        self.settings = ps.load_settings('Custom')
        perc_list = [rune for rune in self.rune_objects if (rune.level >= 12 and rune.slot in st.PERC_SLOTS)]
        flat_list = [rune for rune in self.rune_objects if (rune.level >= 12 and rune.slot in st.FLAT_SLOTS)]
        spd_list = [rune for rune in self.rune_objects if (rune.stats['SPD']['Value'] > 0 and rune.level >= 12 and
                                                           rune.slot not in st.SPD_SLOT)]
        # for rune_type in self.settings['MONS_TYPES'].keys():
        #     av_perc = numpy.median([rune.sums[rune_type] for rune in perc_list if rune.sums[rune_type] > 0])
        #     av_flat = numpy.median([rune.sums[rune_type] for rune in flat_list if rune.sums[rune_type] > 0])
        #     self.stat_averages[rune_type] = {'PERC': av_perc, 'FLAT': av_flat}
        #
        # av_spd = numpy.median([rune.stats['SPD']['Value'] for rune in spd_list])
        # self.stat_averages['SPD'] = av_spd
        for rune_type in self.settings['MONS_TYPES'].keys():
            # barion_av = numpy.median([rune.max_efficiency for rune in self.rune_objects])
            vpm_av_perc = numpy.median([rune.vpm_efficiency[rune_type] for rune in perc_list if
                                        rune.vpm_efficiency[rune_type] > 0])
            vpm_av_flat = numpy.median([rune.vpm_efficiency[rune_type] for rune in flat_list if
                                        rune.vpm_efficiency[rune_type] > 0])

            self.efficiency_averages[rune_type] = {'PERC': vpm_av_perc, 'FLAT': vpm_av_flat}
            barion_av_perc = numpy.median([rune.max_efficiency for rune in perc_list if
                                           rune.vpm_efficiency[rune_type] > 0])
            barion_av_flat = numpy.median([rune.max_efficiency for rune in flat_list if
                                           rune.vpm_efficiency[rune_type] > 0])
            self.barion_averages[rune_type] = {'PERC': barion_av_perc, 'FLAT': barion_av_flat}
        # logger.debug('STATISTICS DONE')
        # logger.debug(self.stat_averages)

    def check_to_sell(self):
        for rune in self.rune_objects:
            # rune.check_to_sell(self.stat_averages)
            rune.check_to_sell(self.efficiency_averages, self.barion_averages)