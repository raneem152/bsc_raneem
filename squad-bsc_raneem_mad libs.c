#include <stdio.h>
int main(){
    
   char color[20];
   char pnoun[20];
   char name[20];
   
   printf("enter the color :" );
   scanf("%s",color);
   printf("enter the pnoun :" );
   scanf("%s",pnoun);
   printf("enter the name :" );
   scanf("%s",name);
   
   printf("roses are %s\n",color);
   printf("%s are adorable\n", pnoun);
   printf("i love %s",name);
   
   return 0;
}