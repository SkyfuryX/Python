#! python3

import re

total = 0

#opens the input file
day1input = open('day1input.txt')
aocinput = day1input.readlines()
day1input.close()

for i in range(len(aocinput)):
    #print(aocinput[i])

    #searches for matches including numbers that run into each other
    number = re.findall('[0-9]|twone|eightwo|oneight|one|two|three|four|five|six|seven|eight|nine', aocinput[i])
    #print(number)

    for x in range(len(number)):
        if number[x] == 'twone':
            number[x] = '21'
        if number[x] == 'oneight':
            number[x] = '18'
        elif number[x] == 'eightwo':
            number[x] = '82'
        elif number[x] == 'one':
            number[x] = '1'
        elif number[x] == 'two':
            number[x] = '2'
        elif number[x] == 'three':
            number[x] = '3'
        elif number[x] == 'four':
            number[x] = '4'
        elif number[x] == 'five':
            number[x] = '5'
        elif number[x] == 'six':
            number[x] = '6'
        elif number[x] == 'seven':
            number[x] = '7'
        elif number[x] == 'eight':
            number[x] = '8'
        elif number[x] == 'nine':
            number[x] = '9'

    #combines the list and pulls first + last chars
    number = ''.join(number)
    firstChar = number[0]
    lastChar = number[-1]
    number = int(firstChar + lastChar)

    total = total + number
    print('Current total ' + str(total))

print('Final Number: ' + str(total))




