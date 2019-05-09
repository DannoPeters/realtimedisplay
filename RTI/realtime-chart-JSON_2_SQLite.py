# Author: Danno Peters, Danno@dannopeters.ca
# Language Python 2.7
# Purpose: Upkeeps an SQLite database of SuperDARN Chart Data
# Input: JSON files from RADARs
# Output: Populated SQLite Database

#import required libaraies
import sqlite #allows for interation with SQLite databases
import sys
import pathlib
import asyncio #used for asynchronous communication (WSS)
import socket #used to connect to chapman server websockets

# Variables
	database = 'realtime-charts.sqlite' #set name of SQLite database to be found or created
	sqlPath = PurePath('') #set path to SQLite Database
	dataSpan = 1 #length of time to store data (Hours)

	radars = {"saskatoon": {
                        "name": "Saskatoon",
                        "maxBeams": 16,                            
                        "maxRangeGates": 75,
                        "address" : 'wss://chapman.usask.ca:5100',
                        "port" : 5100
                        },

             "rankin": {
                        "name": "Rankin Inlet",
                        "maxBeams": 16,
                        "maxRangeGates": 100, 
                        "address" : 'wss://chapman.usask.ca:5101',
                        "port" : 5101
                        },

             "princegeorge": {
                        "name": "Prince George",
                        "maxBeams": 16,
                        "maxRangeGates": 75,
                        "address" : "wss://chapman.usask.ca:5102",
                        "port" : 5102
                        },

             "clyde": {
                        "name": "Clyde River",
                        "maxBeams": 16,
                        "maxRangeGates": 66,
                        "address" : "wss://chapman.usask.ca:5103",
                        "port" : 5103
                        },

             "inuvik": {
                        "name": "Inuvik",
                        "maxBeams": 16,
                        "maxRangeGates": 100,
                        "address" : "wss://chapman.usask.ca:5104",
                        "port" : 5104
                        },

             "blackstone": {
                        "name": "Blackstone",
                        "maxBeams": 24,
                        "maxRangeGates": 110,
                        "address" : "wss://chapman.usask.ca:5105",
                        "port" : 5105
                        },

             "forthayseast": {
                        "name": "Forth Hays East",
                        "maxBeams": 22,
                        "maxRangeGates": 110,
                        "address" : "wss://chapman.usask.ca:5106",
                        "port" : 5106
                        },

             "forthayswest": {
                        "name": "Forth Hays West",
                        "maxBeams": 22,
                        "maxRangeGates": 110,
                        "address" : "wss://chapman.usask.ca:5107",
                        "port" : 5107
                        },

             "kapuskasing": {
                        "name": "Kapuskasing",
                        "maxBeams": 16,
                        "maxRangeGates": 100,
                        "address" : "wss://chapman.usask.ca:5108"
                        },

             "goosebay": {
                        "name": "Goosebay",
                        "maxBeams": 16,
                        "maxRangeGates": 100,
                        "address" : "wss://chapman.usask.ca:5109"
                        },

             "christmasvalleyeast": {
                        "name": "Christmas Valley East",
                        "maxBeams": 24,
                        "maxRangeGates": 75,
                        "address" : "wss://chapman.usask.ca:5110"
                        },

             "christmasvalleywest": {
                        "name": "Christmas Valley West",
                        "maxBeams": 24,
                        "maxRangeGates": 75,
                        "address" : "wss://chapman.usask.ca:5111"
                        }
              };

#Check if database exists, if not, create it (easy in python 3.4+)
sqliteData = sqlite3.connect(database)
#Connect to Web sockets

while 1 {

#Parse JSON File

#Add new Data to SQLite Database

#Remove old Data from SQLite Database
}