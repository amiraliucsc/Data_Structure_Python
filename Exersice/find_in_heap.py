# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 01:42:48 2016

@author: Amirali Shahinpour

Check if a given min Heap A which contains n numbers and a query element q
contains at lest K elements which are smaller than q and it grows as O(k).
"""
'''
A = Heap
i = index
c = counter
q = query element
k = numbers of elements < q that we are looking for
'''
def findSmallest(A,i,c,q,k): 
    if c == k:
        return True
    if A[i] < q:
        left = ((i+1)*2) - 1
        right = ((i+1)*2)
        c+=1
        return findSmallest(A, left, c , q,k)
        return findSmallest(A, right, c , q,k)
        return False
    else:
        return False
    
    
A=[0,10,20,30,40,22,23,35]
print(findSmallest(A,0,0,15,6))


    

