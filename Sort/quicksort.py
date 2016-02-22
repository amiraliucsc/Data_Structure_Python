"""
Created on Wed Jan 27 00:27:35 2016

@author: Amirali Shahinpour

Implementation of Quick Sort
"""

##Quick Sort

import random

def quickSort(A,start,end):
    if start < end:
        key = partition(A, start,end)
        quickSort(A, start, key-1)
        quickSort(A, key+1, end)
        return A
    
    
def partition(A, start, end):
    rand = random.randint(start,end)
    temp = A[rand]
    A[rand] = A[end]
    A[end] = temp
    piviot = A[end]
    i = start -1
    for j in range( start, end):
        if A[j] <= piviot:
            i = i + 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp = A[i+1]
    A[i+1] = A[end]
    A[end] = temp
    return (i+1)
    
    
    
A=[8,5,0,9,10,41,1,84,21,7,10]
print(quickSort(A , 0, len(A)-1) )
