#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//Random and Array
int main() {
    int numbers[10];
    int size = sizeof(numbers) / sizeof(numbers[0]);

    srand(time(0));

    for (int i = 0; i < size; i++) {
        numbers[i] = rand() % 100 + 1;

        printf("Random numbers in array: \n");
        for (int i = 0; i < size; i++) {
            printf("%d ", numbers[i]);
        }
        printf("\n");

        return 0;
    }
}