from src.rune_database import RuneDatabase
from src.plots import Plots


def main():
    rdb = RuneDatabase()
    rdb.read_from_csv('2100324-runes.csv')
    rdb.to_objects()
    rdb.statistics()
    rdb.check_to_sell()
    runes_to_sell =[rune for rune in rdb.rune_objects if rune.sell]
    runes_leveled = [rune for rune in rdb.rune_objects if rune.level >= 12]
    print(len(runes_to_sell), len(runes_leveled))
    vio_to_sell = [rune for rune in runes_to_sell if rune.rune_set == 'Violent']
    for rune in runes_to_sell:
        print(rune.id, rune.equipped, rune.slot, rune.rune_set, rune.level, rune.main_stat, rune.sub_fixed,
              rune.sub_1, rune.sub_2, rune.sub_3, rune.sub_4,
              rune.atk_sum, rune.sup_sum)
    plot = Plots(rdb.rune_objects)
    plot.efficiency_histogram('Violent')

if __name__ == '__main__':
    import logging.config
    logging.basicConfig(filename="test.log", filemode='w', level=logging.DEBUG)
    main()


