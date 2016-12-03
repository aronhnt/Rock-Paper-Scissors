from random import randint
from ErrorCheck import errorCheck

def menu():
    running = True
    while running == True:
        print('''
1 - Play Vs. Human
2 - Play Vs. AI
3 - Quit''')
        option = input('Choose An Option: ')
        option = errorCheck(option,int,'Choose An Option: ')
        if option == 1:
            print('WIP lol')
        if option == 2:
            main()
        if option == 3:
            raise SystemExit
            running = False
def main():
    rps = ['Rock', 'Paper', 'Scissors']
    rounds = input('How Many Rounds Do You Want To Play? ')
    rounds = errorCheck(rounds,int,'How Many Rounds Do You Want To Play? ')
    for i in range(0,rounds):
        userOpt = input('Rock, paper or scissors? ').upper()
        aiOpt = randint(0,len(rps) - 1)
        print (aiOpt)
        if userOpt == 'ROCK' or userOpt == 'R':
            userOpt = 0
        elif userOpt == 'PAPER' or userOpt == 'P':
            userOpt = 1
        elif userOpt == 'SCISSORS' or userOpt == 'S':
            userOpt = 2
        if userOpt == 1 and aiOpt == 3:
            print(rps[1], + 'beats', + rps[3])
menu()
    
