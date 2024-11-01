#include <stdio.h>
//Unsigned Integer Practice
int main() {
    unsigned int itemCount = 0; 

    itemCount += 5;
    printf("Added, Current: %u\n", itemCount);  

    itemCount -= 2;
    printf("Removed, Current: %u\n", itemCount);  

    itemCount -= 4;
    printf("Attempted to remove too much, Current: %u\n", itemCount);

    return 0;
}
