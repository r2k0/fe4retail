"""
The MIT License (MIT)
Copyright(c) 2014 Okkar Than

This is just for Python tutorial and demonstration. 
"""
import numpy as np
import pandas as pd
from parse import parse
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def chart_daily(data):
	"""	calculate daily returns """
	# r(t) = ( price(t)/price(t-1) ) - 1

	daily_ret = 0
	prev_close = 0
	dates = []
	drl = []
	for kv in data:
		d = kv["Date"]
		if prev_close > 0: 
			daily_ret = (float(kv["Close"]) / prev_close) - 1
			daily_ret = round(daily_ret,5) * 100
		print d, kv["Close"], daily_ret
		drl.append(daily_ret)
		dates.append(d)
		prev_close = float(kv["Close"])
	#for i in drl: print i
	x = tuple(dates)
	plt.plot(drl)
	plt.savefig("test.png")	


def daily_returns():
	# get SPY, QQQ, DIA data from csv files
	spy_data = parse("../data/spy_2013.csv", ",")
	#qqq_data = parse("../data/qqq_2013.csv", ",")
	#dia_data = parse("../data/dia_2013.csv", ",")
	spy_data.reverse()	
	#qqq_data.reverse()
	#dia_data.reverse()
	chart_daily(spy_data)

def cumm_daily_returns():
	""" cummulative daily returns """
	return

def port_daily_returns():
	""" porfolio daily returns """
	return

def main():
	daily_returns()


if __name__ == "__main__":
	main()
