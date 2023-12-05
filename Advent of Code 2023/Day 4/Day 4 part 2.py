#! python3

import re

data = open('day4input.txt').read().strip()
score = 0
current_card = 0
next_card = 0
next_card2 = 0
next_card3 = 0
next_card4 = 0
next_card5 = 0
next_card6 = 0
next_card7 = 0
next_card8 = 0
next_card9 = 0
next_card10 = 0

for game, line in enumerate(data.split("\n"), start=1):                       
    #setup    
    score += 1
    numbers = line.split(": ")[-1].split("| ")
    elf_numbers = re.findall('\d+', numbers[0])
    winning_numbers = re.findall('\d+', numbers[1])
    number_matching = 0
    #checks for winning numbers
    for e in elf_numbers:
        for w in winning_numbers:
            if e == w:
                number_matching += 1

    #adds copies of cards to come        
    if number_matching >= 1:
        next_card += 1
    if number_matching >= 2:
        next_card2 += 1
    if number_matching >= 3:
        next_card3 += 1
    if number_matching >= 4:
        next_card4 += 1
    if number_matching >= 5:
        next_card5 += 1
    if number_matching >= 6:
        next_card6 += 1
    if number_matching >= 7:
        next_card7 += 1
    if number_matching >= 8:
        next_card8 += 1
    if number_matching >= 9:
        next_card9 += 1
    if number_matching == 10:
        next_card10 += 1

    #add copies to score and increments further
    if current_card >=1:
        score += current_card
        for copy in range(current_card):
            if number_matching >= 1:
                next_card += 1
            if number_matching >= 2:
                next_card2 += 1
            if number_matching >= 3:
                next_card3 += 1
            if number_matching >= 4:
                next_card4 += 1
            if number_matching >= 5:
                next_card5 += 1
            if number_matching >= 6:
                next_card6 += 1
            if number_matching >= 7:
                next_card7 += 1
            if number_matching >= 8:
                next_card8 += 1
            if number_matching >= 9:
                next_card9 += 1
            if number_matching == 10:
                next_card10 += 1   

    #moves the number of copies to come up the chain and resets the farthest one out
    current_card = next_card
    next_card = next_card2
    next_card2 = next_card3
    next_card3 = next_card4
    next_card4 = next_card5
    next_card5 = next_card6
    next_card6 = next_card7
    next_card7 = next_card8
    next_card8 = next_card9
    next_card9 = next_card10
    next_card10 = 0

print('The score is: ' + str(score))
