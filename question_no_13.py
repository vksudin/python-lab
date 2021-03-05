# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:28:30 2021

@author: sudin jana
"""
def largest(l):
    print(max(l))

def largest_m(l):
    m=-1000000000000000
    for i in l:
        m=max(m,i)
    print(m)

a=[1,2,-3,4,5]
print(a)
largest(a)
largest_m(a)

import numpy as np
def equation(n):
    l=n
    a=np.zeros(l*l,dtype=int)
    a=a.reshape(l,l)
    b=np.zeros(l,dtype=int)
    print("Enter the equations:")
    for i in range(l):
        print("Enter values of a1, a2,...a"+str(l),end='')
        print(" in a1x1+a2x2+...+a"+str(l)+"x"+str(l)+"=b")
        x=list(map(int,input().split()))
        for j in range(l):
            a[i][j]=x[j]
        print("Enter the b value:")
        b[i]=int(input())
    print(a)
    print(b)
    dt=np.linalg.det(a)
    if dt==0:
        print("Solution does not exist")
        return
    res=np.linalg.inv(a)
    res=np.dot(res,b)
    for i in range(l):
        print("x"+str(i+1)+": "+str(res[i]))

equation(3)