# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 13:22:07 2019

@author: strahl
"""

moons = [ {'position': {'x': 6, 'y': -2, 'z': -7}, 'velocity': {'x': 0, 'y': 0, 'z': 0}},
            {'position': {'x': -6, 'y': -7, 'z': -4}, 'velocity': {'x': 0, 'y': 0, 'z': 0}},
            {'position': {'x': -9, 'y': 11, 'z': 0}, 'velocity': {'x': 0, 'y': 0, 'z': 0}},
            {'position': {'x': -3, 'y': -4, 'z': 6}, 'velocity': {'x': 0, 'y': 0, 'z': 0}} ];

def apply_gravity(moon1, moon2):
    for dim in ['x', 'y', 'z']:
        if moon1['position'][dim] < moon2['position'][dim]:
            moon1['velocity'][dim] += 1
            moon2['velocity'][dim] -= 1
        elif moon1['position'][dim] > moon2['position'][dim]:
            moon1['velocity'][dim] -= 1
            moon2['velocity'][dim] += 1

def apply_velocity(moon):
    for dim in ['x', 'y', 'z']:
        moon['position'][dim] += moon['velocity'][dim]

def potential_energy(moon):
    return abs(moon['position']['x']) + abs(moon['position']['y']) + abs(moon['position']['z'])

def kinetic_energy(moon):
    return abs(moon['velocity']['x']) + abs(moon['velocity']['y']) + abs(moon['velocity']['z'])

def apply_step(moons):
    for m1 in range(len(moons)):
        for m2 in range(m1+1, len(moons)):
            apply_gravity(moons[m1], moons[m2])
    for m in moons:
        apply_velocity(m)
    return moons

# part 1 - what is the total energy after 1000 steps?
for time_steps in range(1000):
    moons = apply_step(moons)

total_energy = 0
for m in moons:
    pot = potential_energy(m)
    kin = kinetic_energy(m)
    total_energy += pot*kin
    print(m)
    print('{}*{}={}'.format(pot, kin, pot*kin))
print('Sum of total energy: ' + str(total_energy))

#part 2 - TODO: make it more efficient... but how?
moons = [ {'position': {'x': 6, 'y': -2, 'z': -7}, 'velocity': {'x': 0, 'y': 0, 'z': 0}},
            {'position': {'x': -6, 'y': -7, 'z': -4}, 'velocity': {'x': 0, 'y': 0, 'z': 0}},
            {'position': {'x': -9, 'y': 11, 'z': 0}, 'velocity': {'x': 0, 'y': 0, 'z': 0}},
            {'position': {'x': -3, 'y': -4, 'z': 6}, 'velocity': {'x': 0, 'y': 0, 'z': 0}} ];

def is_original_state(moons):
    if moons[0]['position'] != {'x': 6, 'y': -2, 'z': -7} \
    or moons[1]['position'] != {'x': -6, 'y': -7, 'z': -4} \
    or moons[2]['position'] != {'x': -9, 'y': 11, 'z': 0} \
    or moons[3]['position'] != {'x': -3, 'y': -4, 'z': 6}:
        return False
    if moons[0]['velocity'] != {'x': 0, 'y': 0, 'z': 0} \
    or moons[1]['velocity'] != {'x': 0, 'y': 0, 'z': 0} \
    or moons[2]['velocity'] != {'x': 0, 'y': 0, 'z': 0} \
    or moons[3]['velocity'] != {'x': 0, 'y': 0, 'z': 0}:
        return False
    return True

moons = apply_step(moons)
steps = 1
while is_original_state(moons) == False:
    moons = apply_step(moons)
    steps += 1
print(steps)