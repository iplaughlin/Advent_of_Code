# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 20:53:39 2021

@author: Ian
"""

path = r'C:\Users\Ian\AnacondaProjects\Advent of Code\2021'
day = 6

out = []
with open(f'{path}/day{day}input.txt') as f:
    for line in f.readlines():
        for item in line.split(','):
            out.append(int(item))
    
time_to_reproduce = 6

test_case = [3,4,3,1,2]
    
def counting_down(fish_list):
    new_list = []
    for item in fish_list:
        new_item = item - 1
        if new_item == -1:
            new_item = 6
            second_item = 8
            new_list.extend([new_item, second_item])
        else:
            new_list.append(new_item)
    return new_list

out2 = out.copy()
for _ in range(0, 80):
    out2 = counting_down(out2)
print(len(out2))

#don't do this - takes WAAAAY too long
# for _ in range(0, 256):
#     out = counting_down(out)
    
from collections import defaultdict

def iterate_over_fish(fish_list, number_of_times):
    state = defaultdict(int)
    for fish in fish_list:
        state[fish] += 1
    for _ in range(number_of_times):
        state = update_dict(state)

    return sum(state.values())

def update_dict(original_dict):
    new_dict = defaultdict(int)
    for key, value in original_dict.items():
        if key == 0:
            new_dict[6] += value
            new_dict[8] += value
        else:
            new_dict[key-1] += value
    return new_dict

    

result = iterate_over_fish(out, 80)
print(result)

result = iterate_over_fish(out, 256)
print(result)
    