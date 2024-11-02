#include <stdio.h>
//Find even numbers by limit
int main() {
    unsigned int limit = 10;  // Limit for loop
    unsigned int evenNumber;

    printf("Even numbers up to %u:\n", limit);

    for (evenNumber = 0; evenNumber <= limit; evenNumber += 2) {
        printf("%u ", evenNumber);
    }

    printf("\n");
    return 0;
}
