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

    def set_lower_upper(self):
        if (self.point1['x'] > self.point2['x']) \
        or (self.point1['y'] > self.point2['y']):
            self.lower, self.upper = self.point2, self.point1
        else:
            self.lower, self.upper = self.point1, self.point2

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
    line1.set_lower_upper()
    line2.set_lower_upper()
    if (line2.lower['x'] < line1.lower['x'] < line2.upper['x']) \
    and (line1.lower['y'] < line2.lower['y'] < line1.upper['y']):
        return {'x': line1.lower['x'], 'y': line2.lower['y']}
    if (line1.lower['x'] < line2.lower['x'] < line1.upper['x']) \
    and (line2.lower['y'] < line1.lower['y'] < line2.upper['y']):
        return {'x': line2.lower['x'], 'y': line1.upper['y']}

with open('day03_input.txt') as fp:
    path1 = fp.readline()
    wire1 =get_wire(path1)
    path2 = fp.readline()
    wire2 =get_wire(path2)

def origo_distance(obj):
    return abs(obj['x']) + abs(obj['y'])

def get_intersects(wire1, wire2):
    intersects = []
    for line1 in wire1:
        for line2 in wire2:
            if get_intersect(line1, line2) != None:
                intersects.append(get_intersect(line1, line2))
    return intersects

#part one
intersects = get_intersects(wire1, wire2)

min_intersection = min(intersects, key=origo_distance)
print(min_intersection)
print('Min intesection distance from central port (origin): {}'\
      .format(origo_distance(min_intersection)))

#part two -Find wire intersection with minimal total steps
def calc_steps_in_wire(wire, isect):
    steps = 0
    for line in wire:
        if isect['x'] == line.point1['x'] \
        and ( line.point1['y'] < isect['y'] < line.point2['y'] \
             or line.point2['y'] < isect['y'] < line.point1['y'] ) :
            steps += abs(isect['y'] - line.point1['y'])
            break
        elif isect['y'] == line.point1['y'] \
        and ( line.point1['x'] < isect['x'] < line.point2['x']
             or line.point2['x'] < isect['x'] < line.point1['x'] ):
            steps += abs(isect['x'] - line.point1['x'] )
            break
        elif line.point1['x'] == line.point2['x']:
            steps += abs(line.point2['y'] - line.point1['y'])
        else:
            steps += abs(line.point2['x'] - line.point1['x'])
    return steps

all_steps = []
for isect in intersects:
    steps1 = calc_steps_in_wire(wire1, isect)
    steps2 = calc_steps_in_wire(wire2, isect)
    all_steps.append(steps1 + steps2)

print('Intersection with fewest total steps in wires from the central port: {}'.format(min(all_steps)))