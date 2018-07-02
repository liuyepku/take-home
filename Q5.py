import csv
import time
import matplotlib.pyplot as plt
import numpy as np

file = open('data/twitter_marketplace_data_5.csv', 'r')
lines = csv.reader(file)
head_row = next(lines)
print head_row
# for line in lines:
    # print line

# Q5
baseTime = "2018-04-23 00:00:00"
baseTimeArray = time.strptime(baseTime, "%Y-%m-%d %H:%M:%S")
timeShift = int(time.mktime(baseTimeArray))

cnt_c1 = 0
cnt_chg_c1 = 0
cnt_c2 = 0
cnt_chg_c2 = 0
bid_target_set_c1 = set()
bid_target_set_c2 = set()
timeSet_c1 = {}
timeSet_c2 = {}
for line in lines:
    if line[5] == 'APP_INSTALLS':
        cnt_c1+=1
        if line[6] != '0.0':
            cnt_chg_c1+=1
        # print line
        tp = (line[1], line[8], line[4])
        bid_target_set_c1.add(tp)

        # store value for plot campaign pacing
        if line[1] not in timeSet_c1:
            timeSet_c1[line[1]] = []
            timeSet_c1[line[1]].append((line[0], line[2]))
        else:
            timeSet_c1[line[1]].append((line[0], line[2]))

    if line[5] == 'VIDEO_VIEWS':
        cnt_c2+=1
        if line[6] != '0.0':
            cnt_chg_c2+=1
        # print line
        tp = (line[1], line[8], line[4])
        bid_target_set_c2.add(tp)

        # store value for plot campaign pacing
        if line[1] not in timeSet_c2:
            timeSet_c2[line[1]] = []
            timeSet_c2[line[1]].append((line[0], line[2]))
        else:
            timeSet_c2[line[1]].append((line[0], line[2]))

print "the engagement rate of app install is {}".format(cnt_chg_c1*1.0/cnt_c1)
print "the engagement rate of video view is {}".format(cnt_chg_c2*1.0/cnt_c2)
print "\n"

print "the bid value and targeting parameters for app install are: (campaign_id, bid, matched_targeting)"
for tp in bid_target_set_c1:
    print tp
print "the bid value and targeting parameters for video view are: (campaign_id, bid, matched_targeting)"
for tp in bid_target_set_c2:
    print tp



plt.figure(1)
plt.subplot(121)
plt.title("The campaign pacing of app install")
for attr in timeSet_c1:
    time_c1 = []
    spend_c1 = []
    for ts in timeSet_c1[attr]:
        tms = ts[0]
        tmwords = ts[0].split('.')
        timeArray = time.strptime(tmwords[0], "%Y-%m-%d %H:%M:%S")
        timeStamp = int(time.mktime(timeArray)) - timeShift
        timeStr = str(timeStamp) + '.' + tmwords[1]

        time_c1.append(float(timeStr))
        spend_c1.append(float(ts[1]))
    x1 = np.array(time_c1)
    y1 = np.array(spend_c1)
    plt.plot(x1, y1, label='campaign ' + attr)
    plt.legend(loc='upper right')

plt.xlabel("time")
plt.ylabel("spend")


plt.subplot(122)
plt.title("The campaign pacing of video view")
for attr in timeSet_c2:
    time_c2 = []
    spend_c2 = []
    for ts in timeSet_c2[attr]:
        tms = ts[0]
        tmwords = ts[0].split('.')
        timeArray = time.strptime(tmwords[0], "%Y-%m-%d %H:%M:%S")
        timeStamp = int(time.mktime(timeArray)) - timeShift
        timeStr = str(timeStamp) + '.' + tmwords[1]

        time_c2.append(float(timeStr))
        spend_c2.append(float(ts[1]))
    x2 = np.array(time_c2)
    y2 = np.array(spend_c2)
    plt.plot(x2, y2, label='campaign ' + attr)
    plt.legend(loc='upper right')

plt.xlabel("time")
plt.ylabel("spend")
plt.show()