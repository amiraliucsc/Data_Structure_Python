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
       
   
    def remove(self,data):
        current = self.head
        while current != None:
            if current.getData() == data:
                nextNode = current.getNext()
                nextNodeData = nextNode.getData()
                current.setData( nextNodeData )
                current.setNext(nextNode.getNext())
                return
            current = current.getNext()    
        print (data," was not in the linked list.")
        
      

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
print(link1.search(100))
link1.remove(100)
print(link1.size())
