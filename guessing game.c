#include <stdio.h>
int main() {
  int secretnumber=5;
  int guess;
  int guesscount=0;
  int guesslimit=4;
  int outofrange=0;
  
  while (secretnumber!= guess && outofrange ==0)
  { if(guesscount<guesslimit){
  printf("enter a number : ");
  scanf("%d",&guess);
  guesscount++;
  }else
  outofrange=1;}
  
  if (outofrange==1){
      printf("out of range");
  }else
  printf("you win");
   return 0;
}