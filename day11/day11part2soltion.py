#!/usr/bin/env python3
import sys
import re
from copy import deepcopy

def CheckSeatsInDirection(seatLayout, rowPos, seatPos, direction, positionOfLastRow, positionOfLastSeat):
    newRowPos = rowPos + direction[0]
    newSeatPos = seatPos + direction[1]

    if newRowPos < 0 or newSeatPos < 0 or newRowPos > positionOfLastRow or newSeatPos > positionOfLastSeat:
        return False

    seatToCheck = seatLayout[newRowPos][newSeatPos]

    if seatToCheck == '.':
        return CheckSeatsInDirection(seatLayout, newRowPos, newSeatPos, direction, positionOfLastRow, positionOfLastSeat)
    else:
        return seatToCheck == '#'


def CheckSeats(seatLayout):
    newSeatLayout = deepcopy(seatLayout)
    positionOfLastSeat = len(seatLayout[0]) - 1
    positionOfLastRow = len(seatLayout) - 1

    for i, row in enumerate(seatLayout):
        for j, seat in enumerate(row):
            if seat == '.':#no seat here
                continue

            adjOccupied = 0 #adjacent occupied seats

            directionsToCheck = [
                [-1,-1],#up left
                [-1,0],#up straight
                [-1,+1],#up right
                [0,-1],# left
                [0,+1],# right
                [+1,-1],#down left
                [+1,0],#down straight
                [+1,+1],#down right
            ]

            for direction in directionsToCheck:
                if CheckSeatsInDirection(seatLayout, i, j, direction, positionOfLastRow, positionOfLastSeat):
                    adjOccupied += 1
            
            if seat == 'L' and adjOccupied == 0:
                newSeatLayout[i][j] = '#'
            elif seat == '#' and adjOccupied >= 5:
                newSeatLayout[i][j] = 'L'

    return newSeatLayout

def CountOccupiedSeats(seatLayout):
    occupiedSeats = 0

    for row in seatLayout:
        for seat in row:
            if seat == '#':
                occupiedSeats += 1
    
    return occupiedSeats

if __name__ == "__main__":

    puzzleInputFile = open(sys.argv[1], 'r')
    seats = puzzleInputFile.read().splitlines()

    for i, row in enumerate(seats):
        seats[i] = list(row)

    currentSeatLayout = CheckSeats(seats)
    previousSeatLayout = deepcopy(seats)

    while (currentSeatLayout != previousSeatLayout):
        previousSeatLayout = deepcopy(currentSeatLayout)
        currentSeatLayout = CheckSeats(previousSeatLayout)

    print(CountOccupiedSeats(currentSeatLayout))