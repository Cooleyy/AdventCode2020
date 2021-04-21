#!/usr/bin/env python3
import sys
import re
from copy import deepcopy

def CheckRow(row, j, positionOfLastSeat, currentRow = False):
    occupied = 0

    if j != 0 and row[j-1] == '#':#Check left
        occupied += 1
    if not currentRow and row[j] == '#':#Check straight
        occupied += 1
    if j < positionOfLastSeat and row[j+1] == '#':#Check right
        occupied += 1

    return occupied

def CheckSeats(seatLayout):
    newSeatLayout = deepcopy(seatLayout)
    positionOfLastSeat = len(seatLayout[0]) - 1
    positionOfLastRow = len(seatLayout) - 1

    for i, row in enumerate(seatLayout):
        for j, seat in enumerate(row):
            adjOccupied = 0 #adjacent occupied seats

            if seat == '.': #no seat here
                continue

            #Check up
            if i != 0:
                adjOccupied += CheckRow(seatLayout[i-1], j, positionOfLastSeat)
            
            #Check current row
            adjOccupied += CheckRow(row, j, positionOfLastSeat, True)

            #Check below
            if i < positionOfLastRow :
                adjOccupied += CheckRow(seatLayout[i+1], j, positionOfLastSeat)
            
            if seat == 'L' and adjOccupied == 0:
                newSeatLayout[i][j] = '#'
            elif seat == '#' and adjOccupied >= 4:
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