#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#define MAX_SIZE 10
#define PI 3.14159
int globalInt;
int i;
float globalReal;
bool globalBool;
int vector[10 + 1];
float ComputeValue(int x) {
    float temp;
    if (x > 0) {
        temp = x * PI;
    } else {
        temp = -1.0;
    }
    return temp;
}

void ProcessVector(int limit) {
    int k;
    for (k = 1; k <= limit; k++) {
        vector[k] = k * 2;
    }
}

int main() {
    globalInt = 10;
    globalBool = false;
    globalReal = 0.0;
    ProcessVector(MAX_SIZE);
    i = 1;
    while (i <= MAX_SIZE) {
        globalReal = globalReal + vector[i];
        i = i + 1;
    }
    do {
        globalInt = globalInt - 1;
    } while (!(globalInt == 0));
    switch (globalInt) {
        case 0:
            globalBool = true;
            break;
        case 1:
            globalBool = false;
            break;
        default:
            globalBool = false;
            break;
    }
    return 0;
}
