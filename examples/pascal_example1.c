#include <stdio.h>
#include <stdbool.h>
#include <string.h>

int x;
int y;


int main() {
    x = 5;
    y = x + 10;
    if (y > 10) {
        y = y + 1;
    }
    return 0;
}
