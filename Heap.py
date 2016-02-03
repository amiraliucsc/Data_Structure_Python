"""
Created on Wed Jan 27 00:27:35 2016

@author: Amirali

Implementation of Min Heap
"""

class MinHeap:
    def __init__(self):
        self.current_size = 0
        self.heap_list = [0]
        
    def insert(self,key):
        if self.current_size == 0:
            self.current_size = 1
            self.heap_list.append( key )
        else:
            self.current_size+=1
            self.heap_list.append( key )
            self.reHeapify(self.current_size)
    
    def reHeapify(self,current):
        if current > 0 and current != 1:                
            parent = current // 2
            if self.heap_list[parent] > self.heap_list[current]:
                temp = self.heap_list[current]
                self.heap_list[current] = self.heap_list[parent]
                self.heap_list[parent] = temp
                self.reHeapify(parent)
            
            
    def remove(self,index):
        if self.current_size == 0 and index < len(self.heap_list)-1:
            return
        else:
            self.heap_list[index] = self.heap_list[self.current_size]
            self.current_size-=1
            self.reHeapifyDown(index)
            print(self.heap_list)
            
    def reHeapifyDown(self,index):    
        while index <= (self.current_size // 2):
            left = index*2
            right = left+1
            minValue = self.heap_list[index]
            min_position = index
            if self.heap_list[left] < minValue:
                minValue = self.heap_list[left]
                min_position = left
            elif self.heap_list[right] < minValue:
                minValue = self.heap_list[right]
                min_position = right
            temp = self.heap_list[index]
            self.heap_list[index] = min_position
            self.heap_list[min_position] = temp
            self.reHeapifyDown(min_position)
            index = min_position
        
            
            
            
    def printHeap(self):
        for i in self.heap_list:
            print(i)
            
            
myHeap = MinHeap()
myHeap.insert(4)
myHeap.insert(5)
myHeap.insert(6)
myHeap.insert(10)
myHeap.insert(2)
myHeap.insert(16)
myHeap.insert(31)
myHeap.insert(7)
print("before",myHeap.heap_list)
myHeap.remove(2)
print("after",myHeap.heap_list)



