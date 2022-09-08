#include<stdio.h>
int main()
{
    char op;
    float n1,n2,res=0;
      printf("please enter the operator as +,-,*,/: ");
    scanf("%c",&op);
    printf("please enter the two numbers: ");
    scanf("%f %f",&n1,&n2);
  
    switch(op){
        case '+': res=n1+n2;
           break;
        case '-': res=n1-n2;
           break;

        case '*': res=n1*n2;
            break;
        case '/': res=n1/n2;
            break;
        
        default: printf("\n Invalid Operator ");
    }
    printf("the value is = %f" ,res);
    return 0;
}