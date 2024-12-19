#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//dice roll!
int main() {
    srand(time(0));

    int rollDice = rand() % 6 + 1;
    printf("Rolled a %d\n",rollDice);

    return 0;
}