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
    gs = gridspec.GridSpec(2,2)
    ax_list=[fig.add_subplot(ss) for ss in gs]

    ax_list[0].plot(spy_d)
    ax_list[1].plot(qqq_d)
    ax_list[2].plot(dia_d)
    ax_list[3].plot(tlt_d)

    ax_list[0].set_title('SPY')
    ax_list[1].set_title('QQQ')
    ax_list[2].set_title('DIA')
    ax_list[3].set_title('TLT')

    plt.savefig('daily_return.png')
    


if __name__ == "__main__":
    main()
