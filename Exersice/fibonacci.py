"""
Created on Sun Jan 24 22:09:29 2016

@author: Amirali

Fibonacci recursion and normal
"""

def fib(n): # print up to the given number
    a, b = 1, 1
    while a < n:
        print(a)
        a, b = b, a+b
        
        
def fibRecursion(n): #calculate the nth fibonacci number
    if n == 1 or n == 2:
        return 1
    else:
        return (fibRecursion(n-1) + fibRecursion(n-2))
    
fib(10000)
print(fibRecursion(14))