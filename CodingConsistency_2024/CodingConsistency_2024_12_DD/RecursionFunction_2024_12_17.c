#include <stdio.h>

// Function to calculate factorial using recursion

int factorial(int n) {
    if (n == 0 || n == 1) { 
        return 1;
    }
    return n * factorial(n - 1); 
}

int main() {
    int number;

    printf("Enter a positive integer: ");
    scanf("%d", &number);

    if (number < 0) {
        printf("Factorial is not defined for negative numbers.\n");
    } else {
        printf("The factorial of %d is %d\n", number, factorial(number));
    }

    return 0;
}
