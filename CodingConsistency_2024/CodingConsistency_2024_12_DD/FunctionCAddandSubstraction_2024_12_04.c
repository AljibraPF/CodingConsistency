#include <stdio.h>
//Adding and substractions in C
//12/5/2024
//Added Multiplication and Division
int calculate(int a, int b, char operation) {
    if (operation == '+') {
        return a + b;
    } else if (operation == '-') {
        return a - b;
    } else if (operation == '*') {
        return a * b;
    } else if (operation == '/') {
        return a / b;
    } else {
        return printf("Not a Valid Operator");
        return 0;
    }
}

int main() {
    int num1 = 10, num2 = 5;
    char op = '/';

    int result = calculate(num1,num2,op);
    printf("Result: %d\n", result);

    return 0;
}



