from src.rune_database import Rune_database

rdb = Rune_database()
rdb.read_from_csv('2100324-runes.csv')
rdb.to_objects()
print(rdb.rune_objects[0].id)