import csv
file = open('data/twitter_marketplace_data_5.csv', 'r')
lines = csv.reader(file)
for line in lines:
	print line

# Q1
