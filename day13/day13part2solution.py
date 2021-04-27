#!/usr/bin/env python3
import sys
import re
from copy import deepcopy

def main():
    puzzleInputFile = open(sys.argv[1], 'r')
    puzzleInput = puzzleInputFile.read().splitlines()

    busIDs = puzzleInput[1].split(",")

    busIDsWithDepartOffset = list(enumerate(busIDs))

    busIDsWithDepartOffset = [(x[0], int(x[1])) for x in busIDsWithDepartOffset if x[1] != 'x']

    valid = 0
    increment = 1

    for bus in busIDsWithDepartOffset:
        while(valid + bus[0]) % bus[1] != 0:
            valid += increment
        increment *= bus[1]

    print(valid)

if __name__ == "__main__":
    main()
