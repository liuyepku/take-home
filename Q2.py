import csv
import time
import matplotlib.pyplot as plt
import numpy as np

file = open('data/twitter_marketplace_data_5.csv', 'r')
lines = csv.reader(file)
head_row = next(lines)
print head_row
# for line in lines:
#     print line

# Q2
cnt_c1 = 0
cnt_chg_c1 = 0
cnt_c2 = 0
cnt_chg_c2 = 0
for line in lines:
    if line[1] == '1':
        cnt_c1+=1
        if line[6] != '0.0':
            cnt_chg_c1+=1
            # print line[6]
    if line[1] == '2':
        cnt_c2+=1
        if line[6] != '0.0':
            cnt_chg_c2+=1
            # print line[6]

print "the engagement rate of campaign 1 is {}".format(cnt_chg_c1*1.0/cnt_c1)
print "the engagement rate of campaign 2 is {}".format(cnt_chg_c2*1.0/cnt_c2)