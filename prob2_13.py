import numpy as np
import matplotlib.pyplot as plt
def f(t,y,p):
	return 2*p/t-2*y/t**2+t*np.log(t)
def f1(t,y,p):
	return p

tlist=[]
ylist=[]

t=1
y=1
p=0
h=0.001

while(t<=2+h):
	tlist.append(t)
	ylist.append(y)
	y+=f1(t,y,p)*h
	p+=f(t,y,p)*h
	t+=h

T=np.array(tlist)
y_exact=7*T/4+0.5*T**3*np.log(T)-3/4*(T)**3

plt.plot(tlist,ylist,label="Numerical_sol",color='yellow')
plt.plot(tlist,y_exact,label="Exact sol",color='black',linestyle='dashed')
plt.xlabel("t")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.savefig("sol.png")
plt.show()
