// finding the largetst palindrome from the product of two 3-digit number
#include <stdio.h>


/**helper function to determine if a number is a palindrome**/
int is_palindrome(int num){
    int  dig;
    int rev = 0;
    int n;
    n = num;
    while(num>0)
    {
    dig = num % 10;
    rev = rev * 10 + dig;
    num = num/10;
    }
    printf("num is %i, rev is %i\t", n, rev);
    if (n == rev) return 1;
    else return 0;
    
}


int main(void){

    int i,k;
    int product=0;
    int max=0;

    for(i=999; i > 0;i--){

        for(k=i; k>0;k--){
            product = i * k;
            printf("prouct is: %d\n",product);
            if(is_palindrome(product) == 1)
            {printf("found product to be %d",product);
            if (product > max)            
                max = product;
            }//return product;
        }
    }
    printf("max is %d", max);
}

