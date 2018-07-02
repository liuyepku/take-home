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
