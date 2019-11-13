# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 13:23:07 2019

@author: Stian
"""

import random
import math

def already_sorted(n):
    return [i for i in range(2**n)]

def nearly_sorted(n):
    array = already_sorted(n)
    nearly_sorted_array = []
    split = math.ceil((2**n)/(n**2))
    for i in range(0, len(array), split):
        temp_array = list(array[i:i+split])
        random.shuffle(temp_array)
        nearly_sorted_array += (temp_array)
        
    return nearly_sorted_array

def random_sorted(n):
    return random.shuffle(already_sorted(n))

def reverse_sorted(n):
    return [i for i in range(2**n, 0, -1)]

