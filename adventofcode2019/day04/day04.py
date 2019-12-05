# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 21:45:43 2019

@author: strahl
"""

range_start = 236491
range_end = 713787

def has_2_adj_digits(num):
    num_str = str(num)
    for i in range(1, len(num_str)):
        if num_str[i-1] == num_str[i]:
            return True
    return False

def never_decrease(num):
    num_str = str(num)
    for i in range(1, len(num_str)):
        if num_str[i-1] > num_str[i]:
            return False
    return True

total = 0
for num in range(range_start, range_end):
    if has_2_adj_digits(num) and never_decrease(num):
        total += 1

print(total)

#part 2
def contains_exactly_2_adj(num):
    num_str = str(num)
    group_size = 1
    c = num_str[0]
    for i in range(1, len(num_str)):
        if num_str[i] == c:
            group_size += 1
        else:
            if group_size == 2:
                return True
            group_size = 1
            c = num_str[i]
    if group_size == 2:
        return True
    return False

if contains_exactly_2_adj('111333'):
    print('111333 is good')
else:
   print('No good')

total = 0
for num in range(range_start, range_end):
    if contains_exactly_2_adj(num) and never_decrease(num):
        total += 1

print(total)
