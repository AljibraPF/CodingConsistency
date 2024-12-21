#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//Random picks a day
int main() {
    const char* daysOfWeek[] = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};

    srand(time(0));

    int randomDay = rand() % 7;

    printf("Random day of the week is: %s\n", daysOfWeek[randomDay]);

    return 0;

}