#!/usr/bin/env python3
import sys
import re
from copy import deepcopy

def main():
    puzzleInputFile = open(sys.argv[1], 'r')
    puzzleInput = puzzleInputFile.read().split(",")

    lastSpoken = {}

    for i, num in enumerate(puzzleInput, 1):
        lastSpoken[int(num)] = i

    nextNum = 0
    turn = len(puzzleInput) + 1
    lastNum = 0

    while(turn < 30000000):
        if nextNum in lastSpoken:
            lastNum = nextNum
            nextNum = turn - lastSpoken[nextNum]
            lastSpoken[lastNum] = turn
        else:
            lastSpoken[nextNum] = turn
            nextNum = 0
        turn += 1
    
    print(nextNum)

if __name__ == "__main__":
    main()