# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 16:14:38 2021

@author: Ian
"""

#import requests
path = r'C:\Users\Ian\AnacondaProjects\Advent of Code\2021'
day = 4
#input_url = f'https://adventofcode.com/2021/day/{day}/input'


#response = requests.get(input_url)

with open(f'{path}/day{day}input.txt') as f:
    out = f.readlines()

numbers = [int(item) for item in out[0].split(',')]

class board:
    def __init__(self, list_of_lists, size_of_matrix=5):
        self.list_of_lists = list_of_lists
        self.size_of_matrix = size_of_matrix
        self.horizontals = [item for item in self.list_of_lists]
        self.verticals = []
        for number in range(0, size_of_matrix):
            self.verticals.append([item[number] for item in self.list_of_lists])
        self.complete = False
    
    def find_in_horizontals(self, number):
        for index, sublist in enumerate(self.horizontals):
            if number in sublist:
                sublist[sublist.index(number)] = 'x'
                self.horizontals[index] = sublist
                return self.is_complete()
                
    def find_in_verticals(self, number):
        for index, sublist in enumerate(self.verticals):
            if number in sublist:
                sublist[sublist.index(number)] = 'x'
                self.verticals[index] = sublist
                return self.is_complete()

    def is_complete(self):
        for item in board_.verticals:
            result = all(element == 'x' for element in item)
            if result:
                self.complete = True
        for item in board_.horizontals:
            result = all(element == 'x' for element in item)
            if result:
                self.complete = True
        return self.complete

    def sum_of_board(self):
        sum_all = []
        for item in self.horizontals:
            sum_all.append(sum([part for part in item if isinstance(part, int)]))
        # print(sum_all)
        return sum(sum_all)


lists = []
boards = []
for line in out[1:]:
    line = line.strip()
    # print(line)
    if line != '':
        lists.append([int(item) for item in line.split(' ') if item != ''])
    if len(lists) == 5:
        boards.append(board(lists))
        lists = []


completed_boards = []
for number in numbers: 
    for index, board_ in enumerate(boards):
        # print(index)
        if index not in completed_boards:
            if board_.find_in_horizontals(number):
                completed_boards.append(index)
                print('completed', index)
                print(board_.sum_of_board()* number)
            elif board_.find_in_verticals(number):
                # print(board_.verticals)
                completed_boards.append(index)
                print('completed', index)
                print(board_.sum_of_board()*  number)
        else:
            pass
