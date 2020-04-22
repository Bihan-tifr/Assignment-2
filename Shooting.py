import numpy as np
import matplotlib.pyplot as plt

def Ivp(v_0):
	t=0
	x=0
	t1=10
	h=0.01
	v=v_0 #initial guess of velocity
	tlist=[]
	xlist=[]
	while(t<=t1):
		tlist.append(t)
		xlist.append(x)
	
		x=x+v*h
		v=v-10*h
		t=t+h
	return xlist

z=0
j=0
tl=np.arange(0,10.01,0.01)
xan=-5*tl**2+50*tl # Analytical solution
N=len(tl)
while(1):
	v1=float(input("Enter 1st initial guess of speed:"))
	v2=float(input("Enter 2nd initial guess of speed:"))
	x1l=Ivp(v1)
	x2l=Ivp(v2)
	plt.plot(tl,x1l,color='green')
	plt.plot(tl,x2l,color='green')
	x1=x1l[N-1]
	x2=x2l[N-1]
	if(x1==0):
		z=1
		print("{} is true initial speed".format(v1))
		plt.plot(tl,x1l,label="bvp_solution",color='red')
		break
	elif(x2==0):
		z=2
		print("{} is true initial speed".format(v2))
		plt.plot(tl,x2l,label="bvp_solution",color='red')
		break
	elif(x1*x2<0):
		z=3
		print("True initial speed lies in between {} and {}".format(v1,v2))
		break

if(z==3): 
	for i in range(0,50): #solution by bisection
		v=(v1+v2)/2
		xl=Ivp(v)
		x=xl[N-1]
		if(x==0):
			print("True initial speed is {}".format(v))
			z=4
			break
		elif(abs(x)<0.000000001):
			print("True initial speed is {}".format(v))
			z=4
			break
		plt.plot(tl,xl,color='green')
		elif(x1*x<0):
			v2=v
			x2=x
		elif(x2*x<0):
			v1=v
			x1=x
		
		
plt.ylim(0,200)
plt.xlim(0,11)
plt.xlabel("t")
plt.ylabel("x")
plt.title("Solution of d^x/dt^2=-10 by shooting method:[x(0)=x(10)=0]")
plt.plot(tl,xan,label="bvp_Analytical sol",color='black')
if(z==4):
	plt.plot(tl,xl,label="bvp_num_sol",color='red')
			
plt.legend()
plt.savefig("shooting.jpg")
plt.show()



















