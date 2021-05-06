#!/usr/bin/env python3
import sys
import re
import itertools
from copy import deepcopy

def main():
    puzzleInputFile = open(sys.argv[1], 'r')
    puzzleInput = puzzleInputFile.read().splitlines()

    print(puzzleInput)

if __name__ == "__main__":
    main()