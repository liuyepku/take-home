import csv
import time
import matplotlib.pyplot as plt
import numpy as np

file = open('data/twitter_marketplace_data_5.csv', 'r')
lines = csv.reader(file)
head_row = next(lines)
# for line in lines:
#     print line

# Q1
baseTime = "2018-04-23 00:00:00"
baseTimeArray = time.strptime(baseTime, "%Y-%m-%d %H:%M:%S")
timeShift = int(time.mktime(baseTimeArray))

time_c1 = []
spend_c1 = []
time_c2 = []
spend_c2 = []
for line in lines:
    if line[1] == '1':
        tms = line[0]
        tmwords = line[0].split('.')
        timeArray = time.strptime(tmwords[0], "%Y-%m-%d %H:%M:%S")
        timeStamp = int(time.mktime(timeArray)) - timeShift
        timeStr = str(timeStamp) + '.' + tmwords[1]

        time_c1.append(float(timeStr))
        spend_c1.append(float(line[2]))
    if line[1] == '2':
        # print line
        tmwords = line[0].split('.')
        timeArray = time.strptime(tmwords[0], "%Y-%m-%d %H:%M:%S")
        timeStamp = int(time.mktime(timeArray)) - timeShift
        timeStr = str(timeStamp) + '.' + tmwords[1]

        time_c2.append(float(timeStr))
        spend_c2.append(float(line[2]))

plt.figure(1)
plt.subplot(121)
plt.title("Campaigns 1")
x1 = np.array(time_c1)
y1 = np.array(spend_c1)
plt.plot(x1, y1)
plt.xlabel("time")
plt.ylabel("spend")

plt.subplot(122)
plt.title("Campaigns 2")
x2 = np.array(time_c2)
y2 = np.array(spend_c2)
plt.plot(x2, y2)
plt.xlabel("time")
plt.ylabel("spend")
plt.show()



