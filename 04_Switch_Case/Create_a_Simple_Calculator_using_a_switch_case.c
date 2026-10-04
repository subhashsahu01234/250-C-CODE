#include<stdio.h>
int main(void){
    float a,b;
    int choice;
    printf("Enter First number a: ");
    scanf("%f",&a);
    printf("Enter second number b: ");
    scanf("%f",&b);
    printf("\nEnter Choice \n1.Addition \n2.Substraction \n3.Multiplication \n4.Dvision(a/b) \n");
    scanf("%d",&choice);

    switch (choice) {
        case 1:
        printf("\nAddition of two number is %f",(a+b));
        break;

        case 2:
        printf("\nSubstraction of two number is %f",(a-b));
        break;

        case 3:
        printf("\nMultiplication of two number is %f",(a*b));
        break;

        case 4:
        printf("\nDivision of two number is %f",(a/b));
        break;

        default:
        printf("Enter the correct choice");
        break;
    
    }
    return 0;
}