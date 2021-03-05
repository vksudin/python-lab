# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 19:19:09 2021

@author: sudin jana
"""
def encode(s):
    print(s)
    a=""
    c=ord(s[0])
    l=0
    for i in s:
        if ord(i)==c: l+=1
        else:
            if c>=ord('A') and c<=ord('Z'): c+=32
            else: c-=32
            a+=chr(c)
            if l>1: a+=str(l)
            l=1
            c=ord(i)
    if c>=ord('A') and c<=ord('Z'): c+=32
    else: c-=32
    a+=chr(c)
    if l>1: a+=str(l)
    print(a)

encode('aaaabbBccdee')


def hcf_lcm(a,b):
    print(a,b)
    x=a
    y=b
    t=0
    while b!=0:
        t=b
        b=a%b
        a=t
    print("HCF:",a)
    print("LCM:",x*y//a)

hcf_lcm(2,7)
hcf_lcm(5,35)