#include <stdio.h>

int main(){
    int x = 30;
    int y = 50;
    if (x <= y){
        printf("x is alot bigger then y\n");
    } else {
        printf("x is smaller then y\n");
    }

    int timeofday = 30;
    if (timeofday < 10) {
        printf("Good morning.");
    } else if (timeofday < 20) {
        printf("Good day.");
    } else {
        printf("Good evening.");
    }
}