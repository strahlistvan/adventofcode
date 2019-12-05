# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 20:18:35 2019

@author: strahl
"""

class Line:
    point1: {'x': 0, 'y': 0}
    point2: {'x': 0, 'y': 0}

    def __init__(self, x1, y1, x2, y2):
        self.point1 =  {'x': x1, 'y': y1}
        self.point2 = {'x': x2, 'y': y2}

    def __str__(self):
        return 'Line [A'+str(self.point1)+', B' \
        +str(self.point2)+', direction: ' \
        +str(self.get_direction())+']'

    def __repr__(self):
        return self.__str__();

    def get_direction(self):
        if self.point1['x'] == self.point2['x']:
            return 'vertical'
        if self.point1['y'] == self.point2['y']:
            return 'horizontal'
        return 'invalid'

    def sort_points(self):
        if (self.point1['x'] > self.point2['x']) \
        or (self.point1['y'] > self.point2['y']):
            self.point1, self.point2 = self.point2, self.point1

def get_wire(path):
    path = path.split(',')
    wire = []
    posX = 0
    posY = 0
    for way in path:
        line = Line(posX, posY, 0, 0)
        distance = int(way[1:])
        if way[0] == 'R':
            posX += distance
        elif way[0] == 'L':
            posX -= distance
        elif way[0] == 'U':
            posY += distance
        else:
            posY -= distance
        line.point2 = {'x': posX, 'y': posY}
        wire.append(line)
    return wire

def get_intersect(line1, line2):
    line1.sort_points()
    line2.sort_points()
    if (line2.point1['x'] < line1.point1['x'] < line2.point2['x']) \
    and (line1.point1['y'] < line2.point1['y'] < line1.point2['y']):
        return {'x': line1.point1['x'], 'y': line2.point1['y']}
    if (line1.point1['x'] < line2.point1['x'] < line1.point2['x']) \
    and (line2.point1['y'] < line1.point1['y'] < line2.point2['y']):
        return {'x': line2.point1['x'], 'y': line1.point1['y']}

fp = open('day03_input.txt')

path1 = fp.readline()
wire1 =get_wire(path1)

path2 = fp.readline()
wire2 =get_wire(path2)

fp.close()

def origo_distance(obj):
    return abs(obj['x']) + abs(obj['y'])

def distance(a, b):
    return abs(a['x']-b['x']) + abs(a['y']-b['y'])

#part one
intersects = []
for line1 in wire1:
    for line2 in wire2:
        if get_intersect(line1, line2) != None:
            intersects.append(get_intersect(line1, line2))

min_intersection = min(intersects, key=origo_distance)
print(min_intersection)
print('Min intesection distance from origin: {}'\
      .format(origo_distance(min_intersection)))

#part two
fp = open('day03_input.txt')

path1 = 'R8,U5,L5,D3'
wire1 =get_wire(path1)

path2 = 'U7,R6,D4,L4'
wire2 =get_wire(path2)

print(wire1)
print(wire2)
total_steps1 = 0

for idx in range(len(wire1)):
    if wire1[idx].point1['x'] == min_intersection['x'] \
    and wire1[idx].point1['y'] <= min_intersection['y'] <=  wire1[idx].point2['y']:
        total_steps1 += distance(wire1[idx].point1, min_intersection)
        break
    if wire1[idx].point1['y'] == min_intersection['y'] \
    and wire1[idx].point1['x'] <= min_intersection['x'] <=  wire1[idx].point2['x']:
        total_steps1 += distance(wire1[idx].point1, min_intersection)
        break
    total_steps1 += distance(wire1[idx].point1, wire1[idx].point2)
print(total_steps1)

total_steps2 = 0
for idx in range(len(wire1)):
    if wire2[idx].point1['x'] == min_intersection['x'] \
    and wire2[idx].point1['y'] <= min_intersection['y'] <=  wire2[idx].point2['y']:
        total_steps2 += distance(wire2[idx].point1, min_intersection)
        break
    if wire2[idx].point1['y'] == min_intersection['y'] \
    and wire2[idx].point1['x'] <= min_intersection['x'] <=  wire2[idx].point2['x']:
        total_steps2 += distance(wire2[idx].point1, min_intersection)
        break
    total_steps2 += distance(wire1[idx].point1, wire1[idx].point2)
print(total_steps2)
