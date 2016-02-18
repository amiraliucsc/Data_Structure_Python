# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 12:46:51 2016

@author: Amirali

Return the number of occurance of x in factorization of n. Example n=24 , x=2
must return 3 since 24 = 2^3*3   or n=25,5 must return 2 since 25 = 5^2
"""

def two_count(n,x):
    stop = False
    rem = 0
    div = 2
    count = 0
    countFor = x
    while(not stop):
        rem = n % div
        if (rem > 0):
            div+=1
        else:
            if div == countFor:
                count+=1
            n = (n // div)
            div = 2
        if (n == 1):
            stop = True
    return count
    
print(two_count(24,2))