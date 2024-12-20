#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//Heads or Tails? 
int main() {

    srand(time(0));

    int coinFlip = rand() % 2;

    if (coinFlip == 0) {
        printf("Heads\n");
    } else {
        printf("Tails\n");
    }

    return 0;
}