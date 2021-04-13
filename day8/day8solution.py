#!/usr/bin/env python3
import sys
import re
from copy import deepcopy

if __name__ == "__main__":
    
    puzzleInputFile = open(sys.argv[1], 'r')
    instructionsFromFile = puzzleInputFile.read().splitlines()
    instructions = deepcopy(instructionsFromFile)
    
    instructionPosition = 0
    instructionsCompleted = []
    accumulator = 0
    currentInstruction = instructions[instructionPosition]
    positionToChange = 0

    while instructionPosition < len(instructions) and instructionPosition not in instructionsCompleted:
        print(currentInstruction)
        currentInstructionType = currentInstruction[:3]
        currentInstructionArgument = currentInstruction[4:]
        previousInstructionPosition = instructionPosition

        if currentInstructionType == "nop":
            instructionPosition += 1
        elif currentInstructionType == "acc":
            if currentInstructionArgument[0] == "+":
                accumulator += int(currentInstructionArgument[1:])
            elif currentInstructionArgument[0] == "-":
                accumulator -= int(currentInstructionArgument[1:])
            instructionPosition += 1
        elif currentInstructionType == "jmp":
            if currentInstructionArgument[0] == "+":
                instructionPosition += int(currentInstructionArgument[1:])
            elif currentInstructionArgument[0] == "-":
                instructionPosition -= int(currentInstructionArgument[1:])
        else:
            print("Error instruction not recognised")
            break

        if instructionPosition < len(instructions):
            if instructionPosition in instructionsCompleted or instructionPosition == previousInstructionPosition:
                instructions = deepcopy(instructionsFromFile)
                while instructions[positionToChange][:3] == "acc":
                    positionToChange += 1
                if instructions[positionToChange][:3] == "nop":
                    instructions[positionToChange] = instructions[positionToChange].replace("nop", "jmp")
                else:
                    instructions[positionToChange] = instructions[positionToChange].replace("jmp", "nop")
                print("Changing instruction")
                print(instructions[positionToChange])
                positionToChange += 1
                instructionPosition = 0
                currentInstruction = instructions[instructionPosition]
                instructionsCompleted = []
                accumulator = 0
            else:
                instructionsCompleted.append(previousInstructionPosition)
            currentInstruction = instructions[instructionPosition]
        else:
            print("Last instruction completed")
            break

    print(accumulator)
