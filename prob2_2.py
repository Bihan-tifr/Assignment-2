#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 17:21:18 2020

@author: bihan
"""
import math
import matplotlib.pyplot as plt
def f(t,y):
    return y/t-(y/t)**2
def an(t):
    return t/(math.log(t)+1)
x=1
y=1
h=0.1
xlist1=[]
ylist1=[]
ylist2=[]
elist=[]
relist=[]
while x<=2.1:
    xlist1.append(x)
    ylist1.append(y)
    ylist2.append(an(x))
    y=y+h*f(x,y)
    err=abs(y-an(x))
    re=abs(err/an(x))
    elist.append(err)
    relist.append(re)
    x=x+h

plt.figure(1)    
plt.plot(xlist1,ylist1,label="numerical solution")
plt.plot(xlist1,ylist2,label="analytial sol")
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.savefig("prob2_2_sol.jpg")

plt.figure(2)
plt.plot(xlist1,elist,label="absolute error")
plt.xlabel("t")
plt.ylabel("Abs_err")
plt.legend()
plt.savefig("prob2_2_err.jpg")

plt.figure(3)
plt.plot(xlist1,elist,label="relative error")
plt.xlabel("t")
plt.ylabel("Rel_err")
plt.legend()
plt.savefig("prob2_2_re.jpg")
plt.show()
