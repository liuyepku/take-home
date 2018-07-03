import csv
import time
import matplotlib.pyplot as plt
import numpy as np

file = open('data/twitter_marketplace_data_5.csv', 'r')
lines = csv.reader(file)
head_row = next(lines)
print head_row
# for line in lines:
    # print line[7]

cnt_app = 0
cnt_app_see = 0
cnt_vid = 0
cnt_vid_see = 0
cnt_web = 0
cnt_web_see = 0
for line in lines:
    if line[5] == 'APP_INSTALLS':
        cnt_app+=1
        if line[7] == 'True':
            cnt_app_see+=1
    if line[5] == 'VIDEO_VIEWS':
        cnt_vid += 1
        if line[7] == 'True':
            # print line
            cnt_vid_see += 1
    if line[5] == 'WEBSITE_CLICKS':
        cnt_web += 1
        if line[7] == 'True':
            # print line
            cnt_web_see += 1

print "the user observation rate of app install is {}".format(cnt_app_see*1.0/cnt_app)
print "the user observation rate of video view is {}".format(cnt_vid_see*1.0/cnt_vid)
print "the user observation rate of web clicks is {}".format(cnt_web_see*1.0/cnt_web)
