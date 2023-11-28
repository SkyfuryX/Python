# This is a guess the number game
import random

print('Hello! What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
print('You have 6 guesses.')
secretNumber = random.randint(1,20)

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = input()
        
    try:
      if int(guess) < secretNumber:
          print('Your guess is too low!')
          print('You have ' + str(6 - guessesTaken) + ' guesses remaining.')
      elif int(guess) > secretNumber:
          print('Your guess is too high!')
          print('You have ' + str(6 - guessesTaken) + ' guesses remaining.')
      else:
          break # Breaks the loop when the user guesses the correct number
    except ValueError: # Ensures the input is an integer
        print('That is not a number. Try again.')
        print('You have ' + str(6 - guessesTaken) + ' guesses remaining.')

if int(guess) == secretNumber:
    print(name + '! You guessed my number in ' + str(guessesTaken) + ' guesses. Good job!')
else:
    print('Sorry, the number I was thinking of was ' + str(secretNumber) + '.')
    



