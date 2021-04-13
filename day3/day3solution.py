#!/usr/bin/env python3
import sys

def returnMapPos(x,y):
    x = x % len(treeMap[0])
    return treeMap[y][x]

def countTrees(directionX, directionY):
    x = 0
    y = 0
    treesFound = 0
    while y < len(treeMap):
        if returnMapPos(x,y) == "#":
            treesFound += 1
        x += directionX
        y += directionY
    return treesFound


if __name__ == "__main__":
    
    puzzleInputFile = open(sys.argv[1], 'r')
    treeMap = puzzleInputFile.read().splitlines()
    
    directions = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    
    finalAnswer = 1
    for direction in directions:
        finalAnswer = finalAnswer * countTrees(direction[0],direction[1])

    print(finalAnswer)



