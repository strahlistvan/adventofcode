# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 14:39:46 2019

@author: strahl
"""

orbit_input = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
"""

# Uncomment this line to use the real input
#orbit_input = open('day06_input.txt').read()

orbit_input = [row.split(')') for row in orbit_input.splitlines()]

from anytree import Node, RenderTree

#Build the tree structure with anytree library
node_dict = {}

node_dict['COM'] = Node('COM')
#ugly brute-force method to find keys
while len(orbit_input) > 0:
    for orbit_data in orbit_input:
        if orbit_data[0] in node_dict.keys():
            node_dict[orbit_data[1]] = Node(orbit_data[1], parent=node_dict[orbit_data[0]])
            orbit_input.remove(orbit_data)

#Visualize the orbiting map
print(RenderTree(node_dict['COM']))

#Sum of the direct and indirect orbits = sum of "depths" of all nodes
sum_orbits = 0
for key, node in node_dict.items():
    sum_orbits += node.depth

print('Total orbits in the map ' + str(sum_orbits))

#part 2
# Minimum number of transfers - step up to the closest common orbiting object, then step down
def get_closest_common_anchestor(node_src, node_dest):
    max_depth = 0
    for n in node_src.anchestors:
        for m in node_dest.anchestors:
            if n == m and n.depth > max_depth:
                max_depth = n.depth
                common_anchestor = n
    return common_anchestor

node_src  = node_dict['YOU']
node_dest = node_dict['SAN']

node_cca = get_closest_common_anchestor(node_src, node_dest)

steps_up = node_src.depth - node_cca.depth - 1
steps_down = node_dest.depth - node_cca.depth -1

print('Total orbital transfers required' + str(steps_up + steps_down))

