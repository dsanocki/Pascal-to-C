#include <stdio.h>
#include <stdbool.h>
#include <string.h>

int i;
int sum;
int Add(int a, int b) {
    return a + b;
}

int main() {
    sum = 0;
    for (i = 1; i <= 5; i++) {
        sum = Add(sum, i);
    }
    while (sum < 100) {
        sum = sum + 10;
    }
    return 0;
}
