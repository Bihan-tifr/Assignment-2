import matplotlib.pyplot as plt
import numpy as np

def f1(t,u1,u2,u3):
	return u1+2*u2-2*u3+np.exp(-t)
def f2(t,u1,u2,u3):
	return u2+u3-2*np.exp(-t)
def f3(t,u1,u2,u3):
	return u1+2*u2+np.exp(-t)

t=0
u1=3
u2=-1
u3=1
h=0.1
tlist=[]
u1list=[]
u2list=[]
u3list=[]

while(t<=1):
	tlist.append(t)
	u1list.append(u1)
	u2list.append(u2)
	u3list.append(u3)
	print(u1,u2,u3)

	k1=h*f1(t,u1,u2,u3)
	l1=h*f2(t,u1,u2,u3)
	m1=h*f3(t,u1,u2,u3)
	#print(k1,l1,m1)

	k2=h*f1(t+h/2,u1+k1/2,u2+l1/2,u3+m1/2)
	l2=h*f2(t+h/2,u1+k1/2,u2+l1/2,u3+m1/2)
	m2=h*f3(t+h/2,u1+k1/2,u2+l1/2,u3+m1/2)
	#print(k2,l2,m2)

	k3=h*f1(t+h/2,u1+k2/2,u2+l2/2,u3+m2/2)
	l3=h*f2(t+h/2,u1+k2/2,u2+l2/2,u3+m2/2)
	m3=h*f3(t+h/2,u1+k2/2,u2+l2/2,u3+m2/2)
	#print()	

	k4=h*f1(t+h,u1+k3,u2+l3,u3+m3)
	l4=h*f2(t+h,u1+k3,u2+l3,u3+m3)
	m4=h*f3(t+h,u1+k3,u2+l3,u3+m3)

	u1+=k1/6+k2/3+k3/3+k4/6	
	u2+=l1/6+l2/3+l3/3+l4/6	
	u3+=m1/6+m2/3+m3/3+m4/6	
	t+=h

plt.plot(tlist,u1list,label="u1")
plt.plot(tlist,u2list,label="u2")
plt.plot(tlist,u3list,label="u3")
plt.xlabel("x")
plt.ylabel("u")
plt.grid(True)
plt.legend()
plt.savefig("coupledrk4.jpg")
plt.show()



