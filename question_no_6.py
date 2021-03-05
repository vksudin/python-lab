# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 19:52:36 2021

@author: sudin jana
"""
s=input("Enter the string:")

lower=0

upper=0

for i in s:
    if(ord(i)>=65 and ord(i)<=90):
        upper=upper+1
    elif(ord(i)>=97 and ord(i)<=122):
        lower=lower+1


print(upper)
print(lower)


#FOR first part of this question you should follow 3.b)
            