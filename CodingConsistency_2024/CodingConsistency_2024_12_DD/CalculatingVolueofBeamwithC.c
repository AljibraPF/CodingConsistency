#include <stdio.h>

int main() {
    float length,width,height,volume;

    printf("Length of beam: ");
    scanf("%f", &length);

    printf("Width of beam: ");
    scanf("%f", &width);

    printf("Height of beam: ");
    scanf("%f", &height);

    volume = length * width * height;

    printf("Volume of beam is %.2f cubic meters.\n", volume);

}