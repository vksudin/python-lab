# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:11:27 2021

@author: sudin jana
"""
def palindrome(s):
    print(s)
    l=len(s)
    p=True
    for i in range(0,l//2):
        if s[i]!=s[l-i-1]:
            p=False
            break
    if p: print('The string is a palindrome')
    else: print('The string is not a palindrome')

palindrome('a')
palindrome('abba')
palindrome('abde')

def multiply(d):
    print(d)
    a,b=1,1
    for i in d.keys():
        a*=i
        b*=d[i]
    print(a,b)

multiply({1:2,2:3,3:4})