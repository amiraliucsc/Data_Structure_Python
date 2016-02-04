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
        if (index < self.current_size):            
            '''
            if self.current_size == 0 and index < len(self.heap_list)-1:
                return
            else:
                self.heap_list[index] = self.heap_list[self.current_size]
                self.current_size-=1
                if index <= (self.current_size // 2):
                    self.reHeapifyDown(index)
            '''
        else:
            print("Please enter a number between 1 and %d" % (self.current_size))
            
    
            
    def reHeapifyDown(self,index):    
        #print("size=",self.current_size)
        #print("index=",index)
        #print("heap=",self.heap_list)
        left = -1
        right = -1
        if(index*2 <= self.current_size):
            left = index*2
            #print('left=',left)
        if((index*2) +1 <= self.current_size):
            right = (index*2) +1
            #print('right=',right)
        minValue = self.heap_list[index]
        min_position = index
        if(left != -1):
            if self.heap_list[left] < minValue:
                minValue = self.heap_list[left]
                min_position = left
        if(right != -1):
            if self.heap_list[right] < minValue:
                minValue = self.heap_list[right]
                min_position = right
        #print("min=",minValue)
        #print('pos',min_position)
        temp = self.heap_list[index]
        self.heap_list[index] = self.heap_list[min_position]
        self.heap_list[min_position] = temp
        #print("now=",self.heap_list)
        index = min_position
        print(index)
        if index <= (self.current_size // 2):
            self.reHeapifyDown(index)
        else:
            return
            
            
            
    def printHeap(self):
        for i in self.heap_list:
            print(i)
            
            
myHeap = MinHeap()
myHeap.insert(1)
myHeap.insert(5)
myHeap.insert(6)
myHeap.insert(8)
myHeap.insert(7)
myHeap.insert(10)
myHeap.insert(17)
myHeap.insert(11)
myHeap.insert(12)
myHeap.insert(13)
print("before",myHeap.heap_list," size= ",myHeap.current_size)
myHeap.remove(5)


print("after",myHeap.heap_list," size= ",myHeap.current_size)



