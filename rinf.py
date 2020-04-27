import numpy as np
import matplotlib.pyplot as plt
def f(t,x):
	return 1/(x**2+t**2)
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
t=0
x=1
h=0.2 #initial stepsize
tlist=[]
xlist=[]
while(1):
	#print("initial step size:{}".format(h))
	x2=rk4(2,h,t,x)
	x1=rk4(1,2*h,t,x)
	D=abs(x2-x1)
	#print("Error:{}".format(D))
	h=h*(abs(err/D))**0.2
	#print("Changed stepsize:{}".format(h))
	tlist.append(t)
	xlist.append(x)
	if(t>=3.5*10**6):
		print("Desired value of x:{}".format(x))
		break
	x=rk4(1,h,t,x)
	t+=h
	

plt.semilogx(tlist,xlist,label="solution")
plt.xlabel("t")
plt.ylabel("x")
plt.title("dx/dt=1/(x^2+t^2) over infinite range")
plt.grid(True)
plt.legend()
plt.show()
