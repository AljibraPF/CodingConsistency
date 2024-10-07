#include <stdio.h>
//Variants of C
int main() {
    int numbers[5] = {10, 20, 30, 40, 50};

    printf("Original array values:\n");
    for (int i = 0; i < 5; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");

    for (int i = 0; i < 5; i++) {
        numbers[i] += 5;  
    }

    printf("Modified array values:\n");
    for (int i = 0; i < 5; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");

    return 0;
}
