"""
Created on Tue Feb 11 15:04:10 2016
@author: Amirali Shahinpour & Brian Jones
Purpuse: priority queue implimentation using Linked List to compare with heap implementation

"""


class LinkedList:
    
    def __init__(self, key = None):
        
        self.head = self.Node(key)
        self.size = 1

    class Node:
        def __init__(self, key):
            self.value = key
            self.nextNode = None

        def getNext(self):
            return self.nextNode

        def setNext(self, newNode):
            self.nextNode = newNode

        def getVal(self):
            return self.value

        def setVal(self,val):
            self.value = val
    
    def add(self, key):
        temp = self.Node(key)
        temp.setNext(self.head)
        self.head = temp
        self.size += 1
        
    def get(self, index):
        #print(index, self.size)
        if self.size > index:
            i = 0
            curNode = self.head
            while (i < index):
                #print (curNode.getVal())
                curNode = curNode.getNext()
                if curNode == None:
                    return
                i+=1
            return curNode.getVal()
        else:
            print("Please enter a valid number")
            
    def search(self, key):
        i=0
        #print(index, self.size)
        curNode = self.head
        while (curNode.getVal() != key):
            curNode = curNode.getNext()
            if curNode == None:
                return
            i+=1
        return i

    def setIndex(self, index, key):
        #print(index, self.size)
            
        if self.size > index:
            i = 0
            curNode = self.head
            while (i < index):
                #print (curNode.getVal())
                curNode = curNode.getNext()
                if curNode == None:
                    return
                i+=1
            curNode.setVal(key)
        else:
            print("Please enter a valid number")
            

    def remove(self, index):
        prev = self.Node(0)
        if index == 0:
            remVal = self.head.getVal()
            self.head = self.head.getNext()
            self.size -= 1
            return remVal
        if self.size > index:
            i = 0
            curNode = self.head
            while (i < index):
                #print (curNode.getVal())
                #print("cur val" ,curNode.getVal())
                if (i + 1 == index):
                    prev = curNode
                    #print("prev val" ,prev.getVal())
                curNode = curNode.getNext()
                if curNode == None:
                    return
                i+=1
                
            remVal = curNode.getVal()
            #print("remval=",remVal)
            prev.setNext(curNode.getNext())
            self.size-=1
            return remVal
        else:
            print("Please enter a valid number")
            
            
    def __iter__(self):
        cursor = self.head
        while cursor:
            yield cursor.getVal()
            cursor = cursor.getNext()
        
        
def insert(S,x):
    S.add(x)

def Maximum(S):
    max = 0
    for i in iter(S):
        if i > max:
            max = i
    return max
    
def ExtractMax(S):
    max = Maximum(S)
    index = S.search(max)
    return S.remove(index)
        
def increaseKey(S,x,k):
    S.setIndex(x,k)
    
    

one = LinkedList(3)
two = LinkedList(10)
insert(two,1)
insert(two,10)
insert(two,100)
insert(two,1000)
insert(one,5)
insert(one,123)
insert(one,46)
insert(one,59)
increaseKey(two,0,5000)
for i in iter(two):
    print(i)

print("max=",ExtractMax(two))
print("max=",ExtractMax(two))
print("max=",ExtractMax(two))
print("===")
for i in iter(two):
    print(i)