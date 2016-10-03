# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 19:47:10 2016

@author: davidwilson
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    num = 0
    newTuple = ()
    for x in aTup:
        if num % 2 == 0:
            newTuple += (x, )
        else:
            pass
        num += 1
    return newTuple
    
aTup = ('I', 'am', 'a', 'test', 'tuple')
print(oddTuples(aTup))       
