"""
Financial Data Visualization Project

Parse data from CSV file to render it in JSON,
save to a database for calculation and charting.

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
