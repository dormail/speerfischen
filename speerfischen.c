/* speerfischen.c start */
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "speerfischen.h"

#define PI 3.14159265

coordinate *calc_path_given_y(coordinate *origin, double y_end, double angle)
{
	coordinate *end = (coordinate *) malloc(sizeof(coordinate));
	end->y = y_end;
	end->x = origin->x - tan(angle) * (y_end - origin->y);

	return end;
}

coordinate *calc_path_given_x(coordinate *origin, double x_end, double angle)
{
	coordinate *end = (coordinate *) malloc(sizeof(coordinate));
	angle = PI/2 - angle;

	end->x = x_end;
	end->y = origin->x + tan(angle) * (origin->x - x_end);
	
	return end;
}

double refraction(double n1, double n2, double angle_orig)
{
	if(n2 == 0) return -1;
	double t2 = asin(sin(angle_orig) * n1 / n2);
	return t2;
}

double calc_path_a(coordinate *fish, double a)
{
	coordinate *x1 = (coordinate *) malloc(sizeof(coordinate));
	coordinate *x2 = (coordinate *) malloc(sizeof(coordinate));
	double b;
	double n1 = 1.33;
	double n2 = 1;

	x1 = calc_path_given_y(fish, 0, a);
	printf("%e, ", x1->x);
	b = refraction(n1, n2, a);
	printf("%e, ", b);
	x2 = calc_path_given_x(x1, 0, b);
	printf("%e\n", x2->y);

	double h = x2->y;

	free(x1);
	free(x2);

	return h;
}


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

	double h;

	coordinate *fish = (coordinate *) malloc(sizeof(coordinate));
	fish->x = dist;
	fish->y = -1 * depth;

	printf("a, x1, b, y2\n");
	for(double a = 0.2; a < 0.3; a += 0.01)
	{
		printf("%e, ", a);
		h = calc_path_a(fish, a);
	}

	free(fish);

	return 0;
}

/* speerfischen.c end */
