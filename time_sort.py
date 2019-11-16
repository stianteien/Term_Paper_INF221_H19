# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 12:28:15 2019

@author: Stian
"""

import timeit
import numpy as np
import copy


def time_sort(sort_func, data, num_reps=1):
    """
    Returns times for repeated execution of sort_func(data).
    
    Automatically selects number of loops so execution takes
    at least 0.2 s.
    
    :param sort_func: sorting function to test
    :param data: data to sort
    :param num_reps: number of experiment repetitions
    """
    
    # Create Timer object; only objects named in globals are accessible 
    # to statement being timed
    timer = timeit.Timer('s_func(c_func(o_data))',
                         globals={'s_func': sort_func, 
                                  'c_func': copy.copy,
                                  'o_data': data})
    
    # Find out how many loops we need to run for > 0.2 s
    n_loops, t = timer.autorange()
    
    # Perform n_loops for each of num_reps repeats
    return np.array(timer.repeat(number=n_loops, repeat=num_reps)) / n_loops

