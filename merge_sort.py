# -*- coding: utf-8 -*-

"""
Used the Python implementation from Lecture 03, INF221
Hans Ekkehard Plesser NMBU / REALTEK
September 10, 2019
"""


from math import floor


def merge(a, p, q, r):
    n_1 = q - p + 1
    n_2 = r - q

    # Creating empty arrays
    left = [0] * n_1
    right = [0] * n_2

    # Filling the empty arrays
    for i in list(range(n_1)):
        left[i] = a[p + i - 1]

    for j in list(range(n_2)):
        right[j] = a[q + j]

    left.append(float('inf'))
    right.append(float('inf'))

    i = 1 - 1  # Subtract 1 to adjust to Python indexing
    j = 1 - 1  # Subtract 1 to adjust to Python indexing

    for k in list(range(p - 1, r)):  # Subtract 1 to adjust to Python indexing
        if left[i] <= right[j]:
            a[k] = left[i]
            i = i + 1
        else:
            a[k] = right[j]
            j = j + 1


def merge_sort(a, p, r):
    if p < r:
        q = floor((p + r)/2)
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)


# TEST:
a = [4, 2, 6, 5, 9, 10, 1]
p = 1
r = len(a)

merge_sort(a, p, r)
print(a)

