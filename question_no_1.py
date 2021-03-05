# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 19:07:09 2021

@author: sudin jana
"""
def count(s):
    print(s)
    d=0
    a=0
    for i in s:
        c=ord(i)
        if c>=ord('0') and c<=ord('9'): d+=1
        elif (c>=ord('a') and c<=ord('z')) or (c>=ord('A') and c<=ord('Z')): a+=1
    print("Alphabets:",a)
    print("Digits:",d)
    print("Special symbols:",len(s)-a-d)

count('abcaesfhslgfls2325w(&@&#),msdhbfagf')
count('abcd1234##')

def sumlist(l):
    print(l)
    s=0
    for i in l:
        s+=i
    print("Sum of list is:",s)

sumlist([1,2,3,4,5])
sumlist([3,2,-1,2,3,4])