#include <stdio.h>
//Adding and substractions in C

//12/5/2024
//Added Multiplication and Division

//12/6/2024
//Added Input for flexibility

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

    int num1,num2;
    char op;

    printf("\nNum 1: ");
    scanf("%d", &num1);

    printf("\nNum 2: ");
    scanf("%d", &num2);

    printf("\nOperator: ");
    scanf(" %c", &op);

    int result = calculate(num1,num2,op);
    printf("\nResult: %d\n", result);

    return 0;
}



