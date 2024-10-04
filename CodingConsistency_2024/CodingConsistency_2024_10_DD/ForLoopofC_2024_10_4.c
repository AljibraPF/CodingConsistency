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

    return 0;
}
