#! python3

import re

data = open('day4input.txt').read().strip()
score = 0

for game, line in enumerate(data.split("\n"), start=1):                       
    #setup    
    numbers = line.split(": ")[-1].split("| ")
    elf_numbers = re.findall('\d+', numbers[0])
    winning_numbers = re.findall('\d+', numbers[1])
    number_matching = 0

    for e in elf_numbers:
        for w in winning_numbers:
            if e == w:
                number_matching += 1
                
    if number_matching == 1:
        score += 1
    elif number_matching == 2:
        score += 2
    elif number_matching == 3:
        score += 2**2
    elif number_matching == 4:
        score += 2**3
    elif number_matching == 5:
        score += 2**4
    elif number_matching == 6:
        score += 2**5
    elif number_matching == 7:
        score += 2**6
    elif number_matching == 8:
        score += 2**7
    elif number_matching == 9:
        score += 2**8
    elif number_matching == 10:
        score += 2**9

print('The score is: ' + str(score))
