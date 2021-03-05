# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:22:42 2021

@author: sudin jana
"""
def permutation(a,l,r):
    if l==r:
        print(a)
        return
    for i in range(l,r+1):
        t=a[i]
        a[i]=a[l]
        a[l]=t
        permutation(a,l+1,r)
        t = a[i]
        a[i] = a[l]
        a[l] = t

def combination(a):
    n=len(a)
    m=pow(2,n)

    for i in range(0,m):
        for j in range(0,n):
            if ((i>>j)&1)==1: print(a[j],end=' ')
        print()

permutation([1,2,3],0,2)
combination([1,2,3])


def merge(d1,d2):
    d={}
    for i in d1.keys():
        d[i]=[d1[i]]
    for i in d2.keys():
        if i in d.keys():
            d[i].append(d2[i])
        else: d[i]=[d2[i]]
    print(d)

merge({1:2,2:3},{1:3,3:4})