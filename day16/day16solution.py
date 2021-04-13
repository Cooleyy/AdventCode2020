#!/usr/bin/env python3
import sys
import re
from copy import deepcopy

def CheckField(field):
    fieldValid = False
    fieldValidForTypes = []

    for ruleType, ruleRanges in rules.items():
        for ruleRange in ruleRanges:
            lowerValue, upperValue = ruleRange.split("-")
            if field >= int(lowerValue) and field <= int(upperValue):
                fieldValid = True
                fieldValidForTypes.append(ruleType)
                break
    
    return fieldValid, fieldValidForTypes

def checkTypesFound():
    allTypesFound = True

    for types in fieldTypes:
        if len(types) > 1:
            allTypesFound = False
            break

    return allTypesFound

if __name__ == "__main__":
    
    puzzleInputFile = open(sys.argv[1], 'r')
    notes = puzzleInputFile.read().split("\n\n")

    rules = {}
    for i, rule in enumerate(notes[0].splitlines()):
        ruleType, ruleValues = rule.split(": ")
        rules[ruleType] = ruleValues.split(" or ")

    myTicket = notes[1].splitlines()[1]
    myTicket = list(map(int, myTicket.split(",")))

    tickets = notes[2].splitlines()[1:]
    for i, ticket in enumerate(tickets):
        tickets[i] = list(map(int, tickets[i].split(","))) 

    ticketValid = True
    validTicketTypes = []
    validTickets = []

    for ticket in tickets:
        possibleTypes = []

        for field in ticket:
            ticketValid, possibleTypesForField = CheckField(field)
            possibleTypes.append(possibleTypesForField)
            if not ticketValid:
                break

        if ticketValid:
            validTicketTypes.append(possibleTypes)
            validTickets.append(ticket)

    possibleTypes = []
    for field in myTicket:
        ticketValid, possibleTypesForField = CheckField(field)
        possibleTypes.append(possibleTypesForField)
    validTicketTypes.append(possibleTypes)
    
    fieldTypes = []
    for i in range(len(myTicket)):
        possibleTypes = validTicketTypes[0][i]
        for j in range(len(validTickets)):
            for k, fType in enumerate(possibleTypes):
                if fType not in validTicketTypes[j][i]:
                    del possibleTypes[k]
            if len(possibleTypes) == 1:
                break
        fieldTypes.append(possibleTypes)
    
    foundTypes = []
    while(not checkTypesFound()):
        for types in fieldTypes:
            if len(types) == 1 and types[0] not in foundTypes:
                foundTypes.append(types[0])
        for i, types in enumerate(fieldTypes):
            if len(types) > 1:
                for foundType in foundTypes:
                    if foundType in fieldTypes[i]:
                        fieldTypes[i].remove(foundType)

    productOfFields = 1
    for i, field in enumerate(fieldTypes):
        if field[0].startswith("departure"):
            productOfFields *= myTicket[i]

    print(productOfFields)
