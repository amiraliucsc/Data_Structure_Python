# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 20:48:45 2016

@author: Amirali

To find the most frequent items in a given array

Note that first the given array is pass to the minSort.
"""

def swapSort(A):
    print(A)
    for i in range(0,len(A)):
        for j in range(0,len(A)-i):
            if j < len(A)-1 and A[j+1] < A[j]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
            print(i,j,A)    
    return A
            
           

def minSort(A):
    for i in range(0,len(A)):
        found = False
        min = A[i]
        for j in range(i,len(A)):
            if A[j] < min:
                min = A[j]
                index = j
                found = True
        if found:
            A[index] = A[i]
            A[i] = min
    return(A)
    
def most_frequent_item_count(A):
    #print(A)
    track = {}
    count = 1
    for i in range(0,len(A)-1):
        if A[i+1] - A[i] == 0:
            count+=1
            track[A[i]]=count
        else:
            count=1
    maxval = 0
    #print(track)
    for val,count in track.items():
        if count > maxval:
            maxval = count
            most = val
    print("Most occurance is the value %d which occures %d times" % (most ,maxval))
                
                
minSort([5,8,10,14,0,2,0,0])
most_frequent_item_count(minSort([5,8,-1,-1,-1,-1,-1,-1,-1,10,8,14,0,2,0,0,0]))
        