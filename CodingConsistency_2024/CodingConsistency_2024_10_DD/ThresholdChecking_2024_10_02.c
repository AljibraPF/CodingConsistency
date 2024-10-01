#include <stdio.h>
#include <stdbool.h> 
//Checking Threshold: Used constant, operators, booleans, and if-else.
int main() {
    const int threshold = 10;

    int number = 15;
    bool isGreaterThanThreshold;

    isGreaterThanThreshold = (number > threshold);

    if (isGreaterThanThreshold) {
        printf("The number %d is greater than the threshold of %d.\n", number, threshold);
    } else {
        printf("The number %d is not greater than the threshold of %d.\n", number, threshold);
    }

    int anotherNumber = 20;
    if (anotherNumber > threshold && anotherNumber % 2 == 0) {

        printf("number %d is even and greater than the threshold.\n", anotherNumber);
    } else {
        printf("number %d is not even or not greater than the threshold.\n", anotherNumber);
    }

    return 0;
}
