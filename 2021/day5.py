# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 20:20:50 2021

@author: Ian
"""

path = r'C:\Users\Ian\AnacondaProjects\Advent of Code\2021'
day = 5

with open(f'{path}/day{day}input.txt') as f:
    out = [line.strip() for line in f.readlines()]

rule_1_lines = []

for line in out:
    x1, y1 = line.split('->')[0].strip().split(',')
    x2, y2 = line.split('->')[1].strip().split(',')
    if (x1 == x2) or (y1==y2):
        rule_1_lines.append((int(x1), int(y1), int(x2), int(y2)))

def get_line(x1, y1, x2, y2):
    points = []
    issteep = abs(y2-y1) > abs(x2-x1)
    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        rev = True
    deltax = x2 - x1
    deltay = abs(y2-y1)
    error = int(deltax / 2)
    y = y1
    ystep = None
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1
    for x in range(x1, x2 + 1):
        if issteep:
            points.append((y, x))
        else:
            points.append((x, y))
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax
    return points

rule_2_lines = []
for group in rule_1_lines:
    rule_2_lines.extend(get_line(*group))

from collections import Counter
result = Counter(rule_2_lines)

result2 = Counter(result.values())
print(result2)

def slope(x1, y1, x2, y2):
    if x1 == x2:
        return 0
    else:
        m = (y2 - y1) / (x2 - x1)
        return int(m)

rule_3_lines = []
for line in out:
    x1, y1 = line.split('->')[0].strip().split(',')
    x2, y2 = line.split('->')[1].strip().split(',')
    print(slope(int(x1), int(y1), int(x2), int(y2)))
    if slope(int(x1), int(y1), int(x2), int(y2)) in [1, 0, -1, -0]:
        rule_3_lines.append((int(x1), int(y1), int(x2), int(y2)))
rule_4_lines = []
for group in rule_3_lines:
    rule_4_lines.extend(get_line(*group))

result3 = Counter(rule_4_lines)

result4 = Counter(result3.values())
print(result4)
