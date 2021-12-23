# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 23:58:11 2021

@author: Ian
"""

import pandas as pd

path = r"C:\Users\Ian\AnacondaProjects\Advent of Code\2021\input.txt"

temp = pd.read_csv(path, header = None)
temp_list = list(temp[0])

#-------------
horizontal = 0
depth = 0
aim = 0
for item in temp_list:
    result = item.split(' ')
    direction = result[0]
    amount = result[1]
    if 'forward' in direction:
        temp = int(amount)
        if not aim == 0:
            horizontal += int(amount)
            depth += int(amount) * aim
        else:
            horizontal += int(amount)
    elif 'down' in direction:
        aim += int(amount)
    elif 'up' in direction:
        aim -= int(amount)
    else:
        print(direction)
x=0
for i, j in enumerate(temp_list[:-1]):
    if j < temp_list[i+1]:
        x+=1

#--------------
y=0
n=3
for i in range(len(temp_list)-n+1):
    window = temp_list[i:i+n]
    temp_list2.append(sum(window))
    # temp_list2.append(window)
    print(window)
    