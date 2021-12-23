# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 23:14:11 2021

@author: Ian
"""

path = r'C:\Users\Ian\AnacondaProjects\Advent of Code\2021'
day = 7

out = []
with open(f'{path}/day{day}input.txt') as f:
    for line in f.readlines():
        for item in line.split(','):
            out.append(int(item))
            
            
test_cases = [16,1,2,0,4,2,7,1,2,14]

#part 1
all_loops = []
for number in range(min(out), max(out)):
    first_loop = []
    for item in out:
        distance = abs(item - number)
        first_loop.append(distance)
    all_loops.append(sum(first_loop))
print(min(all_loops))


#part 2
all_loops = []
for number in range(min(out), max(out)):
    print(number)
    first_loop = []
    for item in out:
        distance = abs(item - number)
        distance2 = sum(range(1, distance+1))
        first_loop.append(distance2)
    all_loops.append(sum(first_loop))
print(min(all_loops))
