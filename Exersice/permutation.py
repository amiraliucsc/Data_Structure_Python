"""
Created on Thu Jan 21 22:10:38 2016

@author: Amirali

Calculate the permutation of a given list
"""

def permutaion(Arr):
    if len(Arr) == 0:
        return []
    elif len(Arr) == 1:
        return [Arr]
    else:
        perm = []
        for i in range(len(Arr)):
            key = Arr[i]
            others = Arr[:i] + Arr[i+1:]
            for k in permutaion(others):
                perm.append([key] + k)
        return perm
    
Test = [1,2,3,4]
Result = permutaion(Test)
for i in Result:
    print(i)