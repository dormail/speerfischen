/* speerfischen.c start */
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "speerfischen.h"

coordinate *calc_path_given_y(coordinate *origin, double y_end, double angle)
{
	coordinate *end = (coordinate *) malloc(sizeof(coordinate));
	end->y = y_end;
	end->x = origin->x - tan(angle) * (y_end - origin->y);

	return end;
}

//coordinate *calc_path_given_x(coordinate *origin, double x_end, double angle);

int main()
{
	/* variablen
	 * depth = depth of the fish
	 * dist = distance of the fish to the shore
	 * height = height of the fisher's eyes
	 */
	double depth = 1.5;
	double dist = 1.0;
	double height = 2.0;

	double n_wasser = 1.33;
	double n_luft = 1;


	coordinate *x0 = (coordinate *) malloc(sizeof(coordinate));
	coordinate *x1 = (coordinate *) malloc(sizeof(coordinate));
	
	x0->x = dist;
	x0->y = -1. * depth;

	x1 = calc_path_given_y(x0, 0, 0.1);
	printf("%e\n", x1->x);
	

	// free storage
	free(x0);

	return 0;
}

/* speerfischen.c end */
