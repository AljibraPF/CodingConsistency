#include <stdio.h>

//Varians of a bunch of

int main() {
    int i;

    printf("Increase loop:\n");
    for (i = 0; i < 5; i++) {
        printf("%d\n", i);
    }

//Decrease
    printf("\nDecrease loop:\n");
    for (i = 4; i >= 0; i--) {
        printf("%d\n", i);
    }

//Multiplication Table

    printf("\nMultiplication table of 2:\n");
    for (i = 1; i <= 5; i++) {
        printf("2 * %d = %d\n", i, 2 * i);
    }

    return 0;
}
