# include<stdio.h>
int main()
{
    int a,b,c;
    printf("Enter first number ");
    scanf("%d",&a);
    printf("Enter second number ");
    scanf("%d",&b);
    printf("Enter third number ");
    scanf("%d",&c);

    if (a>b && b>c) {
        printf("First number is largest");
    }
    else if (b>a && b>c) {
        printf("Second number is largest");
    }
    else {
        printf("Third number is largest");
    }
    return 0;
}