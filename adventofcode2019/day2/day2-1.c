#include <stdio.h>
#include <stdlib.h>
#define STEP 3

int main(int argc, char ** argv) {
	char * input_file = (argc > 1) ? argv[1] : "input.txt";
	FILE * fp = fopen(input_file, "r");
	char ch;
	int curr_num = 5;
	
	if (!fp) {
		printf("\nCan not open %s\n", input_file);
		return -1; 	
	}

	printf("\nThe bathroom code is: ");	
	while (!feof(fp)) {
		ch = fgetc(fp);
		if (ch == 'U') {
			if (curr_num > STEP) {
				curr_num -= STEP;
			}			
		}
		else if (ch == 'D') {
			if (curr_num <= (STEP-1)*STEP) {
				curr_num += STEP;
			}		
		}
		else if (ch == 'L') {
			if (curr_num%STEP != 1) {
				--curr_num;		
			}
		}
		else if (ch == 'R') {
			if (curr_num%STEP != 0) {
				++curr_num;
			}
		}
		else if (ch == '\n') {
			printf("%d", curr_num);		
		}
	}
	printf("\n\n");	
	fclose(fp);	
	return 0;
}
