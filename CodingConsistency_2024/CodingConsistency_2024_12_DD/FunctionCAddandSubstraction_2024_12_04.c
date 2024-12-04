#include <stdio.h>
//Adding and substractions in C
int calculate(int a, int b, char operation) {
    if (operation == '+') {
        return a + b;
    } else if (operation == '-') {
        return a - b;
    } else {
        printf("Invalid Operation(Use ' + ' Or ' - ') \n");
        return 0;
    }

}

int main() {
    int num1 = 10, num2 = 5;
    char op = '-';

    int result = calculate(num1,num2,op);
    printf("Result: %d\n", result);

    return 0;
}