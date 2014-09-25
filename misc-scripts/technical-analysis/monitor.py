#!/usr/bin/env python

from __future__ import print_function
import subprocess
from sys import argv
from datetime import datetime
from time import sleep

script, symbol = argv
curl_str = "curl -s 'http://download.finance.yahoo.com/d/quotes.csv?s=" + symbol + "&f=l1'" 

format = "%m%d%Y"
logfile = str(symbol) + "_" + datetime.now().strftime(format)  + ".log"
#print("file name: " + logfile)
target = open(logfile,'w')

format = "%m/%d/%Y:%H:%M:%S"
counter = 0

while counter < 5760:
    time = datetime.now()
    price = subprocess.check_output(curl_str,shell=True)
    output = str(time.strftime(format)) + ", " + price 
    target.write(output)
    #print(output, end='')
    sleep(5)
    counter = counter + 1

target.close()
