# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 02:07:52 2016

@author: Amirali Shahinpour

Purpose: Rotate a N x N array 90 degree
"""

import copy
def arrayRotator(A):
    B = copy.deepcopy(A)
    max_x = len(A)-1
    print(A[0][0])
    for k in range(0,max_x+1):
        for l in range(max_x,-1,-1):
            B[k][max_x-l] = A[l][k]
    return(B)


A = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
#A = [[0,1,2],[3,4,5],[6,7,8]]
B = arrayRotator(A)
print(B)