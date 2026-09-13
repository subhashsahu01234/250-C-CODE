# include<stdio.h>
int main()
{
    char str;
    printf("Enter String ");
    scanf("%c",&str);

    if (str=='a' || str=='e' || str=='i' || str=='o' || str=='u') {
        printf("String is Vowel");
    }
    else {
        printf("String is consonant");
    }
    return 0;
}