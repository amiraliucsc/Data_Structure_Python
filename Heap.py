"""
Created on Wed Jan 27 00:27:35 2016

@author: Amirali

Implementation of Heap
"""

class MinHeap:
    def __init__(self, key):
        self.root = key
        self.left = None
        self.right = None
        
    def insert(self,key):
        if self.root < key:
            if self.left == None:
                self.left = MinHeap(key)
            elif self.right == None:
                self.right == MinHeap(key)
            else:
                while(self.left != None):
                    self.left.insert(key)
    
    def remove(self,key):
                    
                    
myHeap = MinHeap(3)
myHeap.insert(4)
                
        

