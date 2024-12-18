#include <stdio.h>
#include <stdbool.h>

bool isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <=n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    int number;
    printf("Enter Positiive integer: ");
    scanf("%d", &number);

    if (isPrime(number)) {
        printf("%d is prime number. \n",number);
    } else {
        printf("%d is not prime number", number);
    }

    return 0;
}