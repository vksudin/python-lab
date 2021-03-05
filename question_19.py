# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:46:49 2021

@author: sudin jana
"""
def group(l):
    for i in l:
        if i<2: print('born')
        elif i<11: print('child')
        elif i<18: print('young')
        elif i<50: print('adult')
        elif i<79: print('old')
        else: print('very old')

group([1,5,19,25,80,65])

#part b is the question no.12