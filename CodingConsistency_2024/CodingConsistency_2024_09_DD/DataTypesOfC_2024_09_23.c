#include <stdio.h>

int main(){
    char myGrade = 'A';
    printf("%c\n", myGrade);

    // ASCII values
    char a = 65, b = 66, c = 67;
    printf("%c", a);
    printf("%c", b);
    printf("%c\n", c);

    char LongText[] = "Hello";
    printf("%s\n", LongText);

    float f1 = 35e3;
    double d1 = 12E4;

    printf("%f\n", f1);  
    printf("%lf\n", d1); 

    return 0;
}

