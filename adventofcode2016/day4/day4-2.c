#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define N 26      //alphabet size
#define MAX 200   //maximal string length

char * get_checksum(char *);
int get_room_id(char *);
char * decrypt_name_part(char *, int);

int main(int argc, char ** argv) {
	char * input_file = (argc > 1) ? argv[1] : "input.txt";
	FILE * fp = fopen(input_file, "r");
	char str[MAX], * decrypt;

	if (!fp) {
		printf("\nCan not open %s\n", input_file);
		return -1;
	}

    while (!feof(fp)) {
        fscanf(fp,"%s\n", str);
        decrypt = decrypt_name_part(str, get_room_id(str));

        if (strstr(decrypt, "north") != NULL) {
            printf("%s : %d\n", decrypt, get_room_id(str));
        }
    }
	fclose(fp);
	return 0;
}

struct rec {
    char index;
    int value;
};

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

char shift_char(char ch, int times) {
    int k;
    for (k=0; k<times; ++k) {
        ch = (ch == 'z') ? 'a' : ch+1;
    }
    return ch;
}

/** Decoding name with shift rotation*/
char * decrypt_name_part(char * str, int rotates) {
    static char name[MAX];
    int index = 0;
    while (str[index] < '0' || str[index] > '9') {
        if (str[index] >= 'a' && str[index] <= 'z') {
            str[index] = shift_char(str[index], rotates);
        }
        name[index++] = str[index];
    }
    name[index] = '\0';
    return name;
}
