#include <stdio.h>
//Constants? Huh? I Guess Python never had this.

int main(){
    const int randomNum = 10;
    const float Phi = 3.14;
    const int MinutesInaHour = 60;
    //randomNum = 15; Won't change and will produce error
    printf("Testing %d",randomNum);
}