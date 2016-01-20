"""
Created on Tue Jan 16 18:19:40 2016

@author: Amirali Shahinpour

Description: to check if a given string is Palindromes or not
"""

str = "madam"
str2 = "Go hang a salami; I’m a lasagna hog."
str3 = "kayak"

def isPalindromes(str):
    str = str.lower()
    str = str.replace(".","")
    str = str.replace(";","")
    str = str.replace(" ","")
    str = str.replace(",","")
    str = str.replace("-","")
    str = str.replace("’","")
    str = str.replace("'","")
    print(str)
    if len(str) < 2:
        return True
    if str[0] == str[len(str)-1]: 
        return isPalindromes( str[1:len(str)-1] )
    else: return False
        
print( isPalindromes(str2) )