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
            
    def search(self,data):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == data:
                found = True
            else:
                if current.getData() > data:
                    stop = True
                else:
                    current = current.getNext()
        return found
           
    def pop(self):
        prev = None
        stop = False
        current = self.head
        while current != None and not stop:
            if current.getNext() != None:
                prev = current
                current = current.getNext()
            else:
                if prev != None:
                    prev.setNext(None)
                    stop = True
                else:
                    print("List is Empty!")
                    stop = True
                    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count+=1
            current = current.getNext()
        return count
        
    def remove(self,data):
        current = self.head
        stop = False
        prev = None
        while not stop:
            if current.getData() == data:
                stop = True
            else:
                prev = current
                current = current.getNext()
        if prev == None:
            self.head = None
        else:
            prev.setNext(current.getNext)
        
            
link1 = OrderList()
link1.add(100)
link1.add(4)
link1.size()
link1.add(10)
link1.add(1)
link1.Traverse()
link1.remove(1)
link1.Traverse()
