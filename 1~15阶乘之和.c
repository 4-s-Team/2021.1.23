#include <stdio.h>
float JC(int x)
{
	int i;
	float jc=1;
	if(x==1)return 1;
	else 
	{
		
		for(i=1;i<=x;i++)jc*=i;
		return jc;
	}
}
void main()
{
	float sum=0;
	int i;
	for(i=1;i<=15;i++)sum+=JC(i);
	printf("1~15½×³ËÖ®ºÍÎª£»%e",sum);
}
