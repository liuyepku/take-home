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

# Q4
imp_dol_set = {}
imp_cnt_set = {}
imp_bid_tar_set = {}
for line in lines:
    if line[1] not in imp_dol_set:
        imp_cnt_set[line[1]] = 1
        imp_dol_set[line[1]] = []
        imp_dol_set[line[1]].append((imp_cnt_set[line[1]], line[2]))
        imp_bid_tar_set[line[1]] = set()
        imp_bid_tar_set[line[1]].add((line[4], line[8]))
    else:
        imp_cnt_set[line[1]] += 1
        imp_dol_set[line[1]].append((imp_cnt_set[line[1]], line[2]))
        imp_bid_tar_set[line[1]].add((line[4], line[8]))

plt.figure(1)
plt.title("The number of impressions per dollar spend")
for cpg in imp_dol_set:
    imp_cnt = []
    spend_cnt = []
    for ts in imp_dol_set[cpg]:
        imp_cnt.append(float(ts[0]))
        spend_cnt.append(float(ts[1]))

    x1 = np.array(imp_cnt)
    y1 = np.array(spend_cnt)
    plt.plot(x1, y1, label='campaign ' + cpg)
    plt.legend(loc='upper right')

plt.xlabel("dollars spend")
plt.ylabel("# of impressions")
plt.show()

for cpg in imp_bid_tar_set:
    print "The campaign " + cpg + " bid and targeting criteria is :"
    for key in imp_bid_tar_set[cpg]:
        print key