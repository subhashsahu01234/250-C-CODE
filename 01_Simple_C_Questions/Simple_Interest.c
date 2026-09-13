# include<stdio.h>
float main()
{
    float P,R,T,SI;
     printf("Enter the Principle, rate and time ");
     scanf("%f%f%f", &P,&R,&T);

     SI=(P*R*T)/100;
     printf("Simple interest is : %f",SI);

     return 0;
}