#!/bin/bash

dayNum="$1"

echo "Attempting to create template for day $dayNum"

if (($dayNum < 1 || $dayNum > 25)); 
then
    echo "day$dayNum not valid"
    exit 1
fi

if [[ -d "./day$dayNum" ]]
then
    echo "day$dayNum already exists"
    exit 1
fi

mkdir "./day$dayNum"

touch "./day$dayNum/puzzleInput.txt"
touch "./day$dayNum/test.txt"

cp "./template.py" "./day$dayNum/day${dayNum}part1solution.py"

chmod  777 "./day$dayNum/day${dayNum}part1solution.py"

echo "day$dayNum template created"