from src.rune_database import RuneDatabase


def main():
    rdb = RuneDatabase()
    rdb.read_from_csv('2100324-runes.csv')
    rdb.to_objects()
    print(rdb.rune_objects[0].id)

if __name__ == '__main__':
    import logging.config
    logging.basicConfig(filename="test.log",level=logging.DEBUG)
    main()


