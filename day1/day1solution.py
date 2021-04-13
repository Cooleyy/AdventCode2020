#!/usr/bin/python3
import sys

numbersFile = open (sys.argv[1], 'r')

numbers = numbersFile.read().splitlines()
numbers = list(map(int, numbers))

'''
counter = 0
for num in numbers:
    for num2 in numbers[counter+1:]: 
        if (num + num2) == 2020: 
            print(str(num) + " * " + str(num2) + " = " + str(num*num2))
            break
    else:
        counter += 1
        continue
    break
'''

counter1 = 1
for num in numbers:
    for num2 in numbers[counter1:]:
        counter2 = 1
        if (num + num2) < 2020:
            for num3 in numbers[counter1 + counter2:]:
                if (num + num2 + num3) == 2020:
                    print(str(num) + " * " + str(num2) + " * " + str(num3) + " = " + str(num*num2*num3))
                    break
            else:
                continue
                counter += 1
            break
    else:
        counter1 += 1
        continue
    break
