# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:50:20 2021

@author: sudin jana
"""
def frequency(s):
    print(s)
    c=[0 for _ in range(256)]
    for i in s:
        c[ord(i)]+=1

    m=0
    m2=0
    ca=0
    ans=0
    if c[0]>c[1]:
        m=c[0]
        m2=c[1]
        ca=0
        ans=1
    else:
        m=c[1]
        m2=c[0]
        ca=1
        ans=0

    for i in range(2,256):
        if c[i]>=m:
            m2=m
            ans=ca
            m=c[i]
            ca=i
        elif c[i]>m2:
            m2=c[i]
            ans=i

    print('Second most frequent character is:',chr(ans))

frequency('acbba')
frequency('aabababa')


def length(s):
    print(s)
    print(len(s))

length('abababa')
length('a')