"""
Created on Sun Jan 24 23:48:37 2016

@author: Amirali Shahinpour

Convert binary to decimal and hex to decimal
"""

def binaryToDecimal(binarySTR):
    if len(binarySTR) != 0:
        num = 0
        for i in range(len(binarySTR)-1 , -1, -1):
            index = (len(binarySTR)-1) - i
            if binarySTR[i] == "1":
                num += (2 ** index)
            elif binarySTR[i] == "0":
                pass
            else:
                print(binarySTR[i]+" is not a valid binary value, please enter either 0 or 1")
                return 0
        return num
    else:
        return 0
    
    
def hexToDecimal(hexSTR):
    if len(hexSTR) != 0:
        num = 0
        val = 0
        for i in range(len(hexSTR)-1,-1,-1):
            index = (len(hexSTR)-1 ) - i
            try:
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
            except ValueError:
                print(hexSTR[i]+" is not a valid hexadecimal value please enter 0-9 and A-F.")
                return 0
        return num
    else:
        return 0
    
    
print(binaryToDecimal('110101011111111111111111111111111111111111111'))
print(hexToDecimal('FDCfcaa234F0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA1'))