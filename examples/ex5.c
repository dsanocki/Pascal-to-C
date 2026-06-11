#include <stdio.h>
#include <stdbool.h>
#include <string.h>

int n;
int resultFact;
int resultFibo;
int Factorial(int n) {
    if (n <= 1) {
        return 1;
    } else {
        return n * Factorial(n - 1);
    }
}

int Fibonacci(int n) {
    int a;
    int b;
    int temp;
    int i;
    if (n <= 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    } else {
        a = 0;
        b = 1;
        for (i = 2; i <= n; i++) {
            temp = a + b;
            a = b;
            b = temp;
        }
        return b;
    }
}

int main() {
    n = 6;
    resultFact = Factorial(n);
    resultFibo = Fibonacci(n);
    printf("%d\n", resultFact);
    printf("%d\n", resultFibo);
    return 0;
}
