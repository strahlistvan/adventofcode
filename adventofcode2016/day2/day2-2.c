#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define SIZE 5

int main(int argc, char ** argv) {
	char * input_file = (argc > 1) ? argv[1] : "input.txt";
	FILE * fp = fopen(input_file, "r");
	char ch;
	int v_index = 2, h_index = 0;
	char ** grid = (char ** )malloc(SIZE*sizeof(char **));
	grid[0] = "  1  ";
	grid[1] = " 234 ";
	grid[2] = "56789";
	grid[3] = " ABC ";
	grid[4] = "  D  ";

	if (!fp) {
		printf("\nCan not open %s\n", input_file);
		return -1;
	}

	printf("\nThe bathroom code is: ");
	while (!feof(fp)) {
		ch = fgetc(fp);
		if (ch == 'U') {
			if (v_index > 0 && grid[v_index-1][h_index] != ' ') {
				--v_index;
			}
		}
		else if (ch == 'D') {
			if (v_index < SIZE-1 && grid[v_index+1][h_index] != ' ') {
				++v_index;
			}
		}
		else if (ch == 'L') {
			if (h_index > 0 && grid[v_index][h_index-1] != ' ') {
				--h_index;
			}
		}
		else if (ch == 'R') {
			if (h_index < strlen(grid[v_index])-1
                && grid[v_index][h_index+1] != ' ') {
				++h_index;
			}
		}
		else if (ch == '\n') {
			printf("%c", grid[v_index][h_index]);
		}
	}
	printf("\n\n");
	free(grid);
	fclose(fp);
	return 0;
}
