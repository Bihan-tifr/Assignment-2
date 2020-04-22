import numpy as np
import matplotlib.pyplot as plt

dt=0.1
t=np.arange(0,10.1,dt)
x=np.empty((len(t)))
x[:]=0 #initialization

xan=-5*t**2+50*t # Analytical solution

#Boundary conditions
x[0]=0
x[len(x)-1]=0

maxit=1000
for i in range(0,maxit):
	for j in range(1,len(x)-1):
		x[j]=0.5*(x[j+1]+x[j-1])+10*dt**2
	for k in range(1,11):
		if(i==670+10*k):
			plt.plot(t,x,linestyle='dashed',label="Num_sol{}th iteration".format(i))
	
plt.plot(t,xan,label="Analytical sol")
plt.xlabel("t")
plt.ylabel("x")	
plt.legend(loc='best')
plt.show()
