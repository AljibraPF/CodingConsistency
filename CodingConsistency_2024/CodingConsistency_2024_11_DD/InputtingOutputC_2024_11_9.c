#include <stdio.h>

//Prints out input

int main() {
    char text[100]; 

    printf("Enter some text: ");
    
    fgets(text, sizeof(text), stdin);
    
    printf("You entered: %s", text);

    return 0;
}
