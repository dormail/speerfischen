speerfischen: speerfischen.c speerfischen.h
	gcc speerfischen.c speerfischen.h \
		-lm \
		-pthread \
		-o speerfischen

results-a.csv: speerfischen
	./speerfischen > results-a.csv
