#! python 3
import re

total = 0

#opens the input file
day1input = open('day1input.txt')
aocinput = day1input.readlines()

for i in range(len(aocinput)):
    number = re.findall('[0-9]', aocinput[i])
    number = ''.join(number)
    firstChar = number[0]
    lastChar = number[-1]
    number = int(firstChar + lastChar)
    total = total + number


print('Final Number: ' + str(total))




