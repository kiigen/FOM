from random import *
from pyinputplus import inputMenu
x = ['rock', 'paper', 'scissors']

computer = 0
user = 0
for ran in range(int(input("Enter number of times: "))):
    i = inputMenu(x)
    e = choice(x)
    print('computer chose ', e, ', on to Next Round!')

    if i == 'rock':
        i = 2
        if e == 'rock':
            e = 2
        elif e == 'paper':
            e = 3
        elif e == 'scissors':
            e = 1
        if e > i:
            computer +=1
        if i > e:
            user +=1
    if i=='paper':
        i = 2
        if e == 'paper':
            e = 2
        elif e == 'scissors':
            e = 3
        elif e == 'rock':
            e = 1
        if e > i:
            computer += 1
        if i > e:
            user += 1
    if i == 'scissors':
        i = 2
        if e == 'scissors':
            e = 2
        elif e == 'rock':
            e = 3
        elif e == 'paper':
            e = 1
        if e > i:
            computer += 1
        if i > e:
            user += 1
print('computer: ', computer , 'user: ', user)
if computer > user :
    print('computer wins!')
elif user > computer:
    print('user wins!')
else:
    print('draw')
