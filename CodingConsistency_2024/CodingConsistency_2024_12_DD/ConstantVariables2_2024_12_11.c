#include <stdio.h>
//Temperature Conversion
#define FAHRENHEIT_OFFSET 32   
#define CONVERSION_FACTOR 1.8

int main() {
    const double celsius = 25.0;
    double fahrenheit;

    fahrenheit = (celsius * CONVERSION_FACTOR) + FAHRENHEIT_OFFSET;
    printf("%.2f Celcius is equal to %.2f Fahrenheit\n", celsius, fahrenheit);

    return 0;

}