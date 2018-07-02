import csv
import time
import matplotlib.pyplot as plt
import numpy as np

file = open('data/twitter_marketplace_data_5.csv', 'r')
lines = csv.reader(file)
head_row = next(lines)
# for line in lines:
    # print line

# Q3
bid_target_set_c1 = set()
bid_target_set_c2 = set()
for line in lines:
    if line[1] == '1':
        tp = (line[8], line[4])
        bid_target_set_c1.add(tp)
        # print line[1], line[4], line[8]
    if line[1] == '2':
        tp = (line[8], line[4])
        bid_target_set_c2.add(tp)
        # print line[1], line[4], line[8]

print "the bid value and targeting parameters for campaign 1 are: "
for tp in bid_target_set_c1:
    print tp
print "the bid value and targeting parameters for campaign 2 are: "
for tp in bid_target_set_c2:
    print tp