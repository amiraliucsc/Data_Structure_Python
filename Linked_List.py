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
        nextNode = self.head
        while nextNode != None:
            count+=1
            nextNode = nextNode.getNext()
        return count

link1 = LinkedList()
link1.insert(1)
link1.insert(10)
print(link1.size())
