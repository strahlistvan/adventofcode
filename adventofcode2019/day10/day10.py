# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 22:43:53 2019

@author: strahl
"""

import math

with open('day10_input.txt') as fp:
    input = fp.readlines()

input = [".#....#####...#..",
"##...##.#####..##",
"##...#...#.#####.",
"..#.....X...###..",
"..#.#.....#....##" ]

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

def get_asteroid_detect_list(station, asteroids):
    asteroid_detect_list = []
    for other in asteroids:
        if station == other:
            continue
        other['dy'] = station['y']-other['y']
        other['dx'] = station['x']-other['x']
        other['angle'] = round(math.atan2(other['dy'], other['dx']), 4)
        other['dist'] = round(math.sqrt(other['dx']**2 + other['dy']**2), 4)
        asteroid_detect_list.append(other)
    return asteroid_detect_list

# part 1 - find 
max_detectable_count = 0
station_asteroid = asteroids[0]
positions_from_station = {}
for candidate in asteroids:
    asteroid_detect_list = get_asteroid_detect_list(candidate, asteroids)
    #Detectable asteroids = distinct angles count
    detectable_count = len(set([x['angle'] for x in asteroid_detect_list]))
    print(detectable_count)
    if detectable_count > max_detectable_count:
        max_detectable_count = detectable_count
        station_asteroid = { 'x': candidate['x'], 'y': candidate['y'] }
        positions_from_station = asteroid_detect_list
print('Maximal other asteroid detectable from a location: ' + str(max_detectable_count))
print(station_asteroid)
print(len(positions_from_station))

#part 2
positions_from_station.sort(key=lambda x: ((x['angle'] + 1.5*math.pi) % 2*math.pi, x['dist']), reverse=False)
print(positions_from_station)

for i in range(10):
    data = positions_from_station.pop()
    product = 100*data['x']+data['y']
    print(str(data['x']) + ", " + str(data['y']) + ' - ' + str(product))