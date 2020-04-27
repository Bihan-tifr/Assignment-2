#include<stdio.h>
#include<math.h>
#include<stdlib.h>

float f(float(t),float(y))
{
	return y-t*t+1;
}

int main()
{
	float t,y,h;	
	t=0;
	y=0.5;
	h=0.2;
	do
	{	printf("%f\t%f\n",t,y);
		y=y+h*f(t,y);
		t=t+h;
	}while(t<=3.2);
}
