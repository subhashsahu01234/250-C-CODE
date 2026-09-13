# include<stdio.h>
int main()
{
    int a;
    printf("Enter a number ");
    scanf("%d",&a);

    if (a>0) {
        printf("Enter Number is POSTIVE");
    }
    else if (a==0) {
        printf("Enter number is ZERO");
    }
    else {
        printf("Enter Number is NEGATIVE");
    }
    return 0;
}