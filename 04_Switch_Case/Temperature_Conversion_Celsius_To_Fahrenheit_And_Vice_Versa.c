#include<stdio.h>

int main(void)
{
    float f,c;
    int ch;
    printf("\nEnter Choice \n1.Fahrenheit to Celsius \n2.Celsius to Fahrenheit");
    scanf("%d",&ch);

    switch (ch) {
        case 1:
        printf("\nEnter Fahrenheit:");
        scanf("%f",&f);
        printf("\nEquivalent celsius value is %f",((f-32.0)/1.8));
        break;

        case 2:
        printf("\nEnter Celsius:");
        scanf("%f",&c);
        printf("\nEquivalent Fahrenheit value is %f",((c*1.8)+32.0));
        break;
        default: printf("Enter the correct choice");
        break;    
    
    }
    return 0;
}
