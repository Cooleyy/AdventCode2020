#!/usr/bin/env python3
import sys
import re
import itertools
from copy import deepcopy
from operator import itemgetter, mul
from functools import reduce

def main():
    puzzleInputFile = open(sys.argv[1], 'r')
    puzzleInput = puzzleInputFile.read().split("\n\n")
    
    tiles = {tile[0].split()[1]: tile[1].splitlines() for tile in [tile.split(":\n") for tile in puzzleInput]}

    #convert tile data into 4 strings representing each side of the tile
    for key, tile in tiles.items():
        tiles[key] = [tile[0] , tile[-1]]
        tiles[key].append("".join([d[0] for d in tile]))
        tiles[key].append("".join([d[-1] for d in tile]))

    #For each tile check if its sides (or flipped sides) match another side in another tile and count how many sides match another
    #If a tile matches 2 others then it is a corner tile
    tilesSidesMatched = {key: 0 for key in tiles}
    for key, tile in tiles.items():
        for side in tile:
            for key2, tile2 in tiles.items():
                if key != key2 and (side in tile2 or side in [side2[::-1] for side2 in tile2]):
                    tilesSidesMatched[key] += 1
                    break

    print(reduce(mul, [int(key) for key in tilesSidesMatched if tilesSidesMatched[key] == 2]))

if __name__ == "__main__":
    main()