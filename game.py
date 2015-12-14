import random
compnum = random.randint(1, 100)

print('Guessing Game')
print('Enter a number between 1 and 100: ')
number = int(input())

def guessfun(tin):
    
    while tin != compnum:
        if tin < compnum:    
            print('Too low. Guess again:')
            tin = int(input())
        elif tin > compnum:
            print('Too high. Guess again')
            tin = int(input())

guessfun(number)
print('Good job. You win')
