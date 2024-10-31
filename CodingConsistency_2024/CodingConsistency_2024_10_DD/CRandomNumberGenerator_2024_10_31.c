#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//Code to randomly generate number in C

int main() {
    srand((unsigned int) time(0));

    int randomNumber = rand() % 100;

    printf("Random Number: %d\n", randomNumber);

    return 0;
}
