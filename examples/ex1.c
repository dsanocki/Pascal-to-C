#include <stdio.h>
#include <stdbool.h>
#include <string.h>

int x;
int y;


int main() {
    x = 5;
    y = x + 10;
    if (y > 10) {
        printf("%d\n", y);
        y = y + 1;
    }
    printf("%d\n", y);
    return 0;
}
