#include <stdio.h>
//More descriptive version of the date
int main() {
    int day, month, year;

    printf("Enter the day (1-31:) ");
    scanf("%d", &day);

    printf("Enter the month (1-12): ");
    scanf("%d", &month);

    printf("Enter the year: ");
    scanf("%d", &year);

    printf("The date you entered is %02d-%02d-%04d\n", day, month, year);

    return 0;
}