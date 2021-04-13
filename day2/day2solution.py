#!/usr/bin/env python3
import sys

passwordsFile = open (sys.argv[1], 'r')

passwordAndRules = passwordsFile.read().splitlines()

counter = 0
for item in passwordAndRules:
    passAndRule = item.split()
    passAndRule[0] = list(map(int, passAndRule[0].split("-")))
    passAndRule[1] = passAndRule[1][0]
    passwordAndRules[counter] = passAndRule
    counter += 1

numValid = 0
for password in passwordAndRules:
    ##numOfLetter = password[2].count(password[1])
    ##if numOfLetter < password[0][0] or numOfLetter > password[0][1]:
    if (password[2][password[0][0]-1] == password[1] or password[2][password[0][1]-1] == password[1]) and not (password[2][password[0][0]-1] == password[1] and password[2][password[0][1]-1] == password[1]):
        numValid += 1

print(numValid)
