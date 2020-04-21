#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 18:04:27 2020

@author: bihan
"""
import matplotlib.pyplot as plt
import math
def f(x,y,p):
    return 2*p-y+x*math.exp(x)-x
def g(x,y,p):
    return p
x=0
y=0
p=0
h=0.1
xl=[]
yl=[]
y1l=[]
while x<=1.1:
    xl.append(x)
    yl.append(y)
    y1l.append(p)
    
    k1=h*f(x,y,p)
    l1=h*g(x,y,p)
    k2=h*f(x+h/2,y+l1/2,p+k1/2)
    l2=h*g(x+h/2,y+l1/2,p+k1/2)
    k3=h*f(x+h/2,y+l2/2,p+k2/2)
    l3=h*g(x+h/2,y+l2/2,p+k2/2)
    k4=h*f(x+h,y+l3,p+k3)
    l4=h*g(x+h,y+l3,p+k3)

    p=p+k1/6+k2/3+k3/3+k4/6
    y=y+l1/6+l2/3+l3/3+l4/6
    x=x+h

plt.plot(xl,yl,label="y")
plt.plot(xl,y1l,label="y1l")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig("rk4_sol.jpg")
plt.show()
