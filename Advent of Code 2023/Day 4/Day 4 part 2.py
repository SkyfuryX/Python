#! python3
import re

data = open('day4input.txt').read().strip()
score = 0
global next_card
next_card = [0,0,0,0,0,0,0,0,0,0,0,0]

def copies(number_matching):
    for n in range(number_matching):
        next_card[n+1] += 1    

for line in data.split("\n"):                       
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
    copies(number_matching)

    #add copies to score and increments further
    if next_card[0] >=1:
        score += next_card[0]
        for copy in range(next_card[0]):
            copies(number_matching)  

    #moves the number of copies to come up the chain and resets the farthest one out
    for n in range(11):
        next_card[n] = next_card[n+1]

print('The score is: ' + str(score))
