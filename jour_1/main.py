#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
def main():
	print("Hello World!") 

	with open('input.txt', 'r') as read_obj: # read csv file as a list of lists
  		csv_reader = csv.reader(read_obj) # pass the file object to reader() to get the reader object
  		list_of_rows = list(csv_reader) # Pass reader object to list() to get a list of lists
	for i in range(0,len(list_of_rows)) : list_of_rows[i][0] = int(list_of_rows[i][0])
	print(list_of_rows[0])
	print(len(list_of_rows))
	response=0

	prev_sum = list_of_rows[0][0] +list_of_rows[1][0]+list_of_rows[2][0]
	for i in range(1,len(list_of_rows)-2):
		sum = list_of_rows[i][0] +list_of_rows[i+1][0]+list_of_rows[i+2][0]
		print(sum) 
		if sum > prev_sum : 
			response = response + 1
		prev_sum = sum
	print("la reponse est :" + str(response))

if __name__ == "__main__":
	main() 

