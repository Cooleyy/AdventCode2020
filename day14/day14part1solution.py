#!/usr/bin/env python3
import sys
import re
from copy import deepcopy

def applyMask(value, mask):
    print("apply mask: " + mask)
    print("value: " + value)
    value = int(value)

    for i, bit in enumerate(reversed(mask)):
        if "X" not in bit:
            bit = int(bit)
            if bit:
                value = value | (1 << i)
            else:
                value = value & ~(1 << i)

    print("Ans:" + str(value))

    return value

def main():
    puzzleInputFile = open(sys.argv[1], 'r')
    puzzleInput = puzzleInputFile.read().splitlines()

    programInstructions = [instruction.split(' = ') for instruction in puzzleInput ]

    mask = ""
    memory = {}
    for instruction in programInstructions:
        if instruction[0] == 'mask':
            mask = instruction[1]
        else:
            memory[instruction[0]] = applyMask(instruction[1], mask)

    print(sum(memory.values()))

if __name__ == "__main__":
    main()