#!/usr/bin/env python3
import sys
import re
from copy import deepcopy

def checkArrangementsAfter(currentRating, nextAdapterPos):# Unused: too inefficient

    global arrangements

    # reached end of arrangement as there is only one more adapter so no possible arrangements
    if nextAdapterPos >=  lastAdapterPos - 1:
        return

    # assume next adapter is within 3 and continue arrangement
    checkArrangementsAfter(adapters[nextAdapterPos], nextAdapterPos+1)

    # if next adapter is 3 away then no more arrangements from current adapter
    if adapters[nextAdapterPos] - currentRating == 3:
        return

    # if adapter after next is also valid, increase arrangements and check arragements from there
    nextAdapterPos += 1
    if adapters[nextAdapterPos] - currentRating <= 3:
        arrangements += 1
        checkArrangementsAfter(adapters[nextAdapterPos], nextAdapterPos+1)

    # if next adapter is 3 away, or if only one more adapter after then no more arragements from current adapter
    if adapters[nextAdapterPos] - currentRating == 3 or nextAdapterPos == lastAdapterPos - 1:
        return

    # if adapter 2 after next is also valid, increase arrangements and check arrangements from there
    nextAdapterPos += 1
    if adapters[nextAdapterPos] - currentRating == 3:
        arangements += 1
        checkArrangementsAfter(adapters[nextAdapterPos], nextAdapterPos+1)    

if __name__ == "__main__":

    puzzleInputFile = open(sys.argv[1], 'r')
    adapters = puzzleInputFile.read().splitlines()
    adapters = list(map(int, adapters))
    adapters.sort()

    cachedArrangements = {0 : 1}

    for adapter in adapters:
        arrangementsForAdapter = 0
        for prevAdapter in [adapter-1,adapter-2,adapter-3]:
            if prevAdapter >= 0 and prevAdapter in cachedArrangements:
                arrangementsForAdapter += cachedArrangements[prevAdapter]

        cachedArrangements[adapter] = arrangementsForAdapter

    print(cachedArrangements[adapters[-1]])
