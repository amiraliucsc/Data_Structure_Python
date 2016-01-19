"""
Created on Sun Jan 17 23:04:10 2016

@author: Amirali

Purpuse: Linked List Implimentation
"""


class Node:
    def __init__(self, data = None, nextNode = None):
        self.data = data
        self.nextNode = nextNode

    def getNext(self):
        return self.nextNode
        
    def setNext(self,nextNode):
        self.nextNode = nextNode
        
    def getData(self):
        return self.data
        
    def setData(self, data):
        self.data = data
        


class LinkedList:
    def __init__(self):
        self.head = None
    
    # first we have to set the old head for the new node and then set the old head to new node
    def insert(self,data):
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp
        
    def isEmpty(self):
        return self.head == None
        
    def size(self):
        count = 0
        current = self.head
        while current != None:
            count+=1
            current = current.getNext()
        return count
        
    def search(self,look):
       current = self.head
       while current != None:
           if current.getData() == look:
               return True
           else:
               current = current.getNext()
       return False
       
    
    
    
    
    
    
    
    
# remove needs to feed only the data which is inside the linkedlist
    def remove(self,data):
        current = self.head
        prev = None
        found = False
        while (not found):
            if current.getData() == data:
                found = True
            else:
                prev = current
                current = current.getNext()
        if prev == None:
            self.head = current.getNext()
        else:
            prev.setNext(current.getNext())
            
    def traverse(self):
        current = self.head
        while current != None:
            print( current.getData() )
            current = current.getNext()
      

link1 = LinkedList()
link1.insert(1)
link1.insert(2)
link1.insert(3)
link1.insert(4)
link1.insert(5)
link1.insert(6)
link1.insert(7)
link1.insert(8)
link1.insert(9)
link1.insert(10)

link1.traverse()

link1.remove(10)
link1.remove(4)
link1.remove(1)

link1.traverse()
