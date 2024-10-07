#include <stdio.h>
//Looping through an array
int main() {
    int numbers[] = {5, 10, 15, 20, 25};
    int i;

    for (i = 0; i < 5; i++) {
        printf("Element at index %d: %d\n", i, numbers[i]);
    }

    return 0;
}
