all: plot.pdf plot-2b.pdf

speerfischen: speerfischen.c speerfischen.h
	gcc speerfischen.c speerfischen.h \
		-lm \
		-pthread \
		-o speerfischen

results-a.csv: speerfischen
	./speerfischen > results-a.csv

plot-2a.pdf: 2a.py results-a.csv header-matplotlib.tex matplotlibrc
	TEXINPUTS=$$(pwd): python3 2a.py

plot-2b.pdf: 2b.py results-a.csv header-matplotlib.tex matplotlibrc
	TEXINPUTS=$$(pwd): python3 2b.py

clean:
	rm -rf *.csv speerfischen *.pdf

.PHONY: clean
