#!/bin/bash

zless mapped.bed.gz | awk 'BEGIN {OFS="\t"} {Mean=(1000/($4-$3))*((($9+$10)/2)-$3)-500; print Mean, $12}' > range_of_file.tsv
sort range_of_file.tsv | uniq -c > sorted_range.tsv
awk '{$1=$1; print $1 "\t" $2 "\t" $3}' sorted_range.tsv > sorted_file.tsv | python3 plot.py


