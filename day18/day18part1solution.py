#!/usr/bin/env python3
import sys
import re
import itertools
from copy import deepcopy

def FindEndingPara(expression, endPos):
    openPara = 0
    for i, char in enumerate(expression):
        if char == "(":
            openPara += 1
        elif char == ")":
            if openPara == 0:
                endPos += i
                break
            openPara -= 1
    return endPos

def Solve(expression):
    while(len(expression) > 1):
        #print(expression)
        if "(" in expression[:3]:
            if expression[0] == "(":
                endPos = FindEndingPara(expression[1:], 1)
                expression[:endPos+1] = Solve(expression[1:endPos])
            elif expression[2] == "(":
                endPos = FindEndingPara(expression[3:], 3)
                expression[2:endPos+1] = Solve(expression[3:endPos])
        elif expression[1] == "+":
            expression[:3] = [expression[0] + expression[2]]
        else:
            expression[:3] = [expression[0] * expression[2]]
    #print(expression)
    return expression

def main():
    puzzleInputFile = open(sys.argv[1], 'r')
    puzzleInput = puzzleInputFile.read().splitlines()

    sumExpressions = 0
    for expression in puzzleInput:
        expression = [c if c in "()+*" else int(c) for c in list(expression) if c != " "]
        sumExpressions += Solve(expression)[0]

    print(sumExpressions)

if __name__ == "__main__":
    main()