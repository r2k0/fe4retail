"""
The MIT License (MIT)
Copyright(c) 2014 Okkar Than

This is just for Python tutorial and demonstration.
To test if data sources are working properly using pandas
"""

from pandas.io.data import DataReader
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime
starting_date = datetime(2013,1,1)
ending_date = datetime(2013,12,1)


def readTickerData(ticker):
    ticker_df = DataReader(ticker, "yahoo", starting_date, ending_date)
    del ticker_df['Volume']
    del ticker_df['Open']
    del ticker_df['High']
    del ticker_df['Low']
    del ticker_df['Adj Close']
    return ticker_df

def daily_return(t_df):
    dlyr = t_df['Close'].shift(1) / t_df['Close'] - 1
    t_df['Daily Return'] = dlyr * 100
    return t_df
    
spy = readTickerData("SPY")

print "SPY historical data"
print spy.tail()

spy_d = daily_return(spy)
print "SPY daily retrun %"
print spy_d.tail()

print "SPY standard deviations of close prices and daily returns"
print spy_d.std()

#spy_d.plot(kind='bar')
spy_d.plot(y='Daily Return')
plt.axhline(0,color='k')
plt.savefig('spy.png')
