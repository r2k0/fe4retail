"""
The MIT License (MIT)
Copyright(c) 2014 Okkar Than

This is just for Python tutorial and demonstration.
To test if data sources are working properly using pandas
"""
from math import sqrt
from pandas.io.data import DataReader
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime
starting_date = datetime(2013,1,1)
ending_date = datetime(2013,12,1)


def readTickerData(ticker):
    """ read equity data and return as dataframe """
    ticker_df = DataReader(ticker, "yahoo", starting_date, ending_date)
    #del ticker_df['Volume']
    #del ticker_df['Open']
    #del ticker_df['High']
    #del ticker_df['Low']
    #del ticker_df['Adj Close']
    return ticker_df

def daily_return(t_df):
    """ add daily return column to the data frame """
    dlyr = t_df['Close'].shift(1) / t_df['Close'] - 1
    t_df['Daily Return'] = dlyr * 100
    return t_df

def moving_average(t_df):
    adjclose = t_df['Adj Close']
    mavg = pd.rolling_mean(adjclose, 40)
    t_df['MA'] = mavg
    print t_df.tail()
    return t_df

def main():
    spy = readTickerData("SPY")
    spy_d = daily_return(spy)
    moving_average(spy)

    qqq = readTickerData("QQQ")
    qqq_d = daily_return(qqq)
    
    dia = readTickerData("DIA")
    dia_d = daily_return(dia)
    
    tlt = readTickerData("tlt")
    tlt_d = daily_return(tlt)

    #print "SPY historical data"
    #print spy.tail()
    #print "SPY daily retrun %"
    #print spy_d.tail()
    
    # Standard Deviation of Close and Daily Return
    print "SPY standard deviations of close prices and daily returns"
    print spy_d.std()
    print "QQQ standard deviations of close prices and daily returns"
    print qqq_d.std()
    print "DIA standard deviations of close prices and daily returns"
    print dia_d.std()
    print "TLT standard deviations of close prices and daily returns"
    print tlt_d.std()

    #sharpe ratio = sqrt(250)*average daily return / std of daily returns
    # 250 total trading days for one year
    #spy_sr = sqrt(250) * spy_d['Daily Return'].mean()/spy_d['Daily Return'].std()
    #print "Sharpe ratio for SPY:", spy_sr

    # plot daily return percent
    #spy_d.plot(y='Daily Return')
    #plt.axhline(0,color='g')
    #plt.savefig('spy.png')
    fig = plt.figure()
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    ax4 = fig.add_subplot(2,2,4)

    
    ax1.set_title('SPY Daily Returns')
    spy_d.plot(ax=ax1,y='Daily Return')
    plt.savefig('charts.png')

    ax2.set_title('QQQ Daily Returns')
    qqq_d.plot(ax=ax2,y='Daily Return')
    plt.savefig('charts.png')

    ax3.set_title('DIA Daily Returns')
    dia_d.plot(ax=ax3,y='Daily Return')
    plt.savefig('charts.png')

    ax4.set_title('TLT Daily Returns')
    tlt_d.plot(ax=ax4,y='Daily Return')
  
    # tight_layout automatically adjuts subplot params
    plt.tight_layout()
    
    plt.savefig('charts.png')


if __name__ == "__main__":
    main()
