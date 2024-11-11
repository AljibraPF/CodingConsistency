#include <stdio.h>
//Simple Array C Code
int main() {
    int numbers[5] = {10, 20, 30, 40, 50};  
    int sum = 0;

    for (int i = 0; i < 5; i++) {
        sum += numbers[i];
    }

    printf("The sum of the array elements is: %d\n", sum);

    return 0;
}
