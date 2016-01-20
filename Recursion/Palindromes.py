"""
Created on Tue Jan 16 18:19:40 2016

@author: Amirali Shahinpour

Description: to check if a given string is Palindromes
"""

str = "madam"

def isPalindromes(str):
    if len(str) == 1:
        return True
    if str[0] == str[len(str)-1]: 
        return checkPalid( str[1:len(str)-1] )
    else: return False
        
print(isPalindromes(str))