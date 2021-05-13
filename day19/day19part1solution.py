#!/usr/bin/env python3
import sys
import re
import itertools
from copy import deepcopy
from operator import itemgetter

def Check(message, ruleToCheck, rules):
    #print(message, ruleToCheck)

    if "|" in ruleToCheck:
        rule1, rule2 = itemgetter(0, 1)(ruleToCheck.split(" | "))
        valid, noChars = Check(message, rule1, rules) 
        if valid:
            return valid, noChars
        else:
            valid, noChars = Check(message, rule2, rules)
            return valid, noChars
    elif "\"" not in ruleToCheck:
        totalCharsChecked = 0
        for rule in ruleToCheck.split():
            valid, noChars = Check(message, rules[rule], rules)
            totalCharsChecked += noChars

            if valid:
                message = message[noChars:]
            else:
                return False, 1
    else:
        return message.startswith(ruleToCheck[1]), 1
    
    return True, totalCharsChecked
    

def main():
    puzzleInputFile = open(sys.argv[1], 'r')
    puzzleInput = puzzleInputFile.read().split("\n\n")
    rules = {rule.split(": ")[0]: rule.split(": ")[1] for rule in puzzleInput[0].splitlines()}
    messages = puzzleInput[1].splitlines()

    validMessages = []
    ruleToCheckIndex = "0"
    for message in messages:
        valid, totalCharsChecked = Check(message, rules[ruleToCheckIndex], rules)
        if valid and totalCharsChecked == len(message):
            #print("valid: ", message)
            validMessages.append(message)

    #print(validMessages)
    print(len(validMessages))

if __name__ == "__main__":
    main()