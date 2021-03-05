# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:48:28 2021

@author: sudin jana
"""
def anagram(a,b):
    print(a,b)
    if len(a)!=len(b):
        print("Not anagrams")
        return
    a=sorted(a)
    b=sorted(b)
    for i in range(len(a)):
        if a[i]!=b[i]:
            print("Not anagrams")
            return
    print("Anagrams")

anagram('LISTEN','SILENT')
anagram('TRIANGLE','INTEGRAL')
anagram('aba','ccc')

def convert(l):
    print(l)
    t=tuple(l)
    print(t)

convert([1,23,3])