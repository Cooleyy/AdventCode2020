#!/usr/bin/env python3
import sys
import re
from copy import deepcopy

#Next time bus "id" arrives after "afterWhen"
def nextArrival(afterWhen, id):
    arrivalBefore = afterWhen - (afterWhen % id)
    nextArrival = arrivalBefore + id
    return nextArrival

def main():
    puzzleInputFile = open(sys.argv[1], 'r')
    puzzleInput = puzzleInputFile.read().splitlines()

    earliestDepartureTime = int(puzzleInput[0])
    busIDs = puzzleInput[1].split(",")

    busIDs = [x for x in busIDs if "x" not in x]
    busIDs = list(map(int, busIDs))

    busArrivalTimes = {busID : nextArrival(earliestDepartureTime, busID) for busID in busIDs}

    nextBus = min(busArrivalTimes, key = lambda k: busArrivalTimes[k])

    print(nextBus * (busArrivalTimes[nextBus] - earliestDepartureTime))

if __name__ == "__main__":
    main()