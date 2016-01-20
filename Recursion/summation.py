# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 01:37:31 2016

@author: Amirali
"""
import numpy as np

def doSum(mylist):
    sum = mylist[0]
    global n
    n+=1
    print(n)
    if len(mylist) == 1:
        return sum
    else:
        return sum + doSum(mylist[1:])
    
    
n = 0   
A = np.random.randint(0,100,2000)
print( doSum(A))