#include <stdio.h>
int main(){
    int profit,loss,a,b;
    printf("Input principle amount ");
    scanf("%d",&a);
    printf("Enter selling amount ");
    scanf("%d",&b);

    profit=(a-b);
    loss=(b-a);
    if(a>b){
        printf("Profit =%d",profit);
    }
    else{
        printf("Loss =%d",loss);
    }
    return 0;
}
