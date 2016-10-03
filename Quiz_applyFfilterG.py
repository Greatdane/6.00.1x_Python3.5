# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:05:38 2016

@author: davidwilson
"""
# INCORRECT - (18/20 points)


def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    LCopy = L[:]    
    for i in LCopy:
        if g(f(i)) != True:
            L.remove(i)
    L.sort()    
    if L == []:
        return -1
    else:
        return L[-1]
        
# For example, the following functions, f, g, and test code:
        
def f(i):
    return i + 2
def g(i):
    return i > 5

L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f, g))
print(L)

# Should print;
# 6
# [5, 6]