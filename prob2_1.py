#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:18:41 2020

@author: bihan
"""
import math
import matplotlib.pyplot as plt
def f(y):
    return -9*y
def g(x,y):
    return -20*(y-x)**2+2*x

x=0
y=math.exp(1)
z=1/3
h=0.01
xlist1=[]
ylist1=[]
ylist2=[]
while x<=2.01:
    xlist1.append(x)
    ylist1.append(y)
    ylist2.append(z)
    y=y+h*f(y)
    z=z+h*g(x,z)
    x=x+h
plt.plot(xlist1,ylist1,label="solution:dy/dx=-9y")
plt.plot(xlist1,ylist2,label="solution:dy/dx=-20(y-x)^2+2x")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig("prob2_1.jpg")
plt.show()
