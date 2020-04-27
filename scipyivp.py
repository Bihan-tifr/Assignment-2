from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

z=int(input("Which Problem you wanna solve? Enter 1,2,3,4:"))
if(z==1):
	def f(t,y):
		return t*np.exp(3*t)-2*y

	sol=solve_ivp(f,[0,10],[0])

	T=np.array(sol.t)
	print(type(T))
	print(T)
	X=np.reshape(sol.y,len(T))
	print(sol.y)
	print(X)
	Z=1/25*np.exp(-2*T)*(np.exp(5*T)*(5*T-1)+1)
	plt.scatter(T,X,label="Numerical sol points")
	plt.plot(T,Z,label="Analytical sol",color='red')
	plt.xlabel("t")
	plt.ylabel("y")
	plt.legend()
	plt.show()
if(z==2):
	def f(t,y):
		return 1-(t-y)**2

	sol=solve_ivp(f,[2,3],[1])

	T=np.array(sol.t)
	Y=np.reshape(sol.y,len(T))
	Z=(T**2-3*T+1)/(T-3)
	print(sol.y)
	print(Y)
	plt.scatter(T,Y,label="Numerical sol")
	plt.plot(T,Z,label="Analytical sol",color='red')
	plt.xlabel("t")
	plt.ylabel("y")
	plt.legend()
	plt.show()
if(z==3):
	def f(t,y):
		return 1+y/t
	
	sol=solve_ivp(f,[1,2],[2])

	T=np.array(sol.t)
	Y=np.reshape(sol.y,len(T))
	print(sol.y)
	print(Y)
	Z=T*(np.log(T)+2)
	plt.scatter(T,Y,label="Numerical sol")
	plt.plot(T,Z,label="Analytical sol",color='red')
	plt.xlabel("t")
	plt.ylabel("y")
	plt.legend()
	plt.show()
if(z==4):

	def f(t,y):
		return np.cos(2*t)+np.sin(3*t)
	sol=solve_ivp(f,[0,6],[1])

	T=np.array(sol.t)
	Y=np.reshape(sol.y,len(T))
	print(sol.y)
	print(Y)
	plt.scatter(T,Y,label="Numerical sol")
	plt.xlabel("t")
	plt.ylabel("y")
	plt.legend()
	plt.show()
