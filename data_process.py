import csv
import time
file = open('data/twitter_marketplace_data_5.csv', 'r')
lines = csv.reader(file)
head_row = next(lines)
# for line in lines:
	# print line

# Q1
time_c1 = []
spend_c1 = []
time_c2 = []
spend_c2 = []
for line in lines:
	if line[1] == '1':
		tms = line[0]
		tmwords = line[0].split('.')
		timeArray = time.strptime(tmwords[0], "%Y-%m-%d %H:%M:%S")
		timeStamp = int(time.mktime(timeArray))
		timeStr = str(timeStamp) + '.' + tmwords[1]

		time_c1.append(timeStr)
		spend_c1.append(line[2])
	if line[1] == '2':
		# print line
		tmwords = line[0].split('.')
		timeArray = time.strptime(tmwords[0], "%Y-%m-%d %H:%M:%S")
		timeStamp = int(time.mktime(timeArray))
		timeStr = str(timeStamp) + '.' + tmwords[1]

		time_c2.append(timeStr)
		spend_c2.append(line[2])



print time_c2
print spend_c2