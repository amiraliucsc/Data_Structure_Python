"""
Created on Thu Jan 14 12:21:57 2016

@author: Amirali Shahinpour

Name: Insertaion Sort
"""

import matplotlib.pyplot as plt
import numpy as np
import timeit
from timeit import Timer

def insertSort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i >= 0 and key < A[i]:
            A[i+1] = A[i]
            i-=1
        A[i+1] = key
        
        
        
        
        
sizeArray = np.array([])
timeArrayWorst = np.array([])
timeArrayBest = np.array([])
start_time = time.time()
for i in range(1,10000):
    A = np.array(np.random.randint(0,50,i))
    A = np.sort(A)
    start = 0
    end = len(A)-1
    t = Timer(lambda: insertSort(A))
    execTimeBest = t.timeit(number = 1)
    timeArrayBest = np.append(timeArrayBest,execTimeBest)
    # Worts case
    
    A = np.array(np.random.randint(0,50,i))
    A = np.sort(A)
    A = A[::-1]
    start = 0
    end = len(A)-1
    t = Timer(lambda: insertSort(A))
    execTimeWorst = t.timeit(number = 1)
    timeArrayWorst = np.append(timeArrayWorst,execTimeWorst)
    sizeArray = np.append(sizeArray, end)
plt.plot(sizeArray,timeArrayBest)
plt.plot(sizeArray,timeArrayWorst)
plt.show()        
print("Runtime = ", (time.time() - start_time)," Sec")
