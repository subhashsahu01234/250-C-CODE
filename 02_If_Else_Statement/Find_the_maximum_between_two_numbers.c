# include<stdio.h>
int main()
{
    float a,b;
    printf("Enter first number ");
    scanf("%f",&a);
    printf("Enter second number ");
    scanf("%f",&b);

    if (a>b) {
        printf("First number is largest");
    }
    else {
        printf("Second number is largest");
    }
    return 0;
}