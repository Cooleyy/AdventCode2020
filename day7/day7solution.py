#!/usr/bin/env python3
import sys
import re

def bagValid(bag):
    if rulesDict[bag] == "no other bags.":
        return False
    elif targetBag in rulesDict[bag]:
        return True
    else:
        bagsWithin = rulesDict[bag].split(", ")
        for bagWithin in bagsWithin:
            bagWithin = bagWithin[2:].split(" bag")[0]
            if bagValid(bagWithin):
                return True
    return False

if __name__ == "__main__":
    
    puzzleInputFile = open(sys.argv[1], 'r')
    rules = puzzleInputFile.read().splitlines()
    
    rulesDict = {}
    for rule in rules:
        rule = rule.split(" bags contain ")
        rulesDict[str(rule[0])] = rule[1]

    targetBag = "shiny gold"

    noOfValidBags = 0
    for rule in rulesDict.keys():
        if bagValid(rule):
            noOfValidBags += 1

    print(noOfValidBags)
