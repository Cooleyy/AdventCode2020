#!/usr/bin/env python3
import sys
import re

def binarySearch(maxRange, seatCode):
    high = maxRange
    low = 0
    for direction in seatCode[:-1]:
        if direction == "F" or direction == "L":
            high = ((high + low) // 2)
        else:
            low = ((high + low + 1) // 2)

    return low if (seatCode[-1] == "F" or seatCode[-1] == "L") else high

if __name__ == "__main__":
    
    puzzleInputFile = open(sys.argv[1], 'r')
    boardingPasses = puzzleInputFile.read().splitlines()
    
    for i, boardingPass in enumerate(boardingPasses):
        boardingPasses[i] = {}
        boardingPasses[i]["Row"] = binarySearch(127, boardingPass[:7])
        boardingPasses[i]["Column"] = binarySearch(7, boardingPass[7:])
        boardingPasses[i]["SeatID"] = (boardingPasses[i]["Row"] * 8) + boardingPasses[i]["Column"]

    boardingPasses.sort(key=lambda k : k["SeatID"])
    print(boardingPasses)

    highestSeatID = 0
    for i, boardingPass in enumerate(boardingPasses):
        if i+1 < len(boardingPasses):
            if boardingPasses[i+1]["SeatID"] - boardingPass["SeatID"] != 1:
                print(boardingPass["SeatID"]+1)

