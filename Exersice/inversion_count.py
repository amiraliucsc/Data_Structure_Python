# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 11:02:41 2016

@author: Amirali

counting Inversion, ex: [1,2,3,4]  if i < j but A[i] > A[j]
"""

import numpy as np
import scipy
from matplotlib import pyplot as plt
import timeit

#Brute Force Inversion Counting
def brute_count(A):
    count=0
    for i in range(0,len(A)):
        for j in range(i,len(A)):
            if A[i]>A[j]:
                count+=1
    return count


#Mergesort_and_count helper function:
def merge_and_count(L,R):
    result=[]
    count=0
    while len(L) > 0 and len(R) > 0:
        if L[0] <= R[0]:
            result.append(L[0])
            L=L[1:]
        else:
            result.append(R[0])
            R=R[1:]
            count+=len(L)
    while len(L) > 0:
        result.append(L[0])
        L=L[1:]
    while len(R) > 0:
        result.append(R[0])
        R=R[1:]
    return (result,count)


#Mergesort function
#It also counts for inversions
def mergesort_and_count(A):
    if len(A) <= 1:
        return(A,0)
    else:
        middle = len(A) // 2
        left = A[:middle]
        right = A[middle:]
        
        left_count=0
        right_count=0
        split_count=0
        
        (left,left_count)   = mergesort_and_count(left)
        (right,right_count) = mergesort_and_count(right)
        (result,split_count) = merge_and_count(left,right)
        total_count = left_count + right_count + split_count         
        return (result,total_count)



print(mergesort_and_count([9,8,0,1]))

#Testing the performance and comparing the bruteforce VS mergesort_count
'''
#Timing
brute_results=[]
merge_results=[]

input_sizes= range(0,1000,15)

for n in input_sizes:
    A = np.arange(n)
    A = np.random.permutation(A)
    t_brute = timeit.Timer(lambda: brute_count(A))
    t_merge = timeit.Timer(lambda: mergesort_and_count(A))
    result_brute = scipy.mean(t_brute.repeat(repeat=3,number=1))
    result_merge = scipy.mean(t_merge.repeat(repeat=3,number=1))
    brute_results.append(result_brute)
    merge_results.append(result_merge)
    
#Plotting
plt.figure()
plt.plot(input_sizes,brute_results,label="Brute Force")
plt.plot(input_sizes,merge_results,label="Merge Sort")

plt.title('Counting Number of Inversions')
plt.xlabel('Size of input')
plt.ylabel('Time to count (s)')
plt.legend()

plt.show()
'''