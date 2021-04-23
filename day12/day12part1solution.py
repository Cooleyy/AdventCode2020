#!/usr/bin/env python3
import sys
import re
from copy import deepcopy

def main():
    puzzleInputFile = open(sys.argv[1], 'r')
    actions = puzzleInputFile.read().splitlines()

    currentDirection = 90 #0 = North, 90 = East, 180 = South, 270 = West
    currentPosition = [0, 0] #[0] = North/South [1] = East/West

    for action in actions:
        actionType = action[0]
        actionMagnitude = int(action[1:])

        if actionType == "N":
            currentPosition[0] += actionMagnitude
        elif actionType == "S":
            currentPosition[0] -= actionMagnitude
        elif actionType == "E":
            currentPosition[1] += actionMagnitude
        elif actionType == "W":
            currentPosition[1] -= actionMagnitude
        elif actionType == "L":
            currentDirection -= actionMagnitude
            if currentDirection < 0:
                currentDirection %= 360
        elif actionType == "R":
            currentDirection += actionMagnitude
            if currentDirection >= 360:
                currentDirection %= 360
        elif actionType == "F":
            if currentDirection == 0:#North
                currentPosition[0] += actionMagnitude
            elif currentDirection == 90:#East
                currentPosition[1] += actionMagnitude
            elif currentDirection == 180:#South
                currentPosition[0] -= actionMagnitude
            elif currentDirection == 270:#West
                currentPosition[1] -= actionMagnitude

    #just take magnitude and ignore directions
    if currentPosition[0] < 0:
        currentPosition[0] *= -1
    if currentPosition[1] < 0:
        currentPosition[1] *= -1
    
    print(currentPosition[0] + currentPosition[1])

if __name__ == "__main__":
    main()