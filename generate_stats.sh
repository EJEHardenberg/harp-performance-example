#!/bin/sh

echo "Running Some Tests, bare with me!"
for z in `seq 0 9`;
	do
		curl -so /dev/null -w '%{time_total}\n' http://localhost:9000 >> stats.dat
		printf "."
	done
echo "!"

./stats.gp




