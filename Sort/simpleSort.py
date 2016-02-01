# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 00:53:32 2016

@author: Amirali
"""

A = [20,50,10,40]

def minSort(A):
    for i in range(0,len(A)):
        found = False
        min = A[i]
        for j in range(i,len(A)):
            if A[j] < min:
                min = A[j]
                index = j
                found = True
        if found:
            A[index] = A[i]
            A[i] = min
    return(A)

print( minSort(A) )
