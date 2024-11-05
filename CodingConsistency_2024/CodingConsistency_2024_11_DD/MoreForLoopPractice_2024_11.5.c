#include <stdio.h>
//Printing simple pattern
int main() {
    printf("\nPattern:\n");
    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= i; j++) {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}