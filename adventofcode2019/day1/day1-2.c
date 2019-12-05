#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define DIR_COUNT 4
#define MAX 10000

typedef enum {NORTH, EAST, SOUTH, WEST} direction;

typedef struct position {
    int x;
    int y;
    direction face;
} position;

int main(int argc, char ** argv) {
    char ch, found = 0;
    int dist = 0;
    char * input_file = (argc <= 1) ? "input.txt" : argv[1];
    position * pos = (position *) malloc(sizeof(position));
    position * visited_pos = (position *) malloc(MAX * sizeof(position));
    int i, j, vis_index = 0;

    visited_pos[0] = *pos;

    pos->x = pos->y = 0;
    pos->face = NORTH;

    FILE * fp = fopen(input_file, "r");
    if (!fp) {
        printf("\nCan not open %s\n\n", input_file);
        return -1;
    }

    while (!feof(fp) && !found) {
        ch = fgetc(fp);
        if (ch == 'R' || ch == 'L') {

            pos->face = (ch=='R')? (pos->face+1)%DIR_COUNT :
                                   (pos->face-1)%DIR_COUNT;
           fscanf(fp, "%d", &dist);

           //Save all visited corners
           for (i = 0; i < dist; ++i) { 
           	switch (pos->face) {
            	case NORTH :
                	pos->y ++;
                	break;
                case EAST :
                	pos->x ++;
                	break;
                case SOUTH :
                	pos->y --;
                	break;
                case WEST:
                	pos->x --;
                	break;
              	default:
                	printf("\nInvalid direction!\n\n");
            }
            visited_pos[++vis_index] = *pos;
            
            //Is this corner visited before?
            for (j = 0; j < vis_index; ++j) {
                if (pos->x == visited_pos[j].x
                    && pos->y == visited_pos[j].y){
                    printf("\nFirst corner visited twice (x: %d, y: %d) dist.(|x|+|y|): %d\n\n", 
							pos->x, pos->y, abs(pos->x) + abs(pos->y));
                    return 0;
                }
            }

	    }
        }
    }
    printf("There is no corner visited twice\n\n");
    fclose(fp);
    free(visited_pos);
    free(pos);
    return 0;
}
