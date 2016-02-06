# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 18:22:25 2016

@author: 
        Amirali Shahinpour  ashahinp@ucsc.edu
        Brian Jones        
        
Description:
    Hadmat(k):                Create a N x N hadmat matrix where N = 2^k
    scaleMat(A,scalar)        Miltiple a N x N Array by a scalar and return the result
    matmult(A,x)              Multiple a N x N Array by a Nd vector in O(N^2)
    hadmatmult(A,x)           Multiple a N x N Hadmat array by a Nd vector in O (log(N))
         
"""

import numpy as np
import math
import timeit
from timeit import Timer
import matplotlib.pyplot as plt
import scipy
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.patches as mpatches
from matplotlib.pyplot import *


## Counter for number of operations
hadCount = 0
matCount = 0

def scaleMat(A, scalar):
    for i in range(len(A)):
        for j in range(len(A)):
            A[i][j] *= scalar
    return A





def hadmat(k):
    global hadCount
    A = np.array([[1]])
    if k >= 1:
        for i in range(k):
            hadCount+=1
            B = np.concatenate((A,A), axis = 1)
            C = np.concatenate((A, np.copy(A) * -1), axis = 1)
            A = np.concatenate((B,C), axis = 0)
    return A





def matmult(A,x):
    global matCount
    if len(A) != len(x):
        return -1
    else:
        product = np.array(x)
        for i in range(len(A)):
            sum = 0
            for j in range(len(A)):
                sum += A[i][j] * x[j]
                matCount += 1
            product[i] = sum
        return(product)




def hadmatmult(A,x):
    global hadCount
    hadCount += 1
    if len(A) == 1:
        return x
    else:
        x1 = np.array(x[:len(x)//2])
        x2 = np.array(x[len(x)//2:])
        decA = hadmat(int(math.log(len(A),2))-1)
        top = hadmatmult(decA,x1)
        bottom = hadmatmult(decA,x2)
        b1 = top + bottom
        b2 = top - bottom
        return(np.concatenate((b1,b2)))
        
#
# Ploting and comparison of the runtimes
#
hadmatmultTime = []
matmultTime = []
sizeArray = []


for i in range(13):
    rand = np.random.permutation(2**i)
    sizeArray.append(len(rand))
    t2 = Timer(lambda: matmult(hadmat(i),rand))
    #matmultTime.append(t2.timeit(number=1))
    matmultTime.append(scipy.mean(t2.repeat(repeat = 1,number = 1)))
    t1 = Timer(lambda: hadmatmult(hadmat(i),rand))
    #hadmatmultTime.append(t1.timeit(number=1))
    hadmatmultTime.append(scipy.mean(t1.repeat(repeat = 1,number = 1)))

pp = PdfPages('matmulttime.pdf') 
fig = plt.figure()
fig.suptitle('Matrix Multipication Comparison', fontsize=14, fontweight='bold')
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
plt.xlabel("Number of inputs")
plt.ylabel("Seconds")
plt.plot(sizeArray,matmultTime, label="MatMult")
plt.plot(sizeArray,hadmatmultTime, label="HadmatMult")
plt.legend(loc=0)
pp.savefig()
plt.show()
pp.close()
print("number of operation for hadmatmult=",hadCount)
print("number of operation for matmult=",matCount)