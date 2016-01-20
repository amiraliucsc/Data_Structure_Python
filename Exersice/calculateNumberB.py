"""
Author : Amirali Shahinpour

Description: This function accept a number A and return number B which B is the largest number 
smaller than A and B has the same digit as A. example A=315,  B=153   or   A=81024,  B=80421 
"""

num = 315

def calculateNumberB(num):
    numlist = list(str(num))

    for i in range(len(numlist)-2,-1,-1):
        if numlist[i+1] < numlist[i]:
            break
    temp = numlist[i]
    numlist[i] = numlist[i+1]
    numlist[i+1] = temp
    found = False
    for i in range(i+1,len(numlist)):
        j = i
        max = int(numlist[j])
        for j in range(j,len(numlist)):
            if( int(numlist[j]) > max ):
                max = int(numlist[j])
                index = j
                found = True
        if found:
            temp = numlist[i]
            numlist[i] = max
            numlist[index] = temp   
            found = False
    num=""       
    for k in numlist:
        num += str(k)
    return(int(num))



print( calculateNumberB(num) )
