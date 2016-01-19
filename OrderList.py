"""
Created on Tue Jan 19 00:26:10 2016

@author: Amirali

Order List
"""


class Node:
    def __init__(self, data = None, nextNode = None):
        self.data = data
        self.nextNode = nextNode
    
    def setNext(self,nextNode):
        self.nextNode = nextNode
        
    def getNext(self):
        return self.nextNode
        
    def setData(self,data):
        self.data = data
    
    def getData(self):
        return self.data



class OrderList:
    def __init__(self):
        self.head = None

    def add(self,item):
        current = self.head
        prev = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                prev = current
                current = current.getNext()
        temp = Node(item)
        if prev == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            prev.setNext(temp)


    def Traverse(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()
           
link1 = OrderList()
link1.add(3)
link1.add(1)
link1.add(5)
link1.Traverse()