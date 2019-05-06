# Author: Danno Peters, Danno@dannopeters.ca
# Language Python 2.7
# Purpose: Upkeeps an SQLite database of SuperDARN Chart Data
# Input: JSON files from RADARs
# Output: Populated SQLite Database

#import required libaraies
import sqlite #allows for interation with SQLite databases
import sys
import pathlib
import json #allows python to parse JSON files
import asyncio #used for asynchronous communication (WSS)
import websockets #used tyo connect to chapman server websockets

# Variables
	database = 'realtime-charts.sqlite' #set name of SQLite database to be found or created
	sqlPath = PurePath('') #set path to SQLite Database
	dataSpan = 1 #length of time to store data (Hours)

#Check if database exists, if not, create it

#Connect to Web sockets

while 1 {

#Parse JSON File

#Add new Data to SQLite Database

#Remove old Data from SQLite Database
}