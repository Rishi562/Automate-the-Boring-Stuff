#Number Guess Game

import random
print('Hello, Whats your name ? ')
name=input()

print('well, ' + name + ', I am thinking of a number b/w 1 & 20')
secretnumber = random.randint(1,20)

for guesstaken in range(1,7):
    print('take a guess')
    guess = int(input())

    if guess < secretnumber:
        print('Thats too low, go higher')

    elif guess > secretnumber :
         print('you guessed too high')

    else:
        break #this is for correct guess

if guess == secretnumber:
    print('Good Job ' + 'You guess my number in ' + str(guesstaken) + ' guesses')
else:
    print(' the number i was thinking of ' + str(secretnumber))


print(' Rishi, you took ' + str(guesstaken) + ' guesses, the program will close now')
