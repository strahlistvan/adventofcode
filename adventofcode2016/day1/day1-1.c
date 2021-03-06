#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define DIR_COUNT 4

typedef enum {NORTH, EAST, SOUTH, WEST} direction;

typedef struct position {
    int x;
    int y;
    direction face;
} position;

int main(int argc, char ** argv) {
    char ch;
    int dist = 0;
 	char * input_file = (argc <= 1) ? "input.txt" : argv[1];
    position * pos = (position *) malloc(sizeof(position));
 	
	pos->x = pos->y = 0;
    pos->face = NORTH;

    FILE * fp = fopen(input_file, "r");
    if (!fp) {
        printf("\nCan not open %s\n\n", input_file);
        return -1;
    }

    while (!feof(fp)) {
        ch = fgetc(fp);
        if (ch == 'R' || ch == 'L') {
            pos->face = (ch=='R')? (pos->face+1)%DIR_COUNT :
                                        (pos->face-1)%DIR_COUNT;
           fscanf(fp, "%d", &dist);
            switch (pos->face) {
              case NORTH :
                pos->y += dist;
                break;
              case EAST :
                pos->x += dist;
                break;
              case SOUTH :
                pos->y -= dist;
                break;
              case WEST:
                pos->x -= dist;
                break;
              default:
                printf("\nInvalid direction!\n\n");
            }
        }
    }
    printf("\nx: %d, y: %d, dist.(|x|+|y|): %d\n\n", pos->x, pos->y,
            abs(pos->x) + abs(pos->y));

    fclose(fp);
    free(pos);
    return 0;
}
