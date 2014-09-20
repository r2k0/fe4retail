""" QSTK utils """

import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd



def main():

	ls_symbols = ["SPY"]
	dt_start = dt.datetime(2013,1,1)
	dt_end = dt.datetime(2013,12,31)
	dt_timeofday = dt.timedelta(hours=16)
	ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)
