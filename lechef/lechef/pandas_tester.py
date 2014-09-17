"""
To test if data sources are working properly using pandas

Copyright(c) 2014 E. Okkar Than
Distributed under MIT License. 
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

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
