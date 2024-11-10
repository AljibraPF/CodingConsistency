#include <stdio.h>

//Inputting Data
int main() {

    char name[50];
    printf("What is your name? ");
    fgets(name, sizeof(name), stdin);

    printf("Hello, %s\n", name);

    int num1, num2;
    printf("Enter the first number: ");
    scanf("%d", &num1);
    printf("Enter the second number: ");
    scanf("%d", &num2);
    
    int sum = num1 + num2;
    printf("The sum of %d and %d is: %d\n", num1, num2, sum);

    return 0;
}
