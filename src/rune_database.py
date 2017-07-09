import csv
from src.rune import Rune
import src.settings as st
import numpy

import logging

__author__ = 'CGT'

logger = logging.getLogger(__name__)


class RuneDatabase(object):

    def __init__(self):
        self.rune_list = []
        self.rune_objects = []
        self.stat_averages = {}

    def read_from_csv(self,csv_file):
        logger.info('Reading csv data from %s', csv_file)
        with open(csv_file) as f:
            data = list(csv.reader(f))
        self.rune_list = data[1:-3]

    def to_objects(self):
        logger.info('Converting rune data to objects')
        for data in self.rune_list:
            rune = Rune(data)
            rune.process()
            self.rune_objects.append(rune)

    def statistics(self):
        for rune_set in st.RUNE_SETS:
            logger.debug('\n\n*****STATISTICS for set %s\n', rune_set)
            perc_list = [rune for rune in self.rune_objects if (
                rune.rune_set == rune_set and rune.level >= 12 and rune.slot in st.PERC_SLOTS)]

            logger.debug('length perc list = %s \n %s\n', len(perc_list),
                         [[rune.id, rune.sup_sum, rune.atk_sum] for rune in perc_list])

            flat_list = [rune for rune in self.rune_objects if (
                rune.rune_set == rune_set and rune.level >= 12 and rune.slot in st.FLAT_SLOTS)]

            logger.debug('length flat list = %s \n %s\n', len(flat_list),
                         [[rune.id, rune.sup_sum, rune.atk_sum] for rune in flat_list])

            spd_list = [rune for rune in self.rune_objects if (
                rune.spd > 0 and rune.rune_set == rune_set and rune.level >= 12 and rune.slot not in st.SPD_SLOT)]
            logger.debug('length spd list = %s \n %s\n', len(spd_list),[[rune.id, rune.spd] for rune in spd_list])

            av_atk_perc = numpy.mean([rune.atk_sum for rune in perc_list])
            av_atk_flat = numpy.mean([rune.atk_sum for rune in flat_list])
            av_sup_perc = numpy.mean([rune.sup_sum for rune in perc_list])
            av_sup_flat = numpy.mean([rune.sup_sum for rune in flat_list])
            av_spd = numpy.mean([rune.spd for rune in spd_list])

            logger.debug('\nav_atk_perc, av_atk_flat, av_sup_perc, av_sup_flat, av_spd\n %s %s %s %s %s',
                         av_atk_perc, av_atk_flat, av_sup_perc, av_sup_flat, av_spd)

            self.stat_averages[rune_set] = {'ATK' : {'PERC' : av_atk_perc, 'FLAT': av_atk_flat},
                                            'SUP' : {'PERC' : av_sup_perc, 'FLAT': av_sup_flat},
                                            'SPD' : av_spd}

    def check_to_sell(self):
        for rune in self.rune_objects:
            rune.check_to_sell(self.stat_averages)