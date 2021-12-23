# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 06:35:42 2020

@author: Ian
"""

import pandas as pd

path = r"C:\Users\Ian\AnacondaProjects\Advent of Code\2021\input.txt"

temp = pd.read_csv(path, header = None)
temp_list = list(temp[0])

#-------------
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
    