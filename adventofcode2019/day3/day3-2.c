#include <stdio.h>
#include <stdlib.h>

void sort3num(int * a, int * b, int * c);

int main(int argc, char ** argv) {
	char * input_file = (argc > 1) ? argv[1] : "input.txt";
	FILE * fp = fopen(input_file, "r");
	int i, tr1[3], tr2[3], tr3[3], counter = 0;

	if (!fp) {
		printf("\nCan not open %s\n", input_file);
		return -1;
	}

	while (!feof(fp)) {
        for (i=0; i<3; ++i) {
            fscanf(fp,"%d %d %d\n", &tr1[i], &tr2[i], &tr3[i]);
        }
        printf("Triangle 1: %d %d %d\n", tr1[0], tr1[1], tr1[2]);
        printf("Triangle 2: %d %d %d\n", tr2[0], tr2[1], tr2[2]);
        printf("Triangle 3: %d %d %d\n", tr3[0], tr3[1], tr3[2]);

        sort3num(&tr1[0], &tr1[1], &tr1[2]);
        if (tr1[0] + tr1[1] > tr1[2]) {
            ++counter;
        }
        sort3num(&tr2[0], &tr2[1], &tr2[2]);
        if (tr2[0] + tr2[1] > tr2[2]) {
            ++counter;
        }
        sort3num(&tr3[0], &tr3[1], &tr3[2]);
        if (tr3[0] + tr3[1] > tr3[2]) {
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
