#include<stdio.h>
int main(){
    int sub[3][3],a[3][3],b[3][3];
    int i,j;
    printf("Enter element of the first matrix:\n");

    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            scanf("%d",&a[i][j]);
        }
    }
    printf("Enter element of the second matrix");
    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            scanf("%d",&b[i][j]);
        }
    }
    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            sub[i][j]=a[i][j]-b[i][j];
        }
    }
    printf("substraction of matrices:\n");

    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            printf("%d ",sub[i][j]);
        }
        printf("\n");
    }
    return 0;
}