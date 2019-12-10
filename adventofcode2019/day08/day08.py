# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 12:54:55 2019

@author: strahl
"""

image_width = 25
image_height = 6
fp = open('day08_input.txt')
image_data = fp.read() # '123456789012'
fp.close()

def get_layers(image_data):
    layer = []
    layer_list = []
    for i in range(0, len(image_data), image_width):
        row = image_data[i:i+image_width]
        if len(layer) == image_height:
            layer_list.append(layer)
            layer = []
        layer.append(row)
    layer_list.append(layer)
    return layer_list

def get_layer_with_fewest_zeros(layer_list):
    min_sum_layer = sum([row.count('0') for row in layer_list[0]])
    min_layer = layer_list[0]
    for layer in layer_list:
        sum_layer = sum([row.count('0') for row in layer])
        if sum_layer < int(min_sum_layer):
            min_sum_layer = sum_layer
            min_layer = layer
    return min_layer


layer_list = get_layers(image_data)
print(layer_list)

min_layer = get_layer_with_fewest_zeros(layer_list)
print(min_layer)
no_1 = sum([row.count('1') for row in min_layer])
no_2 = sum([row.count('2') for row in min_layer])

print('Result: ' + str(no_1*no_2))

#Decoding layers
decoded_image = [['2']*image_width for i in range(image_height)]
for row in range(image_height):
    for col in range(image_width):
        for depth in range(len(layer_list)):
            if layer_list[depth][row][col] != '2':
                decoded_image[row][col] = layer_list[depth][row][col]
                break

#Print decoded image
for row in range(image_height):
    for col in range(image_width):
        if decoded_image[row][col] == '1':
            print('#', end='',)
        else:
            print(' ', end='')
    print('')