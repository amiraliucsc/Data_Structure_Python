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


def scaleMat(A, scalar):
    for i in range(len(A)):
        for j in range(len(A)):
            A[i][j] *= scalar
    return A

def hadmat(k):
    A = np.array([[1]])
    if k >= 1:
        for i in range(k):
            B = np.concatenate((A,A), axis = 1)
            C = np.concatenate((A, scaleMat(np.copy(A) , -1)), axis = 1)
            A = np.concatenate((B,C), axis = 0)
    return A

def decomposed(A):
    B = np.zeros((len(A)//2,len(A)//2), dtype = np.int)
    if len(A) == 1:
        return A
    else:
        for i in range(0,len(A)//2):
            for j in range(0,len(A)//2):
                 B[i][j] = A[i][j]
        decomposed(B)
    return B


def matmult(A,x):
    if len(A) != len(x):
        return -1
    else:
        product = np.array(x)
        for i in range(len(A)):
            sum = 0
            for j in range(len(A)):
                sum += A[i][j] * x[j]
            product[i] = sum
        return(product)


def hadmatmult(A,x):
    if len(A) == 1:
        return(matmult(A,x))
    else:
        x1 = np.array(x[:len(x)//2])
        x2 = np.array(x[len(x)//2:])
        decA = hadmat(int(math.log(len(A),2))-1)
        b1 = hadmatmult(decA,x1) + hadmatmult(decA, x2)
        b2 = hadmatmult(decA,x1) - hadmatmult(decA, x2)
        return(np.concatenate((b1,b2)))


hadmatmultTime = []
matmultTime = []
sizeArray = []

for i in range(13):
    rand = np.random.permutation(2**i)
    sizeArray.append(len(rand))
    t = Timer(lambda: hadmatmult(hadmat(i),rand))
    hadmatmultTime.append(scipy.mean(t.repeat(repeat = 1,number = 1)))
    t = Timer(lambda: matmult(hadmat(i),rand))
    matmultTime.append(scipy.mean(t.repeat(repeat = 1,number = 1)))
#hadmat(i)
#print(hadmatmult(hadmat(4),range(0,16)))
#print(matmult(hadmat(4),range(0,16)))
#(hadmat(4))
#hadmat(2)
print(sizeArray)    
pp = PdfPages('matmulttime.pdf') 
fig = plt.figure()
fig.suptitle('Matrix Multipication Comparison', fontsize=14, fontweight='bold')
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
plt.xlabel("Number of inputs")
plt.ylabel("Seconds")
plt.plot(sizeArray,hadmatmultTime)
plt.plot(sizeArray,matmultTime)
pp.savefig()
plt.show()
pp.close()
#print("Runtime = ", (time.time() - start_time)," Sec")
