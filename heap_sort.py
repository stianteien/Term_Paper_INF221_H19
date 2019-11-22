# -*- coding: utf-8 -*-

"""
This code is copied from
https://brilliant.org/wiki/heap-sort/
"""

def max_heapify(arr, heap_size, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, heap_size, largest)

def build_heap(arr):
    heap_size = len(arr)
    for i in range (int(heap_size/2),-1,-1):
        max_heapify(arr,heap_size, i)

def heap_sort(arr):
    heap_size = len(arr)
    build_heap(arr)
    #print A #uncomment this print to see the heap it builds
    for i in range(heap_size-1,0,-1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_size -= 1
        max_heapify(arr, heap_size, 0)
