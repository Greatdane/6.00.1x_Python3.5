# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 14:00:41 2016

@author: davidwilson
"""

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    for l in range(0, len(L)):
       L[l].reverse()
    L.reverse()
    
# For example
L = [[1, 2], [3, 4], [5, 6, 7]]
# L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]

print(deep_reverse(L))
print(L)
# L = [[7, 6, 5], [4, 3], [2, 1]]