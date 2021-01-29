/* speerfischen.h start */

typedef struct coordinate
{
	double x,y;
} coordinate;

coordinate *calc_path_given_y(coordinate *origin, double y_end, double angle);
coordinate *calc_path_given_x(coordinate *origin, double x_end, double angle);

/* speerfischen.h end */
