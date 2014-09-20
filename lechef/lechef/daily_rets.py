"""
The MIT License (MIT)
Copyright(c) 2014 Okkar Than

This is just for Python tutorial and demonstration. 
"""
import numpy as np
import pandas as pd
from parse import parse




def calculate_daily(data):
	"""	calculate daily returns """
	# r(t) = ( price(t)/price(t-1) ) - 1

	daily_ret = 0
	prev_close = 0
	for kv in data:
		if prev_close > 0: 
			daily_ret = (float(kv["Close"]) / prev_close) - 1
			daily_ret = round(daily_ret,5) * 100
		print kv["Date"], kv["Close"], daily_ret
		prev_close = float(kv["Close"])
	


def daily_returns():
	# get SPY, QQQ, DIA data from csv files
	spy_data = parse("../data/spy_2013.csv", ",")
	#qqq_data = parse("../data/qqq_2013.csv", ",")
	#dia_data = parse("../data/dia_2013.csv", ",")
	spy_data.reverse()	
	#qqq_data.reverse()
	#dia_data.reverse()
	calculate_daily(spy_data)

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
