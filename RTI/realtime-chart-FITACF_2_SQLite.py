# Author: Danno Peters, Danno@dannopeters.ca
# Language Python 2.7
# Purpose: Upkeeps an SQLite database of SuperDARN Chart Data
# Input: JFITACF files from RADARs
# Output: Populated SQLite Database


#Functions


#import required libaraies
import sqlite3 #allows for interation with SQLite databases
import sys
import os


# Variables
db_name = 'SuperDARN RealTimeChart.sql' #set name of SQLite database to be found or created
#db_schema = 
dataSpan = 1 #length of time to store data (Hours)
connection = sqlite3.connect(db_name)

def check_db(db_name):
    if exists_db(db_name):
        cursor = connection.cursor()
        db_tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        for table in db_tables:
            print(table)
    else:
        print('Message: ', db_name, ' Does Not Exist')


#exists_db: checks if a database currently exists
    #Input: db_name - name of the database ie 'realtime-charts.sqlite'
    #Output: exists - bool, True if database exists, False if it does not
def exists_db(db_name):
    exists = os.path.exists(db_name)
    return exists


if exists_db(db_name):
    print('Message: ', db_name, ' Exists')
    check_db(db_name)
else:
    print('Message: ', db_name, ' Does Not Exist')

connection.close()

#create_db: creates a SQLite database with user defined name and schema
#   Input:  db_name - name of the database ie 'realtime-charts.sqlite'
#           db_schema - expected databse schema ***need to decide on format***
#   Output: 
#def create_db(db_name, db_schema):
    

#check_db: compares current database structure to expected schema
#   Input:  db_name - name of the database ie 'realtime-charts.sqlite'
#           db_schema - expected databse schema ***need to decide on format***
#   Output:
