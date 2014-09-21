"""
The MIT License (MIT)
Copyright(c) 2014 Okkar Than

This is just for Python tutorial and demonstration. 
"""
import csv
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def parse(raw_file, delimiter):
	""" parses CSV to JSON """
	# open CSV file
	csvfile = open(raw_file,'r')
	# read CSV data
	csv_data = csv.reader(csvfile, delimiter=delimiter)
	# parsed data
	pdata = []
	keys = csv_data.next()
	for values in csv_data:
		# append dict(key, values) to pdata list
		# dictionary = dict(zip(keys, values))
		pdata.append(dict(zip(keys, values)))
	csvfile.close()
	return pdata


def chart_daily(data):
	"""	calculate daily returns """
	# r(t) = ( price(t)/price(t-1) ) - 1
	csvfile = open("daily_returns.csv",'wb')
	daily_ret = 0
	prev_close = 0
	dates = []
	drl = []
	writer = csv.writer(csvfile)
	writer.writerow( ('Date','Close','Daily Return') )
	print "Date","\t","Close","\t","Daily Return"
	for kv in data:
		d = kv["Date"]
		if prev_close > 0: 
			daily_ret = (float(kv["Close"]) / prev_close) - 1
			daily_ret = round(daily_ret,5) * 100
		print d, kv["Close"], daily_ret
		writer.writerow((d, kv["Close"], daily_ret))

		drl.append(daily_ret)
		dates.append(d)
		prev_close = float(kv["Close"])
	#for i in drl: print i
	csvfile.close()

def daily_returns():
	# get SPY, QQQ, DIA data from csv files
	spy_data = parse("../data/spy_2013.csv", ",")
	spy_data.reverse()	
	chart_daily(spy_data)

def main():
	daily_returns()


if __name__ == "__main__":
	main()
