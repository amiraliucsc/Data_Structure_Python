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
            self.current_size == 1
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
                    
                    
myHeap = MinHeap()
myHeap.insert(4)
                
        

