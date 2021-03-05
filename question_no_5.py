# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 19:47:11 2021

@author: sudin jana
"""
def armstrong(n):
    no=n
    l=0
    while n>0:
        n//=10
        l+=1

    a=0
    n=no
    while n>0:
        a+=pow(n%10,l)
        n//=10

    if no==a: print(a,'is an armstrong number')
    else: print(a,'is not an armstrong number')

armstrong(153)
armstrong(5)
armstrong(34)

def multiply(l):
    print(l)
    p=1
    for i in l:
        p*=i
    print("Product of number is:",p)

multiply([1,2,3,4,5])
multiply([2,3,4,5,0])