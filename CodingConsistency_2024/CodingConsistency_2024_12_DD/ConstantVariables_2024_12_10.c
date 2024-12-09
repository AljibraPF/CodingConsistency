//Using Const

#include <stdio.h>
#define PI 3.14159

int main() {
    const double radius = 5.0;
    double area;

    area = PI * radius * radius;

    printf("Area of circle with radius %.2f is %2.f\n",radius,area);
    return 0;
}