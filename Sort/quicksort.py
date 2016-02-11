"""
Created on Wed Jan 27 00:27:35 2016

@author: Amirali Shahinpour
         Brian Jones

Implementation of Quick Sort
"""

##Quick Sort
A=[6,2,9,5,7,10,4]
p = 0
r = len(A)


def Quicksort(A, p, r):    
    if p < r:
        q = Partition(A, p, r)
        #print(A[q+1:r])
        Quicksort(A, p, q)
        Quicksort(A, q+1, r)
        return A

    
    
def Partition(A,p,r):
    x = A[r-1]
    i = p - 1
    for j in range(p,r):
        print("j = ",j, "A = ", A)
        if A[j] < x:
            i += 1
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
    temp = A[i+1]
    A[i+1] = x
    A[r-1] = temp
    print("Pivot Swap = ",A[i+1])
    return i+1

print(Quicksort(A, p, r))
#print(Partition(A, 0, len(A)))