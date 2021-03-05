# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:52:07 2021

@author: sudin jana
"""
def frequency(s):
    d={}
    print(s)
    for i in s:
        if i not in d.keys():
            d[i]=1
        else: d[i]+=1
    print(d)

frequency('abcdeada')
frequency('google.com')

#question no-21 for the 2nd part of this question
