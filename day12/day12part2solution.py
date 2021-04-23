#!/usr/bin/env python3
import sys
import re
from copy import copy, deepcopy

def main():
    puzzleInputFile = open(sys.argv[1], 'r')
    actions = puzzleInputFile.read().splitlines()

    currentPosition = [0, 0] #[0] = North/South [1] = East/West
    waypointPosition = [1,10] # Relative to ship position

    for action in actions:
        actionType = action[0]
        actionMagnitude = int(action[1:])

        print("action: "+ action)
        print("currentPos = " + str(currentPosition))
        print("waypointPos = " + str(waypointPosition) + "\n")

        if actionType == "N":
            waypointPosition[0] += actionMagnitude
        elif actionType == "S":
            waypointPosition[0] -= actionMagnitude
        elif actionType == "E":
            waypointPosition[1] += actionMagnitude
        elif actionType == "W":
            waypointPosition[1] -= actionMagnitude
        elif actionType == "L":
            for i in range(actionMagnitude // 90):#For each 90 degrees rotate waypoint left around ship
                northPos = waypointPosition[0]
                waypointPosition[0] = waypointPosition[1]
                waypointPosition[1] = -northPos
        elif actionType == "R":
            for i in range(actionMagnitude // 90):#For each 90 degrees rotate waypoint right around ship
                northPos = waypointPosition[0]
                waypointPosition[0] = -waypointPosition[1]
                waypointPosition[1] = northPos
        elif actionType == "F":
            currentPosition[0] += (waypointPosition[0] * actionMagnitude)
            currentPosition[1] += (waypointPosition[1] * actionMagnitude)
        
        print("currentPos = " + str(currentPosition))
        print("waypointPos = " + str(waypointPosition) + "\n")

    #just take magnitude and ignore directions
    if currentPosition[0] < 0:
        currentPosition[0] *= -1
    if currentPosition[1] < 0:
        currentPosition[1] *= -1
    
    print(currentPosition)
    print(currentPosition[0] + currentPosition[1])

if __name__ == "__main__":
    main()