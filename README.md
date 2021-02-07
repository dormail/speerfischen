# speerfischen
Monte Carlo simulation of the spearfisher.

## Calculations
The pathes themselves are based on straight propagation inside each media. Since 
we have simple shapes for the media (the media are different layers with
set borders on y values) each fraction point can be calulated with a linear 
function for the line-of-sight propagation.<br>

For calculating the refraction angles the programm uses
[Snell's law](https://en.wikipedia.org/wiki/Snell%27s_law).
