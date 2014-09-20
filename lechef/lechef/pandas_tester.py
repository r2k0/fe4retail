"""
The MIT License (MIT)
Copyright(c) 2014 Okkar Than

This is just for Python tutorial and demonstration.
To test if data sources are working properly using pandas
"""
from pandas.io.data import DataReader
from datetime import datetime
starting_date = datetime(2014,1,1)
ending_date = datetime(2014,8,7)


def readIndexData(ticker):
	ticker_df = DataReader(ticker, "yahoo", starting_date, ending_date)
	#del ticker_df['Volume']
	return ticker_df


print "SPY historical data"
print readIndexData("SPY")[:5] 


print "QQQ historical data"
print readIndexData("QQQ")[:5]

print "DIA historical data"
print readIndexData("DIA")[:5]
