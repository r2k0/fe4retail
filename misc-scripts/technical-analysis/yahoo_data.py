#!/usr/local/bin/python3

import urllib.request
import os
import time
import datetime
import logging
import sys



desktopDir = os.path.join(os.path.expanduser("~"), "Dropbox/Stocks/")
os.chdir(desktopDir)
logging.basicConfig(filename='errorlog.log', level=logging.DEBUG)
directory = desktopDir + 'Yahoo-Data/'
if not os.path.exists(directory):
    os.makedirs(directory)
# Get Stockticker list
try:
    url = 'ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt'
    file = 'nasdaq.txt'
    print(url, '->', file)
    urllib.request.urlretrieve(url, file)
except:
    print("Error in getting file: " + file)

try:
    url = 'ftp://ftp.nasdaqtrader.com/SymbolDirectory/otherlisted.txt'
    file = 'otherTest.txt'
    print(url, '->', file)
    urllib.request.urlretrieve(url, file)
except:
    print("Error in getting file: " + file)

# Open File with stock ticker list
AMEXNYSE = open('otherTest.txt')
NASDAQ = open('nasdaq.txt')


# Get todays date in Year, Month, Date 
now = datetime.datetime.now()

year = now.year
month = now.month
date = now.day
today = str(year) + '-' + str(month) + '-' + str(date)

#get past header
AMEXNYSE.readline()
NASDAQ.readline()

errors = 0
firstLine = 0
stockLine = ""

f = open('Yahoo-Data_' + today + '.csv', 'w')
f.write('Symbol,Name,Last_Trade_Date,Last_Trade_Price,PE_Ratio,PEG_Ratio,\
        Earnings/Share,EPS_Estimate_Next_Quarter,EPS_Estimate_Next_Year,\
        Market_Cap,200-Day_Moving_Ave,Change_From_200-Day_Moving_Ave,\
        Percent_Change_From_200-Day-Moving_Ave,EBITDA\n')

print("Investigating AMEX-NYSE")
for line in AMEXNYSE:
    if firstLine == 0:
        firstLine = 1
        continue
    if 'File Creation Time' in line:
        break
    firstIndex = line.find('|')
    stockLine = line[:firstIndex]
    url = 'http://finance.yahoo.com/d/quotes.csv?s=' + stockLine + '&f=snd1l1rr5ee9e7j1m4m5m6j4'
    file = 'temp.csv'
    urllib.request.urlretrieve(url, file)
    temp = open('temp.csv', 'r')
    for line in temp:
        f.write(line)
    temp.close()

print("Investigating NASDAQ")
firstLine = 0
for line in NASDAQ:
    if firstLine == 0:
        firstLine = 1
        continue
    if 'File Creation Time' in line:
        break
    firstIndex = line.find('|')
    stockLine = line[:firstIndex]
    url = 'http://finance.yahoo.com/d/quotes.csv?s=' + stockLine + '&f=snd1l1rr5ee9e7j1m4m5m6j4'
    file = 'temp.csv'
    urllib.request.urlretrieve(url, file)
    temp = open('temp.csv', 'r')
    for line in temp:
        f.write(line)
    temp.close()

f.close()

