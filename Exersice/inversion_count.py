# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 11:02:41 2016

@author: Amirali

counting Inversion [1,2,3,4]  if i < j buy A[i] > A[j]
"""

def brute_count(A):
    count = 0
    for i in range(0,len(A)):
        for j in range(i,len(A)):
            if A[i] > A[j]:
                count+=1
    return count
    
    
    
def mergeSort(A):
    if len(A) <= 1:
        return A
    else:
        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]
        left = mergeSort(left)
        right = mergeSort(right)
        res = merge(left,right)
        return res
        
def merge(L,R):
    result = []
    while len(L) > 0 and len(R) > 0:
        if L[0] <= R[0]:
            result.append(L[0])
            L = L[1:]
        else:
            result.append(R[0])
            R = R[1:]
    return result        



B = [3,2,1,4]

print( mergeSort([5,4,10]) )

