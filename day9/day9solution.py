#!/usr/bin/env python3
import sys
import re
from copy import deepcopy

if __name__ == "__main__":
    
    puzzleInputFile = open(sys.argv[1], 'r')
    numList = puzzleInputFile.read().splitlines()
    for i, number in enumerate(numList):
        numList[i] = int(number)
    
    preambleLength = 25
    invalidNumber = 0

    for i, number in enumerate(numList[preambleLength:]):
        validNumber = False
        previousNumbers = numList[i:preambleLength+i]

        for i, n1 in enumerate(previousNumbers[:-1]):
            for n2 in previousNumbers[i+1:]:
                if number == n1 + n2:
                    validNumber = True
                    break

        if not validNumber:
            invalidNumber = number
            break

    sumFirstLast = 0
    for i, startNum in enumerate(numList):
        nextNumPos = i + 1
        setSum = startNum + numList[nextNumPos]
        while(setSum < invalidNumber):
            nextNumPos += 1
            setSum += numList[nextNumPos]
        if setSum == invalidNumber:
            invalidSet = numList[i:nextNumPos+1]
            invalidSet.sort()
            sumFirstLast = invalidSet[0] + invalidSet[-1]
            break

    print(sumFirstLast)
