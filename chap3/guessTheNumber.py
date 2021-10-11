# This is a guess the number game.
import random
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 imes.
for guessesTaken in range(1,7):
    print('Take a guess.')
    try:
        guess = int(input())
    except ValueError:
        print('Wrong Value, please enter a number between 1 and 20.')
        continue

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break
try:
    if guess == secretNumber:
        print('Good guess! Thats correct! The secret number is: ' + str(secretNumber) + '\nYout took ' + str(guessesTaken) + ' guesses.')
    else:
        print('Nope: ' + str(secretNumber))
except NameError:
    print('You made no valid guess.')