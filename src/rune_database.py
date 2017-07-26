import csv
from src.rune import Rune
import src.settings as st
import numpy
import src.pickle_settings as ps

import logging

__author__ = 'CGT'

logger = logging.getLogger(__name__)

settings = ps.load_settings('Custom')

class RuneDatabase(object):

    def __init__(self):
        self.rune_list = []
        self.rune_objects = []
        self.stat_averages = {}
        # self.settings = settings
        # logger.debug('__init__:')
        # logger.debug(self.settings)

    def runes_to_sell(self):
        return [rune for rune in self.rune_objects if rune.sell]

    def runes_to_keep(self):
        return [rune for rune in self.rune_objects if not rune.sell]

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
        perc_list = [rune for rune in self.rune_objects if (rune.level >= 12 and rune.slot in st.PERC_SLOTS)]

        # logger.debug('length perc list = %s \n %s\n', len(perc_list),
        #              [[rune.id, rune.sup_sum, rune.atk_sum] for rune in perc_list])

        flat_list = [rune for rune in self.rune_objects if (rune.level >= 12 and rune.slot in st.FLAT_SLOTS)]

        # logger.debug('length flat list = %s \n %s\n', len(flat_list),
        #              [[rune.id, rune.sup_sum, rune.atk_sum] for rune in flat_list])

        spd_list = [rune for rune in self.rune_objects if (rune.stats['SPD'] > 0 and rune.level >= 12 and
                                                           rune.slot not in st.SPD_SLOT)]
        # logger.debug('length spd list = %s \n %s\n', len(spd_list),[[rune.id, rune.spd] for rune in spd_list])

        # av_atk_perc = numpy.median([rune.atk_sum for rune in perc_list])
        # av_atk_flat = numpy.median([rune.atk_sum for rune in flat_list])
        # av_sup_perc = numpy.median([rune.sup_sum for rune in perc_list])
        # av_sup_flat = numpy.median([rune.sup_sum for rune in flat_list])
        # av_spd = numpy.median([rune.spd for rune in spd_list])

        for rune_type in st.TYPES.keys():
            av_perc = numpy.median([rune.sums[rune_type] for rune in perc_list if rune.sums[rune_type] > 0])
            av_flat = numpy.median([rune.sums[rune_type] for rune in flat_list if rune.sums[rune_type] > 0])
            self.stat_averages[rune_type] = {'PERC': av_perc, 'FLAT': av_flat}

        av_spd = numpy.median([rune.stats['SPD'] for rune in spd_list])
        self.stat_averages['SPD'] = av_spd

        logger.debug('STATISTICS DONE')
        logger.debug(self.stat_averages)

    def check_to_sell(self):
        for rune in self.rune_objects:
            rune.check_to_sell(self.stat_averages)