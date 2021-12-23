# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 00:26:22 2021

@author: Ian
"""

import pandas as pd

path = r"C:\Users\Ian\AnacondaProjects\Advent of Code\2021\input.txt"

temp = pd.read_csv(path, header = None, dtype = str)
temp_list = list(temp[0])

As = []
Bs = []
Cs = []
Ds = []
Es = []
Fs = []
Gs = []
Hs = []
Is = []
Js = []
Ks = []
Ls = []

for item in temp_list:
    a, b, c, d, e, f, g, h, i, j, k, l = list(item)
    As.append(a)
    Bs.append(b)
    Cs.append(c)
    Ds.append(d)
    Es.append(e)
    Fs.append(f)
    Gs.append(g)
    Hs.append(h)
    Is.append(i)
    Js.append(j)
    Ks.append(k)
    Ls.append(l)
    
criteria = lambda strs, pos, sort, default: ('1' if sort == 'most' else '0') if [x[pos] for x in strs].count('1') > [x[pos] for x in strs].count('0') else default if [x[pos] for x in strs].count('1') == [x[pos] for x in strs].count('0') else ('0' if sort == 'most' else '1')
    i, j, ox, co2 = (0, 0, data[:], data[:])
    while len(ox) > 1 or len(co2) > 1: 
        if len(ox) > 1: ox = [x for x in ox if x[i] == criteria(ox, i, 'most', '1')]
        if len(co2) > 1: co2 = [x for x in co2 if x[i] == criteria(co2, i, 'least', '0')]
        i, j = i + 1, j + 1
    print(int(ox[0], 2) * int(co2[0], 2))

lines = open(path).read().splitlines()
gamma = ""
eps = ""
for x in zip(*lines):
    if x.count('0') > x.count('1'):
        gamma += '0'
        eps += '1'
    else:
        gamma += '1'
        eps += '0'

g = int(gamma, 2)
e = int(eps, 2)
print('p1', e*g)

# oxygen:
data = lines[::]
for i in range(len(data[0])):
    # Take the bits from the i'th column of the data that is left.
    bits = list(zip(*data))[i]
    if len(data) == 1:
        break
    if bits.count('0') > bits.count('1'):
        data = [line for line in data if line[i] == '0']
    else:
        data = [line for line in data if line[i] == '1']
if len(data) == 1:
    oxygen = data[0]
oxygen = int(oxygen, 2)

# co2:
data = lines[::]
for i in range(len(data[0])):
    # Take the bits from the i'th column of the data that is left.
    bits = list(zip(*data))[i]
    if len(data) == 1:
        break
    if bits.count('0') <= bits.count('1'):
        data = [line for line in data if line[i] == '0']
    else:
        data = [line for line in data if line[i] == '1']
if len(data) == 1:
    co2 = data[0]
co2 = int(co2, 2)
print('p2', co2*oxygen)

def cols(rows):
    return zip(*rows)

def rule(rows, f):
    for i in range(len(rows[0])):
        # Take the bits from the i'th column of the data that is left.
        bits = list(cols(rows))[i]
        rows = [row for row in rows if row[i] == f(bits)]
        if len(rows) == 1:
            break
    else:
        raise Exception('More than 1 data left after filtering out')

    return int(rows[0], 2)

def get_oxygen(data):
    most_common = lambda bits: '1' if bits.count('1') >= len(bits) // 2 else '0'
    return rule(data, most_common)

def get_co2(data):
    least_common = lambda bits: '0' if bits.count('1') >= len(bits) // 2 else '1'
    return rule(data, least_common)

oxygen = get_oxygen(lines)
co2 = get_co2(lines)
print('p2', co2*oxygen)

def get_most_common(most_common_numbers_list, position, list_to_assess):
    count_list = []
    for item in list_to_assess:
        count_list.append(item[position])
    # print(count_list)
    for item in most_common_numbers_list:
        if count_list.count(item) > len(list_to_assess)/2:
            return item
        
def get_least_common(least_common_numbers_list, position, list_to_assess):
    count_list = []
    for item in list_to_assess:
        count_list.append(item[position])
    for item in least_common_numbers_list:
        if count_list.count(item) < len(list_to_assess)/2:
            return item

def oxy_generator(common_numbers, position, list_to_assess, how = 'most'):
    if how == 'most':
        common = get_most_common(common_numbers, position, list_to_assess)
        
    if how == 'least':
        common = get_least_common(common_numbers, position, list_to_assess)
    return common
    
    

x = 0
for item in most_common:
    temp_list2 = test(int(item), x, temp_list2)
    print(temp_list2)
    x+1
    if len(temp_list2) < 2:
        print(temp_list2)
        break