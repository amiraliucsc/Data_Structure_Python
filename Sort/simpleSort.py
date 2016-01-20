# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 00:53:32 2016

@author: Amirali
"""

A = [20,50,10,40]

def doSort(Arr):
    found = False
    for i in range(0,len(Arr)):
        j = i
        minVal = A[i]
        for j in range(j,len(Arr)):
            if A[j] < minVal:
                minVal = A[j]
                index = j
                found = True
        if found:
            temp = A[i]
            A[i] = minVal
            A[index] = temp
        fount = False
        
doSort(A)
print(A)
