# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:56:39 2019

@author: strahl
"""

def run_program(operand1, operand2, intcode):
    intcode[1] = operand1
    intcode[2] = operand2
    for ip in range(0, len(intcode)-4, 4):
        opcode = intcode[ip]
        operand1 = intcode[intcode[ip+1]]
        operand2 = intcode[intcode[ip+2]]
        output_pos = intcode[ip+3]
        if opcode == 1:
            intcode[output_pos] = operand1 + operand2
        elif opcode == 2:
            intcode[output_pos] = operand1 * operand2
        elif opcode == 99:
            break
        else:
            print('Oops something went wrong!')
    return intcode[0]

#part 1:
intcode = open('day02_input.txt').read().split(',')
intcode = [int(x) for x in intcode]
print(intcode)
print(run_program(12, 2, intcode))

#part 2: https://dev.to/aspittel/comment/id8j
for i in range(100):
    for j in range(100):
        intcode = open('day02_input.txt').read().split(',')
        intcode = [int(x) for x in intcode]
        if run_program(i, j, intcode) == 19690720:
            print(100*i+j)
