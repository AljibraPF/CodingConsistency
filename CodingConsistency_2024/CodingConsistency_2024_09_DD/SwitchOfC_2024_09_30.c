#include <stdio.h>
//is used when you have variable that can be compared against multiple vals.
int main() {
    int day = 3;

    switch(day) {
        case 1:
            printf("Senin\n");
            break;
        case 2:
            printf("Selasa\n");
            break;
        case 3:
            printf("Rabu\n");
            break;
        case 4:
            printf("Kamis\n");
            break;
        case 5:
            printf("Jumat\n");
            break;
        case 6:
            printf("Sabtu\n");
            break;
        case 7:
            printf("Minggu\n");
            break;
        default:
            printf("Invalid day\n");
    }

    return 0;
}
