#!/usr/bin/env python
from pandas.io.data import DataReader
import matplotlib.pyplot as plt
import datetime
import pandas as pd

vxx = DataReader("vxx", "yahoo", datetime.datetime(2012, 1, 1),datetime.datetime(2013,1,1))
vxx['30_MA_Open'] = pd.stats.moments.rolling_mean(vxx['Open'], 30)
vxx['150_MA_Open'] = pd.stats.moments.rolling_mean(vxx['Open'], 150)
vxx[20:60]

top = plt.subplot2grid((4,4), (0, 0), rowspan=3, colspan=4)
top.plot(vxx.index, vxx['Open'], label='Open')
top.plot(vxx.index, vxx['30_MA_Open'], label='30 Day MA')
top.plot(vxx.index, vxx['150_MA_Open'], label='150 Day MA')
plt.title('Opening Stock Price from 2012 - 2013')
plt.legend()

bottom = plt.subplot2grid((4,4), (3,0), rowspan=1, colspan=4)
bottom.bar(vxx.index, vxx['Volume'])

plt.title('Trading Volume')
plt.gcf().set_size_inches(15,8)
