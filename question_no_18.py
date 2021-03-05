# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:45:32 2021

@author: sudin jana
"""
def pattern(n):
    for i in range(n): print('*',end=' ')
    print()
    for i in range(n-2):
        print('*',end=' ')
        for j in range(n-2): print(' ',end=' ')
        print('*')
    for i in range(n): print('*',end=' ')

pattern(8)

#2nd part is question no.13