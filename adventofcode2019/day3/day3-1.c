#include <stdio.h>
#include <stdlib.h>

void sort3num(int * a, int * b, int * c);

int main(int argc, char ** argv) {
	char * input_file = (argc > 1) ? argv[1] : "input.txt";
	FILE * fp = fopen(input_file, "r");
	int a, b, c, counter = 0;

	if (!fp) {
		printf("\nCan not open %s\n", input_file);
		return -1;
	}

	while (!feof(fp)) {
		fscanf(fp,"%d %d %d\n", &a, &b, &c);

        sort3num(&a, &b, &c);
        if (a + b > c) {
            ++counter;
        }
	}
	printf("\n%d possible triangles are in the list\n", counter);
	fclose(fp);
	return 0;
}

void sort3num(int * a, int * b, int * c) {
    if (*a > *b) {
        *a += *b;
        *b = *a - *b;
        *a -= *b;
    }
    if (*a > *c) {
        *a += *c;
        *c = *a - *c;
        *a -= *c;
    }
    if (*b > *c) {
        *b += *c;
        *c = *b - *c;
        *b -= *c;
    }
}
