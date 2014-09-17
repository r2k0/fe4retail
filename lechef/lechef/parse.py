"""
Financial Data Visualization Project

Parse data from CSV file to render it in JSON,
save to a database for calculation and charting.

"""
import json
import csv

INPUT = "../data/spy.csv"

def parse(raw_file, delimiter):
	""" parses CSV to JSON """
	
	f = open(raw_file)
	
	csv_data = csv.reader(f, delimiter=delimiter)
	
	pdata = []
	
	fields = csv_data.next()
	
	for r in csv_data: 
		pdata.append(dict(zip(fields,r)))
	
	f.close()
	
	return pdata

def main():
	spy_data = parse(INPUT,",")
	print spy_data
	

if __name__ == "__main__":
	main()
