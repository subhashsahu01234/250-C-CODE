# include<stdio.h>
int main(void)
{
    float a,b,c;
    printf("Enter first angle of a triangle ");
    scanf("%f",&a);
    printf("Enter second angle of a triangle ");
    scanf("%f",&b);
    printf("Enter third angle of a triangle ");
    scanf("%f",&c);
    
    if (a > 0 && b > 0 && c > 0 && (a + b + c == 180.0f)) {
        printf("The angles are valid");
    }
    else {
        printf("Angles are invalid");
    }
    return 0;


}