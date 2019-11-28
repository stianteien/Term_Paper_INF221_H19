# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 13:20:55 2019

@author: Stian
"""

import time_sort
import make_problem
import merge_sort
import heap_sort
import quick_sort
import math
import datetime
import numpy as np
import matplotlib.pyplot as plt
import copy




def make_graph(size, time, c1=1, c2=1, loga=False, title="Benchmark"): 
    #size = [10**i for i in size]
    fig = plt.figure(figsize=(3, 3))
    ax = fig.add_axes([0.16, 0.15, 0.83, 0.75])
    line_sorted, = ax.plot(size,time[0], 'o-', label="Sorted", linewidth=1, markersize=3)
    line_reversed, = ax.plot(size,time[1], 'o-', label="Reversed", linewidth=1, markersize=3)
    line_nearly, = ax.plot(size,time[2], 'o-', label="Nearly Sorted", linewidth=1, markersize=3)
    line_random, = ax.plot(size,time[3], 'o-', label="Random", linewidth=1, markersize=3)
    
    
    if 'Quick Sort' in title:
        upper = [(i**2)*c1 for i in size]
        line_upperbound, = ax.plot(size, upper, '--', linewidth=1.5, color="black")
        lower = [(i * math.log(i))*c2 for i in size]
        line_lowerbound, = ax.plot(size, lower, '--', linewidth=1.5, color='grey')
        
    elif 'Merge Sort' in title:
        upper = [(i * math.log(i))*c1 for i in size]
        line_upperbound, = ax.plot(size, upper, '--', linewidth=1, color="black")
        lower = [(i * math.log(i))*c2 for i in size]
        line_lowerbound, = ax.plot(size, lower, '--', linewidth=1, color='grey')
        
    elif 'Heap Sort' in title:
        upper = [(i * math.log(i))*c1 for i in size]
        line_upperbound, = ax.plot(size, upper, '--', linewidth=1, color="black")
        
    
    
    
    ax.legend(handles=[line_sorted, line_reversed, line_nearly, line_random],
               loc='best', prop={'size': 7})
    
    #ax.locator_params(axis='x', nbins=4)
    ax.set_xlabel('Array size', fontsize=8)
    ax.set_ylabel('Runtime [s]', fontsize=8)
    
    #ax.set_xticklabels(ax.get_xticklabels(), fontsize=10)
    ax.tick_params(axis="x", labelsize=6)
    ax.tick_params(axis="y", labelsize=6)

    if loga == True:
        plt.xscale('log')
        plt.yscale('log')
        
    plt.title(title)
    
def make_logaritmal(data):
    min_data = copy.deepcopy(data)
    for i,value in enumerate(min_data):
        for j, item in enumerate(value):
            min_data[i][j] = math.log2(item[0]*100000)
        
    return min_data

def make_two_desimals(data):
    if 'e' in data:
        a = data.split('e')
        a[0] = a[0][0:4]
        return 'e'.join(a)
        
    if len(data) > 7:
        if(float(data[0:7])==0):
            return '0.00001'
        
        return data[0:7]
    
    return data

def make_table(merge, heap, quick, numpy, sort):
    bugg = "\\"
    
    
    for i, value in enumerate(merge[1][0]):
        info = bugg[0]+'textit{' + (str(merge[0][i])) + '} & '
        info += make_two_desimals(str(merge[1][3][i][0])) + ' & '
        info += make_two_desimals(str(heap[1][3][i][0])) + ' & '
        try:
            info += make_two_desimals(str(quick[1][3][i][0])) + ' & '
        except:
            info += '- & '
        info += make_two_desimals(str(numpy[1][3][i][0]))+ '& '
        info += make_two_desimals(str(sort[1][3][i][0]))+ ' \\\ '
            
        print(info)

    


def simualtion(function, array):
    return time_sort.time_sort(function, data=array, num_reps=1)

def multi_simulations(function, n):
    times = [[], [], [], []]
    problemsize = []
    for i in range(1,n+1):
        a = create_data_sorted(i)
        b = create_data_reversed(i)
        c = create_data_nearly_sorted(i)
        d = create_data_random(i)
        
        problemsize.append(len(a))
        times[0].append (list(simualtion(function, a)))
        logg('  -  Ferdig med array på str ' + str(2**i) + ' sorted')
        times[1].append (list(simualtion(function, b)))
        logg('  -  Ferdig med array på str ' + str(2**i) + ' reversed')
        times[2].append (list(simualtion(function, c)))
        logg('  -  Ferdig med array på str ' + str(2**i) + ' nearly sorted')
        times[3].append (list(simualtion(function, d)))
        logg('  -  Ferdig med array på str ' + str(2**i)  +' random ' + '(' + function.__name__ + ',i er nå: '+ str(i) +')')
    
    return problemsize, times

def logg(text):
    print(datetime.datetime.now(),text)

def create_data_sorted(n):
    return make_problem.already_sorted(n)

def create_data_reversed(n):
    return make_problem.reverse_sorted(n)

def create_data_nearly_sorted(n):
    return make_problem.nearly_sorted(n)

def create_data_random(n):
    return make_problem.random_sorted(n)


if __name__ == "__main__":
    
    # Mergesort
    merge_sort = multi_simulations(merge_sort.merge_sort, 20)
    make_graph(merge_sort[0], (merge_sort[1]), c1=11.39*10**-7, c2=5.39*10**-7, title='Merge Sort')
    plt.savefig('graphs/merge_sort_image.pdf')
    make_graph(merge_sort[0], (merge_sort[1]), c1=11.39*10**-7, c2=5.39*10**-7, loga=True, title='Merge Sort Logarithmic')
    plt.savefig('graphs/merge_sort_log_image.pdf')
    
    # Heapsort
    heap_sort = multi_simulations(heap_sort.heap_sort, 20)
    make_graph(heap_sort[0], (heap_sort[1]), c1=10.53*10**-7, c2=6.53*10**-7, title='Heap Sort')
    plt.savefig('graphs/heap_sort_image.pdf')
    make_graph(heap_sort[0], (heap_sort[1]), c1=10.53*10**-7, c2=6.53*10**-7, loga=True, title='Heap Sort Logarithmic')
    plt.savefig('graphs/heap_sort_log_image.pdf')
    
    # Quicksort
    quick_sort = multi_simulations(quick_sort.quick_sort, 10)
    make_graph(quick_sort[0], (quick_sort[1]), c1=1.2*10**-7, c2=1.86*10**-7, title='Quick Sort')
    plt.savefig('graphs/quick_sort_image.pdf')
    make_graph(quick_sort[0], (quick_sort[1]), c1=1.2*10**-7, c2=1.86*10**-7, loga=True, title='Quick Sort Logarithmic')
    plt.savefig('graphs/quick_sort_log_image.pdf')
    
    # Numpysort 
    numpy_sort = multi_simulations(np.sort, 20)
    make_graph(numpy_sort[0], (numpy_sort[1]), title='Numpy Sort')
    plt.savefig('graphs/numpy_sort_image.pdf')
    make_graph(numpy_sort[0], (numpy_sort[1]), loga=True, title='Numpy Sort Logarithmic')
    plt.savefig('graphs/numpy_sort_log_image.pdf')
    
    # Sorted sort
    sorted_sort = multi_simulations(sorted, 20)
    make_graph(sorted_sort[0],(sorted_sort[1]), title='Sorted Sort')
    plt.savefig('graphs/sorted_sort_image.pdf')
    make_graph(sorted_sort[0], (sorted_sort[1]), loga=True, title='Sorted Sort Logarithmic')
    plt.savefig('graphs/sorted_sort_log_image.pdf')
    
    #make_table(merge_sort, heap_sort, quick_sort, numpy_sort, sorted_sort)
    
    
