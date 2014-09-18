"""
Financial Data Visualization Project

Parse data from CSV file 

"""
import csv

INPUT = "../data/spy.csv"

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

def main():
	spy_data = parse(INPUT,",")
	print spy_data
	

if __name__ == "__main__":
	main()
