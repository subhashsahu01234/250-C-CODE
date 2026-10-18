#include <stdio.h>

int main(){
    float bs,da,hra,gs;

    printf("Enter your base  salary ");
    scanf("%f\n",&bs);

    if (bs<5000){
        hra=bs*10/100;
        da=bs*90/100;
    }
    else {
        hra=600;
        da=bs*95/100;
    }
    gs=bs+da+hra;

    printf("Gross salary is %f",gs);
    return 0;

}