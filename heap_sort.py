# -*- coding: utf-8 -*-

""" FÅR IKKE TIL...
"""

from math import floor


def max_heapify(a, i, heap_size):
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l <= heap_size and a[l] > a[i]:
        largest = l
    else:
        largest = i
        
    if r <= heap_size and a[r] > a[largest]:
        largest = r
    
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, largest, heap_size)


def build_max_heap(a):
    heap_size = len(a)
    n = floor(len(a)/2)
    for i in range(n - 1, 0, -1): # Edited Index
        print(i)
        max_heapify(a, i, heap_size)
 
    
def heap_sort(a):
    heap_size = len(a)
    build_max_heap(a)

    for i in range(len(a) - 1, 0, -1): # Edited index
        print(i)
        a[1], a[i] = a[i], a[1]
        heap_size = heap_size - 1
        max_heapify(a, 1, heap_size)


a = [4, 2, 6, 5, 9, 10, 1]

heap_sort(a)
print(a)





# Python program for implementation of heap Sort 
  
# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 
  
# Driver code to test above 
arr = [4, 2, 6, 5, 9, 10, 1]
heapSort(arr) 
n = len(arr) 
print ("Sorted array is") 
for i in range(n): 
    print ("%d" %arr[i]), 
# This code is contributed by Mohit Kumra 
    
    