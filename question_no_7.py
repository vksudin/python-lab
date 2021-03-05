# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 19:54:09 2021

@author: sudin jana
"""

a=input("Enter the number:")

a=int(a)

res=0


b=a//2+1

for i in range(1,b):
    if(a%i==0):
        res=res+i

if(res==a):
    print("Perfect number:")
else:
    print("Not a perfect number:")
    
    
#for the 2nd part you should follow the 1.b)