#!/bin/bash
# it is possible to give args to the script during execution 
# i.e ./main.sh pink red yellow
echo "Number of entered colours are: $#"
for colour in $@ #$@reps all args as a single entity
do
	echo "Entered colours are: $colour"
done
