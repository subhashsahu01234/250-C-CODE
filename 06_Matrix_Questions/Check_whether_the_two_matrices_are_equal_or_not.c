#include<stdio.h>
int main(){
    int a[3][3],b[3][3];
    int i,j;

    printf("Enter element of the first matrix:\n");
    
    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            scanf("%d",&a[i][j]);
        }
    }

    printf("Enter element of the second matrix:\n");

    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            scanf("%d",&b[i][j]);
        }
    }

    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            if (a[i][j] == b[i][j]) {
                printf("Matrices are equal");
    }       
            else {
                printf("Matrices are not equal");
    }
        }
    }
    
    return 0;
       
}