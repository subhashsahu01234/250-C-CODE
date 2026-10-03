#include <stdio.h>
int main(void) {
  float a, b, c;
  printf("Enter first side of triangle ");
  scanf("%f", &a);
  printf("Enter second side of triangle ");
  scanf("%f", &b);
  printf("Enter third side of triangle ");
  scanf("%f", &c);

  if (a > 0 && b > 0 && c > 0 && (a + b > c) && (a + c > b) && (b + c > a)) {
    printf("Sides are valid");
  } else {
    printf("Sides are invalid");
  }
  return 0;
}