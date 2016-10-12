#Tushar Borole
#Python 2.7

import sqlite3
import json
with open('config.json') as data_file:
    config = json.load(data_file)

conn=sqlite3.connect(config['database'], check_same_thread=False)
conn.execute('pragma foreign_keys=ON')



def dict_factory(cursor, row):
    """This is an function use to fonmat the json when retirve from the  myswl database"""
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


conn.row_factory = dict_factory

