#include <stdio.h>

//Simple Function Parameter C

int add(int a, int b) {
    return a + b;
}

int main() {
    int x = 5;
    int y = 10;

    int result = add(x,y);

    printf("Sum of %d and %d is %d\n", x,y,result);

    return 0;

}