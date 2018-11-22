#!/usr/bin/env python
print( "Content-type: text/html\n")
import cgitb
import cgi
import datetime
import sqlite3
import datetime
cgitb.enable()

#command below takes the arguements from the get request and puts them in some sort of a dictionary

inDataDict = cgi.FieldStorage()

#ask that the info will bi in the form of asdfgefs/dataHandler.py?status='alive' OR 'filming'
if 'status' in inDataDict:
    # modify the txt file
    print('Status is', inDataDict['status']['status'], 'at', datetime.datetime.now())

# print the txt file