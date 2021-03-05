# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:41:59 2021

@author: sudin jana
"""
def printmat(m):
    for i in range(3):
        print(m[i])

def add(a,b):
    printmat(a)
    print()
    printmat(b)
    print()
    ans=[[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            ans[i][j]+=a[i][j]+b[i][j]
    printmat(ans)

add([[1,2,3],[4,5,6],[7,8,9]],[[2,3,1],[2,4,5],[4,5,7]])

def pattern(n):
    p=[0 for _ in range(n)]
    p[0]=1
    for i in range(1,n): p[i]=p[i-1]*2

    for i in range(n):
        for j in range(i+1): print(p[i-j],end=' ')
        print()

pattern(7)