#!/usr/bin/env python3
import sys
import re

def bagContains(bag):
    bagsContained = 0
    if rulesDict[bag] == "no other bags.":
        return bagsContained

    bagsWithin = rulesDict[bag].split(", ")
    for bagWithin in bagsWithin:
        noOfBagWithin = int(bagWithin[0])
        bagWithin = bagWithin[2:].split(" bag")[0]
        bagsContained += noOfBagWithin
        bagsContained += noOfBagWithin * bagContains(bagWithin)
    return bagsContained

if __name__ == "__main__":
    
    puzzleInputFile = open(sys.argv[1], 'r')
    rules = puzzleInputFile.read().splitlines()
    
    rulesDict = {}
    for rule in rules:
        rule = rule.split(" bags contain ")
        rulesDict[str(rule[0])] = rule[1]

    targetBag = "shiny gold"

    noOfValidBags = bagContains(targetBag)

    print(noOfValidBags)
