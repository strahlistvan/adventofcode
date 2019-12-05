#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define N 26      //alphabet size
#define MAX 200   //maximal string length
#define LENGTH 5  //checksum length

char * get_checksum(char * str);
int get_room_id(char * str);

int main(int argc, char ** argv) {
	char * input_file = (argc > 1) ? argv[1] : "input.txt";
	FILE * fp = fopen(input_file, "r");
	char str[MAX], * chk_sum, * chk_sum_real;
	int sum = 0;

	if (!fp) {
		printf("\nCan not open %s\n", input_file);
		return -1;
	}

    while (!feof(fp)) {
        fscanf(fp,"%s\n", str);
        chk_sum = get_checksum(str);

        if (strstr(str, chk_sum) != NULL) {
           sum += get_room_id(str);
        }
    }
    printf("\nSum of the room\'s sector id: %d\n", sum);
	fclose(fp);
	return 0;
}

struct rec {
    char index;
    int value;
};

void swap(struct rec * a, struct rec * b) {
    struct rec tmp= *a;
    *a = *b;
    *b = tmp;
}

/** Calculate the room's checksum */
char * get_checksum(char * str) {
    static char chk_sum[LENGTH];
    char i, j, max_j;
    struct rec counts[N];
    struct rec max_rec;

    for (i=0; i<N; ++i) {
        counts[i].index = i+'a';
        counts[i].value = 0;
    }

    for (i=0; i<strlen(str) && str[i] !='['; ++i) {
        if (str[i] >= 'a' && str[i] <= 'z') {}
            ++counts[ str[i]-'a' ].value;
    }
        //Partial max selection sort (for the first LENGTH (5) element)
        for (i=0; i<LENGTH; ++i) {
            max_rec = counts[i];
            max_j = i;
            for (j=i+1; j<N; ++j) {
                if (max_rec.value < counts[j].value) {
                    max_rec = counts[j];
                    max_j = j;
                }
                if (max_rec.value == counts[j].value
                    && max_rec.index > counts[j].index)
                {
                    max_rec = counts[j];
                    max_j = j;
                }
            }
            swap(&counts[i], &counts[max_j]);
        }
    //fill chk_sum string
    for (i=0; i<LENGTH; ++i) {
        chk_sum[i] = counts[i].index;
    }
    chk_sum[LENGTH] = '\0';
    return chk_sum;
}

/** Return the number part from the string */
int get_room_id(char * str) {
    int i, id = 0;
    for (i=0; i<strlen(str); ++i) {
        if (str[i] >= '0' && str[i] <= '9') {
            id *= 10;
            id += str[i] - '0';
        }
    }
    return id;
}
