# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:33:16 2021

@author: sudin jana
"""
def calculate(l):
    print(l)
    if len(l)==1:
        print('Too small a list')
        return

    m=max(l[0],l[1])
    m2=l[0]+l[1]-m
    s=min(l[0],l[1])
    s2=l[0]+l[1]-s
    for i in range(2,len(l)):
        if l[i]>=m:
            m2=m
            m=l[i]
        elif l[i]>m2: m2=l[i]
        if l[i]<=s:
            s2=s
            s=l[i]
        elif l[i]<s2: s2=l[i]

    print('maximum:',m)
    print('second max:',m2)
    print('minimum:',s)
    print('second min:',s2)

calculate([1,3,4,1,2,-1,3,-1,2,3,5,6])


def sumdiag(m):
    print(m)
    l=min(len(m),len(m[0]))
    s=0
    for i in range(l):
        s+=m[i][i]
    print("sum:",s)

m=[[1,2,3],[2,1,2]]
sumdiag(m)
m=[[1,2],[2,3],[3,4]]
sumdiag(m)