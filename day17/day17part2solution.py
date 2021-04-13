#!/usr/bin/env python3
import sys
import re
from copy import deepcopy
import numpy as np

def checkNeighbours(w,z,y,x):
    if w > len(currentState) or z > len(currentState[0]) or y > len(currentState[0,0]) or x > len(currentState[0,0,0]):
        currentCube = "."
    elif w <= 0 or z <= 0 or y <= 0 or x <= 0:
        currentCube = "."
    else:
        currentCube = currentState[w-1, z-1,y-1,x-1]
    
    totalActiveNeighbours = 0

    for neighbourW in range(w-1,w+2):
        for neighbourZ in range(z-1,z+2):
            for neighbourY in range(y-1,y+2):
                for neighbourX in range(x-1,x+2):
                    if [neighbourW, neighbourZ, neighbourY, neighbourX] == [w,z,y,x]:
                        continue
                    elif neighbourW > len(currentState) or neighbourZ > len(currentState[0]) or neighbourY > len(currentState[0,0]) or neighbourX > len(currentState[0,0,0]):
                        continue
                    elif neighbourW <= 0 or neighbourZ <= 0 or neighbourY <= 0 or neighbourX <= 0:
                        continue
                    elif currentState[neighbourW-1, neighbourZ-1,neighbourY-1,neighbourX-1] == "#":
                        totalActiveNeighbours += 1

    if (totalActiveNeighbours == 2 or totalActiveNeighbours == 3) and currentCube == "#":
        return "#"
    elif totalActiveNeighbours == 3 and currentCube == ".":
        return "#"
    else:
        return "."

if __name__ == "__main__":
    
    puzzleInputFile = open(sys.argv[1], 'r')
    initialState = puzzleInputFile.read().splitlines()
    for i, xCol in enumerate(initialState):
        initialState[i] = list(xCol)

    currentState = np.array([[initialState]], str)
    cycles = 6 

    for i in range(cycles):
        newStateSize = tuple([x+2 for x in list(currentState.shape)])
        nextState = np.empty(newStateSize, str)
        for w1, row in enumerate(nextState):
            for z1, zCol in enumerate(row):
                for y1, yCol in enumerate(zCol):
                    for x1, cube in enumerate(yCol):
                        nextState[w1,z1,y1,x1] = checkNeighbours(w1,z1,y1,x1)
        currentState = deepcopy(nextState)

    totalActive = 0
    for cube in np.nditer(currentState):
        if cube == "#":
            totalActive += 1

    print(totalActive)
