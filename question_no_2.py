# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 19:11:36 2021

@author: sudin jana
"""
def count(s):
    print(s)
    v=0
    cn=0
    for i in s:
        c=ord(i)
        if c>=ord('A') and c<=ord('Z'): c+=32
        if c>=ord('a') and c<=ord('z'):
            if c==ord('a') or c==ord('e') or c==ord('i') or c==ord('o') or c==ord('u'): v+=1
            else: cn+=1

    print("Vowels:",v)
    print("Consonants:",cn)

count("abcde239470sbfb")


def max_num(a,b,c):
    print(a,b,c)
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

print(max_num(5,5,4))
print(max_num(2,3,5))
print(max_num(1,2,-1))
print(max_num(5,5,5))