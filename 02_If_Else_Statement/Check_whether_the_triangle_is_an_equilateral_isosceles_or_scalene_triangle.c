#include<stdio.h>
int main(){
    int a,b,c;
    printf("Enter first side of the triangle: ");
    scanf("%d",&a);
    printf("Enter second side of the triangle: ");
    scanf("%d",&b);
    printf("Enter third side of the triangle: ");
    scanf("%d",&c);
    if (a > 0 && b > 0 && c > 0 && (a + b > c) && (a + c > b) && (b + c > a)) {
        printf("Sides are valid\n");
            if(a==b && b==c) {
                printf("It is Equilateral triangle: ");
            }
            else if(a!=b && b!=c && a!=c) {
                printf("triangle is scalene");
            }
            else {
                printf("triangle is isoceles");
            }
    }
    else {
        printf("Sides are invalid");
    }            
    return 0;
}