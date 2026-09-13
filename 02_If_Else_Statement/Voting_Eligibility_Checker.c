# include<stdio.h>
int main()
{
    int age;
    printf("Enter your age ");
    scanf("%d",&age);

    if (age<18){
        printf("you're not eligible for vote");
    }
    else {
        printf("you're eligible for vote");
    }
    return 0;
}