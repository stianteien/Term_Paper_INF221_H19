# -*- coding: utf-8 -*-

"""
Made the partition and quick_sort functions from the pseudocodes.
"""


def partition(a, p, r):
    x = a[r]
    i = p - 1
    
    for j in range(p, r):  # Adding 1 to adjust to Python indexing
        if a[j] <= x:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def quick_sort(a, p=0, r=None):
    if(r==None):
        r = len(a)-1
    if p < r:
        q = partition(a, p, r)
        quick_sort(a, p, q - 1)
        quick_sort(a, q + 1, r)