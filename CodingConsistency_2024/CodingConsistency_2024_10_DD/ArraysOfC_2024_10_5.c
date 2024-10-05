#include <stdio.h>

int main() {
    int firstArray[] = {25,50,75,100};
    firstArray[0] = 33;

    int i;
    for (i =0; i < 4; i++) {
        printf("%d\n", firstArray[i]);
    }
    
}