# include<stdio.h>
int main()
{
    float a,b,c;
    printf("Enter first number ");
    scanf("%f",&a);
    printf("Enter second number ");
    scanf("%f",&b);
    printf("Enter third number ");
    scanf("%f",&c);

    if (a>=b && a>=c) {
        printf("First number is largest");
    }
    else if (b>=a && b>=c) {
        printf("Second number is largest");
    }
    else {
        printf("Third number is largest");
    }
    return 0;
}