#include <stdio.h>

//Parameter Float

float average(int a, int b, int c) {
    return (a + b + c) / 3.0;
}

int main() {
    int num1 = 10;
    int num2 = 20;
    int num3 = 30;

    float result = average(num1, num2, num3);

    printf("Average of %d, %d, and %d is %.2f\n", num1, num2, num3, result);

    return 0;
}
