import matplotlib.pyplot as plt
import src.settings as st
import collections
import numpy

__author__ = 'CGT'


class Plots(object):

    def __init__(self, rune_objects):
        self.data = rune_objects

    def level_histogram(self):
        x = []
        for rune_set in st.RUNE_SETS:
            x.append([rune.level for rune in self.data if rune.rune_set==rune_set])
        n_bins = 5
        colors = ['red', 'tan', 'lime', 'cyan', 'yellow',
                  'orange', 'blue', 'pink', 'green', 'navy',
                  'maroon', 'teal', 'silver', 'purple', 'steelblue', 'olive']
        plt.hist(x, n_bins, histtype='bar', color=colors, label=st.RUNE_SETS)
        plt.legend(prop={'size': 10})
        plt.show()

    def set_pie(self):
        sizes = []
        count = collections.Counter([rune.rune_set for rune in self.data])
        for rune_set in st.RUNE_SETS:
            sizes.append(count[rune_set])
        plt.pie(sizes, labels=st.RUNE_SETS, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        plt.show()

    def efficiency_histogram(self, rune_set):
        runes = [rune for rune in self.data if rune.rune_set == rune_set]
        x = [[rune.atk_sum for rune in runes if rune.slot in st.PERC_SLOTS]]
        plt.hist(x, normed = True, bins= range(int(numpy.amin(x)), int(numpy.amax(x)), 10))
        plt.legend(prop={'size': 10})
        plt.show()