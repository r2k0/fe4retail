"""
The MIT License (MIT)
Copyright(c) 2014 Okkar Than

"""

from pandas.io.data import DataReader
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from datetime import datetime
starting_date = datetime(2013,1,1)
ending_date = datetime(2013,12,1)


   
def chart_data(ticker):
    
    def readTickerData(ticker):
        """ read equity data and return as dataframe """
        ticker_df = DataReader(ticker, "yahoo", starting_date, ending_date)
        del ticker_df['Volume']
        del ticker_df['Open']
        del ticker_df['High']
        del ticker_df['Low']
        del ticker_df['Adj Close']
        return ticker_df
    
    def daily_return(t_df):
        """ add daily return column to the data frame """
        dlyr = t_df['Close'].shift(1) / t_df['Close'] - 1
        t_df['Daily Return'] = dlyr * 100
        return t_df
     

    d = readTickerData(ticker)
    df = daily_return(d)

    # Standard Deviation of Close and Daily Return
    print ticker,"standard deviations of close prices and daily returns"
    print df.std()
    del df['Close']
    return df



def main():
    spy_d = chart_data("SPY")
    qqq_d = chart_data("QQQ")
    dia_d = chart_data("DIA")
    tlt_d = chart_data("TLT")
    
    fig = plt.figure()
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    ax4 = fig.add_subplot(2,2,4)

    ax1.set_title('SPY Daily Returns')
    spy_d.plot(ax=ax1,y='Daily Return')
    plt.savefig('daily_return.png')
    
    ax2.set_title('QQQ Daily Returns')
    qqq_d.plot(ax=ax2,y='Daily Return')
    plt.savefig('daily_return.png')

    ax3.set_title('DIA Daily Returns')
    dia_d.plot(ax=ax3,y='Daily Return')
    plt.savefig('daily_return.png')
    
    ax4.set_title('TLT Daily Returns')
    tlt_d.plot(ax=ax4,y='Daily Return')
    plt.tight_layout() 
    plt.savefig('daily_return.png')

if __name__ == "__main__":
    main()
