#include<stdio.h>
#include<math.h>
int main()
{
    int num,original,remainder;
    int digits=0,sum=0;
    printf("Enter a number:");
    scanf("%d",&num);
    original=num;
    //Count the number of digits
    while (num!=0) {
        digits++;
        num=num/10;
    }
    num=original;
    //Calculate the Armstrong sum
    while (num!=0) {
        remainder=num%10;
        sum = sum + pow(remainder,digits);
        num=num/10;
    }
    //Check Armstrong Number
    if (sum==original) {
        printf("%d is an Armstrong number",original);
    else {
        printf("%d is not an Armstong number",original);
    return 0;
    }
    
}