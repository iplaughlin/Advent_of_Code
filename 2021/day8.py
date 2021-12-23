# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 08:36:47 2021

@author: Ian
"""

path = r'C:\Users\Ian\AnacondaProjects\Advent of Code\2021'
day = 8

out = []
signal_patterns = []
output_values = []
with open(f'{path}/day{day}input.txt') as f:
    for line in f.readlines():
        new_line = line.split('|')
        signal_pattern = new_line[0].split()
        output_value = new_line[1].split()
        signal_patterns.append(signal_pattern)
        output_values.append(output_value)

number_dict = {0: ['a', 'b', 'c', 'e', 'f', 'g'],
               1: ['c', 'f'],
               2: ['a', 'c', 'd', 'e', 'g'],
               3: ['a', 'c', 'd', 'f', 'g'],
               4: ['b', 'c', 'd', 'f'],
               5: ['a', 'b', 'd', 'f', 'g'],
               6: ['a', 'b', 'd', 'e', 'f', 'g'],
               7: ['a', 'c', 'f'],
               8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
               9: ['a', 'b', 'c', 'd', 'f', 'g']}





