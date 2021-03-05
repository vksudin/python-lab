# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:35:07 2021

@author: sudin jana
"""
def replace(l1,l2):
    d={}
    print(l1,l2)
    for i in range(0,len(l1)):
        d[l1[i]]=i
    for i in range(0,len(l2)):
        l2[i]=d[l2[i]]
    print(l2)

replace([1,2,3,4,5],[5,1,2,3,3,5])

def printmat(m):
    for i in range(3):
        print(m[i])

def multiply(a,b):
    printmat(a)
    printmat(b)
    ans=[[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                ans[i][j]+=a[i][k]*b[k][j]
    printmat(ans)


multiply([[1,2,3],[4,5,6],[7,8,9]],[[2,3,1],[2,4,5],[4,5,7]])