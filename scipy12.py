# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 14:15:58 2017

@author: user
"""
import random
x1=0.1
x2=0.3
x3=0.5
x4=0.8
L0=[x1,x2,x3,x4]

# 生产随机数
L=[]

for i in range(100):
    L.append(random.random())
#print(L)

L1=[]
L2=[]
L3=[]
L4=[]

def dist(x,y):
    return abs(x - y)

def means(num):
    sum1=0
    for i in num:
        sum1=sum1+i
    return float(sum1)/len(num)
        
for i in range(100):
    if dist(x1,L[i])==min(dist(x1,L[i]),dist(x2,L[i]),dist(x3,L[i]),dist(x4,L[i])):
        L1.append(L[i])
    if dist(x2,L[i])==min(dist(x1,L[i]),dist(x2,L[i]),dist(x3,L[i]),dist(x4,L[i])):
        L2.append(L[i])    
    if dist(x3,L[i])==min(dist(x1,L[i]),dist(x2,L[i]),dist(x3,L[i]),dist(x4,L[i])):
        L3.append(L[i])
    if dist(x4,L[i])==min(dist(x1,L[i]),dist(x2,L[i]),dist(x3,L[i]),dist(x4,L[i])):
        L4.append(L[i])
x1=means(L1)
x2=means(L2)
x3=means(L3)
x4=means(L4)

print(x1,x2,x3,x4)
