# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:40:36 2021

@author: sudin jana
"""
def largest(l):
    print(l)
    print(max(l))

largest([1,2,-3,4,-5])


def sorting(l):
    print(l)
    l=sorted(l)
    print(l)

def sorting_m(l):
    n=len(l)
    print(l)
    for i in range(n-1):
        p=False
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                p=True
                t=l[j]
                l[j]=l[j+1]
                l[j+1]=t
        if p: continue
        else: break
    print(l)

sorting([1,4,3,1,2])
sorting_m([4,5,6,1,7,8,2])