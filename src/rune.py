__author__ = 'CGT'

class Rune(object):

    def __init__(self,data_list=None):
        self.id = data_list[0]
        self.equipped = data_list[1]
        self.rune_set = data_list[2]
        self.slot = int(data_list[3])
        self.stars = int(data_list[4])
        self.level = int(data_list[5])
        self.price = data_list[6]
        self.main_stat = data_list[7]
        self.sub_fixed = data_list[8]
        self.sub_1 = data_list[9]
        self.sub_2 = data_list[10]
        self.sub_3 = data_list[11]
        self.sub_4 = data_list[12]
        self.current_efficiency = data_list[13]
        self.max_efficiency = data_list[14]

    def process(self):
        pass