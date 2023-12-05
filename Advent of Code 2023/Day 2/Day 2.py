#! python3

import re

data = open('day2input.txt').read().strip()

p1 = 0
p2 = 0

for game, line in enumerate(data.split("\n"), start=1):                       
    #setup
    #print('Game: ' + str(game))
    valid = True
    min_red = min_green = min_blue = 0
    
    for s in line.split(": ")[-1].split("; "):
        #print(s)
        # sum of each color in set
        red = sum(int(n) for n in re.findall(r"(\d+)\sred" , s))
        green = sum(int(n) for n in re.findall(r"(\d+)\sgreen" , s))
        blue = sum(int(n) for n in re.findall(r"(\d+)\sblue" , s))
        #set the minimum required for the set
        min_red = max(min_red, red)
        min_green = max(min_green, green)
        min_blue = max(min_blue, blue)
        #check game validity
        if red > 12 or green > 13 or blue > 14:
            valid = False
    
    if valid:
        p1 += game
    #part 2 - add product of minimum required cubes for each game
    p2 += min_red * min_blue * min_green

print('Part 1: ' + str(p1))
print('Part 2: ' + str(p2))
