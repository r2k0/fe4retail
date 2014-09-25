#!/usr/bin/env python
from pandas.io.data import DataReader
from sys import argv
import datetime
import pandas as pd

script, symbol, b_year, b_month, b_day, e_year, e_month, e_day = argv
# date format (year,month,day)

sym = DataReader(str(symbol),"yahoo", datetime.datetime(int(b_year),int(b_month),int(b_day)),datetime.datetime(int(e_year),int(e_month),int(e_day)))
print sym[0:]

#### Example ####
# python data_range.py goog 2012 06 01 2013 03 05
#

