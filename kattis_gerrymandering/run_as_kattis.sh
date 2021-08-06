#!/usr/bin/env bash

declare -i i=1
for filename in input/*.in; do
    echo $filename
    cat $filename | python problem.py > "output/so_${i}.out"
    i+=1
done
$SHELL