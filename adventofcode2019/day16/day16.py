# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 21:46:39 2019

@author: strahl
"""


def apply_pattern(input_signal, base_pattern):
    digit = 0
    pattern_idx = 1 #skip the very first value
    for sign in input_signal:
            digit += sign*base_pattern[pattern_idx]
            pattern_idx= (pattern_idx + 1) % len(base_pattern)
    digit = abs(digit)%10
    return digit

def get_pattern(base_pattern, num):
    new_base_pattern = []
    for p in base_pattern:
        new_base_pattern.extend([p]*num)
    return new_base_pattern

def fft_cycle(input_signal, base_pattern):
    result = ''
    for num in range(1, len(input_signal)+1):
        pattern = get_pattern(base_pattern, num)
        digit = apply_pattern(input_signal, pattern)
        result += str(digit)
    return result

base_pattern = [0,1,0,-1]
input_signal = '59708372326282850478374632294363143285591907230244898069506559289353324363446827480040836943068215774680673708005813752468017892971245448103168634442773462686566173338029941559688604621181240586891859988614902179556407022792661948523370366667688937217081165148397649462617248164167011250975576380324668693910824497627133242485090976104918375531998433324622853428842410855024093891994449937031688743195134239353469076295752542683739823044981442437538627404276327027998857400463920633633578266795454389967583600019852126383407785643022367809199144154166725123539386550399024919155708875622641704428963905767166129198009532884347151391845112189952083025' # '12345678'

for n in range(100):
    input_signal = [int(x) for x in input_signal]
    input_signal = fft_cycle(input_signal, base_pattern)
print(input_signal)
