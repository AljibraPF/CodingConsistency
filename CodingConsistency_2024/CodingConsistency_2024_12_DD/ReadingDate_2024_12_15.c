#include <stdio.h>
//Read and input date
int main() {
    int day, month, year;

    printf("Enter the date (DD MM YYYY)");
    scanf("%d %d %d", &day, &month, &year);

    printf("You entered: %02d/%02d/%04d\n", day, month, year);

    return 0;
}