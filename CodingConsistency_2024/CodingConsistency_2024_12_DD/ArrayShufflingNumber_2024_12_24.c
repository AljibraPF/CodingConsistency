#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//Shuffling
int main() {
    int numbers[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}; 
    int size = sizeof(numbers) / sizeof(numbers[0]);

    srand(time(0));

    printf("Original array:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");

    for (int i = 0; i < size; i++) {
        int randomIndex = rand() % size; 
        int temp = numbers[i];
        numbers[i] = numbers[randomIndex];
        numbers[randomIndex] = temp;
    }

    printf("Shuffled array:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");

    return 0;
}
