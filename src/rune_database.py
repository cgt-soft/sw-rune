import csv
from src.rune import Rune

__author__ = 'CGT'

class Rune_database(object):

    def __init__(self):
        self.rune_list = []
        self.rune_objects = []

    def read_from_csv(self,csv_file):
        with open(csv_file) as f:
            data = list(csv.reader(f))
        self.rune_list = data[1:-3]

    def to_objects(self):
        for data in self.rune_list:
            rune = Rune(data)
            rune.process()
            self.rune_objects.append(rune)