# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:16:05 2021

@author: sudin jana
"""
def pangram(s):
    print(s)
    c=[False]*26
    for i in s:
        l=ord(i)
        if l>=ord('A') and l<=ord('Z'): l+=32
        if l>=ord('a') and l<=ord('z'):
            l-=ord('a')
            c[l]=True

    p=True
    for i in c:
        if i==False:
            p=False
            break

    if p: print("The string is a pangram")
    else: print("The string is not a pangram")

pangram('abcdefghij klmnopQRS TUVWxyz')
pangram('abcderr')


def check(d,k):
    if k in d.keys(): print('Key exists in dictionary')
    else: print('Key does not exist in dictionary')

check({1:1,2:1},3)
check({1:1,2:1},2)