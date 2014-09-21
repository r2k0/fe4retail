import Quandl
data = Quandl.get('GOOG/NYSE_SPY',collapse='yearly')
print data.tail()
