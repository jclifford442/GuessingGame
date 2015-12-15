##Guessing Game

import random
compnum = random.randint(1, 100)

def guessfun(tin):
    if tin > 0 and tin <= 100:
        if tin < compnum:
            print('Too low. Guess again:')
            return tin
        elif tin > compnum:
            print('Too high. Guess again:')
            return tin
    else:
        print('Way to follow directions. This counts as a guess. Try again:')
        return tin
    
print('Guessing Game')
print('Enter a number between 1 and 100: ')
number = int(input())
guessfun(number)

          
i = 1
while number != compnum:
    i = i + 1
    number = int(input())
    guessfun(number)

if i <= 5:
    print("You're smarter than you look. You got it in", i, "guesses") 
elif i <= 10 and i > 5:
    print("You did OK. Like a fast fat kid. You got it in", i, "guesses")
elif i > 10 and i <= 15:
    print("Guessing skills are worse than the weatherman.", i, "guesses")
elif i > 15:
    print("Please stop playing. You got it in", i, "miserable guesses")
