#include <stdio.h>
#define MULTIPLIER 2
//Calculate perimeter and area of rectangle
int main() {
    const int length = 10;
    const int width = 5;
    int perimenter,area;

    perimenter = MULTIPLIER * (length + width);
    area = length * width;

    printf("Rectangle dimensions: %d x %d\n",length,width);
    printf("Perimeter: %d units\n", perimenter);
    printf("Area: %d square units\n", area);

    return 0;
}