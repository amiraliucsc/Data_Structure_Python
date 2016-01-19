# -*- coding: utf-8 -*-
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
        
        
link1 = LinkedList()
link2 = LinkedList()
link1.insert(5)
link1.insert(50)
link1.insert(500)
print(link1.isEmpty())
print(link2.isEmpty())
        