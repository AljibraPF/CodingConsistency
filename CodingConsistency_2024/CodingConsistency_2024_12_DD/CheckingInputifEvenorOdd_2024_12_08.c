#include <stdio.h>

int main() {
    int number;

    printf("Enter Number: ");
    scanf("%d",&number);

    if(number % 2 == 0) {
        printf("Number is an Even number");
    } else {
        printf("Number is an Odd number");
    }

    return 0;
}