# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 21:43:47 2016

@author: davidwilson
"""

#While loops
num = 2
while num <= 10:
    print(num)
    num += 2
print("Goodbye!")

num = 10
print("Hello!")
while num >= 2:
    print(num)
    num -= 2
    
end = 6
num = 1
result = 0
while num <= end:
    result += num    
    num += 1
print(result)

#For loops

for x in range(2, 11, 2):
    print(x)
print("Goodbye!")
    
print("Hello!")
for x in range(10, 1, -2):
    print(x)
    
end = 6
result = 0
for x in range(1, end+1):
    result += x
print(result)