#!/usr/bin/env python3
import sys
import re

def getYesAnswers(groupForm):
    if len(groupForm) == 1:
        return len(groupForm[0])

    totalUnanimousAnswers = 0
    for letter in groupForm[0]:
        if checkLetterInAll(groupForm, letter):
            totalUnanimousAnswers += 1

    return totalUnanimousAnswers

def checkLetterInAll(forms, letter):
    for form in forms:
        if letter not in form:
            return False
    
    return True


if __name__ == "__main__":
    
    puzzleInputFile = open(sys.argv[1], 'r')
    customsForms = puzzleInputFile.read().split("\n\n")
    
    for i, customsForm in enumerate(customsForms):
        customsForms[i] = customsForm.splitlines()

    totalYesAnswers = 0
    for customsForm in customsForms:
        totalYesAnswers += getYesAnswers(customsForm)

    print(totalYesAnswers)
