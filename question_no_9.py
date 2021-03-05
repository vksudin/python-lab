# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:09:16 2021

@author: sudin jana
"""
def unique(l):
    print(l)
    s=set({})
    for i in l:
        s.add(i)
    return list(s)

print(unique([1,2,2,3,4,5,5]))

def sum(d):
    print(d)
    a,b=0,0
    for i in d.keys():
        a+=i
        b+=d[i]
    print(a,b)

sum({1:2,2:3,3:4})