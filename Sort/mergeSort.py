"""
Created on Thu Jan 12 11:25:32 2016

@author: Amirali Shahinpour

Name: Merge Sort
"""

import numpy as np
import timeit
from timeit import Timer
import time
import matplotlib.pyplot as plt
import scipy
def mergeSort(A,p,q):
    if p < q:
        mid = (p+q) // 2
        mergeSort(A,p,mid)
        mergeSort(A,mid+1,q)
        merge(A,p,mid,q)

def merge(A,s1,e1,e2):
    k = s1
    s2 = e1+1
    L = np.copy(A[s1:e1+1])
    R = np.copy(A[s2:e2+1])
    i = 0
    j = 0
    while(i < len(L) and j < len(R)):
        if (L[i] > R[j]):
            A[k] = R[j]
            j+=1
        else:
            A[k] = L[i]
            i+=1
        k+=1
    # copy the rest of L or R into A    
    while i < len(L):
        A[k] = L[i]
        i+=1
        k+=1
    while j < len(R):    
        A[k] = R[j]
        j+=1
        k+=1


start_time= time.time()
sizeArray = np.array([])
timeArrayBest = np.array([])
timeArrayWorst = np.array([])
# Testing the worst case and base case (to Proof there is no different)
for i in range(1,200):
    A = np.array(np.random.randint(0,50,i))
    A = np.sort(A)
    start = 0
    end = len(A)-1
    t = Timer(lambda: mergeSort(A,start,end))
    execTimeBest = scipy.mean(t.repeat(repeat = 10,number = 1))
    timeArrayBest = np.append(timeArrayBest,execTimeBest)    
    
    
    #Worst
    A = np.array(np.random.randint(0,50,i))
    A = np.sort(A)
    A = A[::-1]
    start = 0
    end = len(A)-1
    t = Timer(lambda: mergeSort(A,start,end))
    execTimeWorst = scipy.mean(t.repeat(repeat = 10,number = 1))
    timeArrayWorst = np.append(timeArrayWorst,execTimeWorst)
    sizeArray = np.append(sizeArray, end)
    
fig = plt.figure()
fig.suptitle('Merge Sort', fontsize=14, fontweight='bold')
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
plt.plot(sizeArray,timeArrayBest)
#plt.axis([0,1000,0,0.02])
plt.plot(sizeArray,timeArrayWorst)
plt.show()
print("Runtime = ", (time.time() - start_time)," Sec")