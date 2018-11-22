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
    with open('status.txt', 'w') as f:
        # re-write the file with the current data we got:
        month_dict = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep',10:'Oct', 11:'Nov', 12:'Dec'}
        now = datetime.datetime.now()
        year = now.year
        day = now.day 
        date = month_dict[now.month] +' '+ str(day)+' ' + str(year)
        
        hour = ('0'+ str(now.hour))[-2:] + ':' +('0'+ str(now.minute))[-2:] +':'+ ('0'+ str(now.second))[-2:]



        new_data_string = 'Status is ~~' +  inDataDict.getvalue('status') + '~~ at '+hour+' '+ date + ' Boston Time'
        f.write(new_data_string)

# now, whether or not we modified the file, we will print the file out, since this is the most recent update

with open ('status.txt', 'r') as f:
    data = f.read()
    print(data)



