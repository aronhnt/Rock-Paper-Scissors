from random import randint
from ErrorCheck import errorCheck
from sys import exit

def menu():
    running = True
    while running == True:
        print('''
1 - Play Vs. Human
2 - Play Vs. AI
3 - Quit''')
        option = errorCheck(input('Choose An Option: '), int, 'Choose An Option: ')
        if option == 1:
            print('WIP lol')
        if option == 2:
            main()
        if option == 3:
            running = False
    exit(0)

def main():
    rps = ['Rock', 'Paper', 'Scissors']
    rounds = errorCheck(input('How Many Rounds Do You Want To Play? '), int, 'How Many Rounds Do You Want To Play? ')
    for i in range(0, rounds):
        win = False
        userOpt = input('Rock, paper or scissors? ').upper()
        aiOpt = randint(0, len(rps) - 1)
        print('The AI Chose:', rps[aiOpt], sep=' ')
        if userOpt == 'ROCK' or userOpt == 'R':
            userOpt = 0
            if aiOpt == 2:
                print(rps[0], 'beats', rps[2], 'so you win!', sep=' ')
                win = True
        elif userOpt == 'PAPER' or userOpt == 'P':
            userOpt = 1
            if aiOpt == 0:
                print(rps[1], 'beats', rps[0], 'so you win!', sep=' ')
                win = True
        elif userOpt == 'SCISSORS' or userOpt == 'S':
            userOpt = 2
            if aiOpt == 1:
                print(rps[2], 'beats', rps[1], 'so you win', sep=' ')
                win = True
        if not win:
            if userOpt == aiOpt: print('Draw')
            else:
                print(rps[aiOpt], 'beats', rps[userOpt], 'Sorry, you lost!', sep=' ')

menu()
