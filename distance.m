% distance.m
% script calculating the distance between the fish and what the fisher sees

a_a = 0.31213759999999996
a_b = 0.3199955781753592

dist = 1; depth = 1.5;

r = [0, 2, 0]; % fisher's eyes
a_a = [sin(a_a), -1 * cos(a_a), 0]; % direction the fisher looks at
a_b = [sin(a_b), -1 * cos(a_b), 0]; % direction the fisher looks at
fish = [dist, -1 * depth, 0];

d1 = norm(cross(a_a, (r-fish))) / norm(a_a)
d2 = norm(cross(a_b, (r-fish))) / norm(a_b)
