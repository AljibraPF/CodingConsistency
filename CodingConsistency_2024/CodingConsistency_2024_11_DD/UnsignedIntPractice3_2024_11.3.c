#include <stdio.h>

//Sums first positive numbers of n

int main() {
    unsigned int n = 5; 
    unsigned int sum = 0;

    for (unsigned int i = 1; i <= n; i++) {
        sum += i; 
    }

    printf("The sum of the first %u positive numbers is: %u\n", n, sum);

    return 0;
}
