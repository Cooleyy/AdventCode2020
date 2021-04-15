#!/usr/bin/env python3
import sys
import re
from copy import deepcopy

if __name__ == "__main__":

    puzzleInputFile = open(sys.argv[1], 'r')
    adapters = puzzleInputFile.read().splitlines()
    adapters = list(map(int, adapters))
    adapters.sort()

    currentRating = 0
    targetRating = adapters[-1] + 3

    joltDiffs = {1: 0, 2: 0, 3: 1}#difference in jolts between adapters, built in is always 3 away so begin with 1 3 diff

    for adapter in adapters:
        diff = adapter - currentRating
        if diff <= 3:
            joltDiffs[diff] += 1
            currentRating = adapter
        else:
            print("Error: diff = " + diff)
            break

    print(joltDiffs)
    print(joltDiffs[1] * joltDiffs[3])
