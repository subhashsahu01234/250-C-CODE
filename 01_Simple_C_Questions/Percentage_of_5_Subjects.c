# include<stdio.h>
int main()
{
    int M,P,C,E,SST;
    float Percentage;

    printf("Enter the marks of Maths, Physics, Chemistry, English and SST");
    scanf("%d%d%d%d%d",&M, &P, &C, &E, &SST);

    Percentage=(M+P+C+E+SST)/5;

    printf("You're Percentage is %f\n",Percentage);

    return 0;
}