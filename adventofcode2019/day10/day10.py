# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 22:43:53 2019

@author: strahl
"""

import math

with open('day10_input.txt') as fp:
    input = fp.readlines()

#Convert string list to list-in-list
input_list = []
for line in input:
    input_list.append([ch for ch in line])
print(input_list)

#Fill coordinate list by "asteroid map"
asteroids = []
for x in range(len(input_list)):
    for y in range(len(input_list[x])):
        if input_list[x][y] == '#':
            asteroids.append({'x': x, 'y': y})

max_detectable_count = 0
for candidate in asteroids:
    asteroid_detect_list = []
    for other in asteroids:
        if candidate == other:
            continue
        other['dy'] = candidate['y']-other['y']
        other['dx'] = candidate['x']-other['x']
        other['angle'] = round(math.atan2(other['dy'], other['dx']), 4)
        other['dist'] = round(math.sqrt(other['dx']**2 + other['dy']**2), 4)
        asteroid_detect_list.append(other)
    #Detectable asteroids = distinct angles count
    detectable_count = len(set([x['angle'] for x in asteroid_detect_list]))
    print(detectable_count)
    if detectable_count > max_detectable_count:
        max_detectable_count = detectable_count
print('Maximal other asteroid detectable from a location: ' + str(max_detectable_count))