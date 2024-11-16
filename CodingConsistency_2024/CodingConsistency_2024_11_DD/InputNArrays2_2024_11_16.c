#include <stdio.h>
//Calculate sum and average of array
int main() {
    int n = 5; 
    int arr[n];
    int sum = 0;
    float average;

    printf("Enter 5 integers:\n");
    for (int i = 0; i < n; i++) {
        printf("Element %d: ", i + 1);
        scanf("%d", &arr[i]);
    }

    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }

    average = (float)sum / n;

    printf("The sum of the numbers is: %d\n", sum);
    printf("The average of the numbers is: %.2f\n", average);

    return 0;
}
