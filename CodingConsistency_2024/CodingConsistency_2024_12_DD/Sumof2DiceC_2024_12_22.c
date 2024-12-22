#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//Rolling 2 Dice and calculates sum
int main() {

    srand(time(0));

    int dice1 = rand() % 6 + 1;
    int dice2 = rand() % 6 + 1;

    int sum = dice1 + dice2;

    printf("You rolled: %d and %d\n", dice1, dice2);
    printf("The sum of the dicei is: %d\n", sum);

    return 0;
}