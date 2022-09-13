#include <stdio.h>
int main(){
    
  double x,y,z;
  
  printf("please enter the 3 numbers :");
  scanf("%lf %lf %lf",&x,&y,&z);
  double sum=x+y+z;
  printf("the sum is %lf ",sum);
  double avg=sum/3;
  printf("\nthe average is %lf",avg);
  return 0;
}
