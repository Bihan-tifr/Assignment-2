import numpy as np
import matplotlib.pyplot as plt
def f(t,y):
	return (y**2+y)/t
def rk4(j,h,x,y):
	for i in range(0,j):
		k1=h*f(x,y)
		k2=h*f(x+h/2,y+k1/2)
		k3=h*f(x+h/2,y+k2/2)
		k4=h*f(x+h,y+k3)

		y=y+k1/6+k2/3+k3/3+k4/6
		x=x+h
	return y

err=10**(-4)
t=1
y=-2
h=0.5 #initial stepsize
tlist=[]
ylist=[]
while(1):
	print("initial step size:{}".format(h))
	y2=rk4(2,h,t,y)
	y1=rk4(1,2*h,t,y)
	D=abs(y2-y1)
	print("Error:{}".format(D))
	h=h*(abs(err/D))**0.2
	print("Changed stepsize:{}".format(h))
	tlist.append(t)
	ylist.append(y)
	if(t>3):
		break
	y=rk4(1,h,t,y)
	t+=h
	

plt.scatter(tlist,ylist,label="solution")
plt.xlabel("t")
plt.ylabel("y")
plt.xlim(0.9,3.1)
plt.title("Rk4 with adaptive step size")
plt.grid(True)
plt.legend()
plt.show()
