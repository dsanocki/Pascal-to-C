#include <stdio.h>
#include <stdbool.h>
#include <string.h>

int MojaTablica[5 + 1];
int i;
int j;
int temp;


int main() {
    MojaTablica[1] = 42;
    MojaTablica[2] = 12;
    MojaTablica[3] = 89;
    MojaTablica[4] = 23;
    MojaTablica[5] = 11;
    for (i = 1; i <= 4; i++) {
        for (j = 1; j <= 5 - i; j++) {
            if (MojaTablica[j] > MojaTablica[j + 1]) {
                temp = MojaTablica[j];
                MojaTablica[j] = MojaTablica[j + 1];
                MojaTablica[j + 1] = temp;
            }
        }
    }
    printf("Posortowana tablica:\n");
    for (i = 1; i <= 5; i++) {
        printf("%d ", MojaTablica[i]);
    }
    return 0;
}
