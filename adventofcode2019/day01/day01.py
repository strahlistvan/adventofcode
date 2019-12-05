# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 16:12:52 2019

@author: strahl
"""

numbers = open('day01_input.txt').read().splitlines()

def get_module_fuel_rec(mass):
    sum_fuel = 0
    mass = int(mass)//3-2
    while (mass > 0):
        sum_fuel += mass
        mass = mass//3-2
    return sum_fuel

def get_module_fuel(mass):
    return int(int(mass)//3-2)

sum_fuel = 0 
sum_fuel_of_fuels = 0
for mass in numbers:
    module_fuel = int(mass)//3-2
    sum_fuel += module_fuel;
    sum_fuel_of_fuels += get_module_fuel_rec(mass)


print(sum_fuel)
print(sum_fuel_of_fuels)

print(sum([get_module_fuel(mass) for mass in  open('day01_input.txt').read().splitlines()]))
print(sum([get_module_fuel_rec(mass) for mass in  open('day01_input.txt').read().splitlines()]))
