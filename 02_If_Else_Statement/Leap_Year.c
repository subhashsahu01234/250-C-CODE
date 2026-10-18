#include<stdio.h>
int main()
{
    int a;
    printf("Enter year: ");
    scanf("%d",&a);
    if (a%4==0) {
        printf("Entered year is leap year");
    }
    else {
        printf("Entered is not leap year");
    }
    return 0;
}