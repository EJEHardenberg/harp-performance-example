#!/usr/bin/gnuplot

set terminal dumb
set ylabel "Clock Time (m/s)"
set xlabel "Number"
plot "stats.dat" with lines
