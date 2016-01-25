# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 23:48:37 2016

@author: Amirali
"""

def binaryToDecimal(binarySTR):
    if len(binarySTR) != 0:
        num = 0
        for i in range(len(binarySTR)-1 , -1, -1):
            index = (len(binarySTR)-1) - i
            if binarySTR[i] == "1":
                num += (2 ** index)
        return num
    else:
        return 0
    
    
def hexToDecimal(hexSTR):
    if len(hexSTR) != 0:
        num = 0
        val = 0
        for i in range(len(hexSTR)-1,-1,-1):
            index = (len(hexSTR)-1 ) - i
            if hexSTR[i] == "A" or hexSTR[i] == "a":
                val = 10
            elif hexSTR[i] == "B" or hexSTR[i] == "b":
                val = 11
            elif hexSTR[i] == "C" or hexSTR[i] == "c":
                val = 12
            elif hexSTR[i] == "D" or hexSTR[i] == "d":
                val = 13
            elif hexSTR[i] == "E" or hexSTR[i] == "e":
                val = 14
            elif hexSTR[i] == "F" or hexSTR[i] == "f":
                val = 15
            elif int(hexSTR[i]) < 10:
                val = int(hexSTR[i])    
            num+= val * (16 ** index)
        return num
    else:
        return 0
    
    
#print(binaryToDecimal('1000000000001'))
print(hexToDecimal('FF'))