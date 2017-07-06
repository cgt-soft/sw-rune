import csv
from src.rune import Rune

import logging

__author__ = 'CGT'

logger = logging.getLogger(__name__)

class Rune_database(object):

    def __init__(self):
        self.rune_list = []
        self.rune_objects = []

    def read_from_csv(self,csv_file):
        logger.info('Reading csv data from %s',csv_file)
        with open(csv_file) as f:
            data = list(csv.reader(f))
        self.rune_list = data[1:-3]

    def to_objects(self):
        logger.info('Converting rune data to objects')
        for data in self.rune_list:
            rune = Rune(data)
            rune.process()
            self.rune_objects.append(rune)