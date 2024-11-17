#include <stdio.h>
#include <string.h>

//Enter number of names, shows the names and reverses it

int main() {
    int n;

    printf("Enter the number of names: ");
    scanf("%d", &n);

    char names[n][50];  

    printf("Enter %d names:\n", n);
    for (int i = 0; i < n; i++) {
        printf("Name %d: ", i + 1);
        scanf("%s", names[i]); 
    }

    printf("Names in reverse order:\n");
    for (int i = n - 1; i >= 0; i--) {
        printf("%s\n", names[i]);
    }

    return 0;
}
