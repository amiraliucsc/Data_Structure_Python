# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 18:41:47 2016

@author: Amirali

found Prime numbers
"""
import math

def findPrime():
    found = True
    num=1
    count = 1
    divcount = 1
    while(found):
        if num == 1 or num==2:
            print(count," Prime num=",num)
            if num == 1:
                num+=1
                count+=1
            else:
                num=3
        else:
            for i in range(2,int(math.sqrt(num))+1):
                if(num % i == 0):
                    divcount+=1
                if(divcount > 2):
                    break
            if divcount == 1:
                count+=1
                print(count," Prime num=",num)
            divcount=1
            num+=2            
            if(num>100000000000000000):
                found = False
                

findPrime()
        
        

