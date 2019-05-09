# Author: Danno Peters, Danno@dannopeters.ca
# Language Python 2.7
# Purpose: Upkeeps an SQLite database of SuperDARN Chart Data
# Input: JSON files from RADARs
# Output: Populated SQLite Database

#import required libaraies
import sqlite3 #allows for interation with SQLite databases
import sys
import os
import pathlib
import asyncio #used for asynchronous communication (WSS)
import socket #used to connect to chapman server websockets

# Variables
	db_name = 'realtime-charts.sqlite' #set name of SQLite database to be found or created
	sqlPath = PurePath('') #set path to SQLite Database
	dataSpan = 1 #length of time to store data (Hours)

#Check if database exists, if not, create it (easy in python 3.4+)
db_exists = not os.path.exists(db_name)
connection = sqlite3.connect(db_name)

if db_exists:
    print('No schema exists.')
else:
    print('DB exists.')

connection.close()