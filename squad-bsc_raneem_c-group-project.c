
#include <stdio.h>
#include <math.h>

void RightTriangle(int height)
{
    
    int i,j;
      for(i = 1; i <= height; i++) {
      for(j = 1; j <= i; j++)
         printf("* ");

      printf("\n");
   }
}
void square(int height)
{
    
    int  i, j;

 
    
 
    for (i = 1; i <= height; i++) {
        for (j = 1; j <= height; j++) {
            if (i == 1 || i == height || j == 1 || j == height)
                printf("* ");
            else
                printf("  ");
        }
        printf("\n");
    }
}
void pyramid(int rows)
{
    
    int i, j, k = 0;  
       
      
    for ( i =1; i <= rows; i++)  
    {  
        for ( j = 1; j <= rows - i; j++)  
        {  
            printf ("  ");   
        }  
     
        for ( k = 1; k <= ( 2 * i - 1); k++)  
        {  
            printf ("* ");
        }  
        printf ("\n");  
    }
}
void circle(int diameter)
{
   
    
    int i,j;
    for (i=0; i<=diameter; i++)
    {
        for (j=0; j<=diameter; j++)
        {
            double distance = sqrt((i-(diameter/2))*(i-(diameter/2)) + (j-(diameter/2))*(j-(diameter/2)));
            if (distance>(diameter/2)-0.5 && distance<(diameter/2)+0.5)
            {
                printf("*");
            }
            else
            { printf(" ");}
        }
        printf("\n");
    }
}
struct circle
{
    int diameter;
};
struct square
{
    int height;
};
struct pyramids
{
    int rows;
};
struct RightTriangle
{
    int height;
};


int main()
{
    struct circle c;
    struct square s;
    struct pyramids p;
    struct RightTriangle r;
        
        
    
        
    
    
    char shape;
    while (shape!='r' || shape!='c' || shape!='s' || shape!='p' ){
    printf("please choose from cirlce (c) square (s) right angle triangle (r) pyramid (p) : ");
    scanf("%s",&shape);
    if(shape=='r')
    {
        
         printf("enter height : ");
        scanf("%d",&r.height);
        
        RightTriangle(r.height);
    }
    else if(shape=='s')
    {
        
         printf("enter height : ");
         scanf("%d",&s.height);
        square(s.height);
    }
    else if(shape=='p')
    {
         
         printf("enter rows : ");
         scanf("%d",&p.rows);
        
        pyramid(p.rows);

    }
    else if(shape=='c')
    {
        
         printf("enter diameter : ");
         scanf("%d",&c.diameter);
         
        
        circle(c.diameter);
    }
     else {
        printf("please enter a shape from the choices :) \n");
    }
    }
   
   
    
}