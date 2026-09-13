# include<stdio.h>
float main()
{
    float base, height, Area;
    printf("Enter base and height ");
    scanf("%f%f",&base,&height);

    Area=(base*height)/2;
    printf("Area Of Triangle: %f\n",Area);

    return 0;
}