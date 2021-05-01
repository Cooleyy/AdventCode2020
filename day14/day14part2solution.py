#!/usr/bin/env python3
import sys
import re
from copy import deepcopy

def resolveFloatingBits(address):
    for i, bit in enumerate(address):
        if bit == "X":
            address1 = ["1"] + address[i+1:]
            address0 = ["0"] + address[i+1:]
            return [address[:i] + a for a in resolveFloatingBits(address1)] + [address[:i] + a for a in resolveFloatingBits(address0)]
    return [address]

def applyMask(address, mask):
    print("apply mask: " + mask)
    binaryAddress = bin(int(address))[2:]
    binaryAddress = ("0" * (36 - len(binaryAddress))) + binaryAddress
    print("address: " + binaryAddress)

    binaryAddress = list(binaryAddress)

    for i, bit in enumerate(mask):
        if "X" in bit:
            binaryAddress[i] = bit
        else:
            binaryAddress[i] = str(int(binaryAddress[i]) | int(bit))# if mask bit = 1 then set address bit to 1 /  if mask bit = 0 then keep address bit

    print("AddressWithMask:" + "".join(binaryAddress))

    return resolveFloatingBits(binaryAddress)

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
            insertValue = int(instruction[1])
            memAddress = instruction[0][4:-1]
            for address in applyMask(memAddress, mask):
                memory["".join(address)] = insertValue

    print(sum(memory.values()))

if __name__ == "__main__":
    main()