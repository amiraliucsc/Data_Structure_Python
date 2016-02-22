# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 21:54:03 2016

@author: Amirali
"""

class minHeap:
    def __init__(self):
        self.heapArray = []
        self.heapSize = 0
    
    def insert(self,key):
        self.heapArray.append(key)
        self.heapSize += 1
        self.reHeapify( len(self.heapArray)-1 )
    
    def reHeapify(self,index):
        if index > 0:
            parent = ( index - 1 ) // 2
            if( self.heapArray[index] < self.heapArray[parent]):
                temp = self.heapArray[index]
                self.heapArray[index] = self.heapArray[parent]
                self.heapArray[parent] = temp
                self.reHeapify(parent)
    
    def printHeap(self):
        for i in range(0,self.heapSize):
            print(self.heapArray[i])
            
    def minimum(self):
        return self.heapArray[0]
        
    def extractMin(self):
        if self.heapSize > 0:
            self.heapArray[0] = self.heapArray[self.heapSize-1]
            self.heapSize -= 1
            self.reHeapifyDown(0)

    def reHeapifyDown(self,index):
        if ( index <= (self.heapSize // 2) ):
            left = (index * 2) + 1
            right = left + 1
            minPosition = index
            if (left <= self.heapSize and self.heapArray[left] < self.heapArray[minPosition]):
                minPosition = left
            if (right <= self.heapSize and self.heapArray[right] < self.heapArray[minPosition]):    
                minPosition = right
            if (minPosition != index):
                temp = self.heapArray[minPosition]
                self.heapArray[minPosition] = self.heapArray[index]
                self.heapArray[index] = temp
                self.reHeapifyDown(minPosition)
                
            
            
test = minHeap()
test.insert(5)
test.insert(9)
test.insert(12)
test.insert(50)
test.insert(8)
test.insert(0)
test.insert(6)
test.extractMin()
test.extractMin()
test.printHeap()