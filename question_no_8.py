# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:01:46 2021

@author: sudin jana
"""
def factorial(n):
    f=1
    for i in range(1,n+1):
        f*=i
    print("Factorial of",n,"is:",f)

factorial(5)
factorial(10)

def sort_dict(d):
    print(d)
    l=[]
    for i in d.keys():  #convert dict to list of tuples
        l.append((i,d[i]))
    l.sort(key=lambda x:x[1])  #sort tuples by 2nd value
    d={}
    d2={}
    for i in l: #convert list back to dict
        d[i[0]]=i[1]
    print('Ascending order:',d)

    i=len(l)-1
    while i>=0:
        d2[l[i][0]]=l[i][1]
        i-=1
    print('Descending order:',d2)
    
sort_dict({1:1,2:9,3:4})
sort_dict({1:1,2:2,3:1})
