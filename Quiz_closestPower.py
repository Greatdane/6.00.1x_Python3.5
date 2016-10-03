# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:34:40 2016

@author: davidwilson
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    exponent = 0 # start at 0, and work up.    
    while num > exponent:
        if abs(num - (base ** exponent)) > abs(num - (base ** (exponent + 1))):
            exponent += 1
            #print("trying " + str(exponent))
        else:
            return exponent

print(closest_power(3,12)) #returns 2

print(closest_power(4,12)) #returns 2

print(closest_power(4,1)) #returns 0