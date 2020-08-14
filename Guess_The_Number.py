# generate a random number between 1 and 100
# and asks the user to guess it

import random

play = True

while play:
    # generate random number
    ran_n = random.randint(1,100)
    
    # initialise guess variable
    guess = ''
    
    # initialise decision to replay
    decide = ''
    
    # initialise guesses counter
    i= 0
    
        # guessing loop
    while guess != ran_n:
        # ask user to guess the number
        guess = int(input('Guess which number I picked:\n'))
        if guess < ran_n:
            print('Too low, guess again!')
        elif guess > ran_n:
            print('Too high, guess again!')
        # updates the guesses counter
        i += 1
        
    # when the user guesses the correct number,
    # exit while loop and print the number and
    # the number of guesses the user has taken
    print("That's right, I picked the number {}!\nYou took {} guesses!"
            .format(ran_n, i))
    
    # ask the user if he wants to replay or not
    while decide != 'y' and decide != 'n':        
        decide = input('Do you want to play again? [y,n]\n')
        if decide == 'n':
            print('Alright then, bye!')
            play = False
        elif decide == 'y':
            continue
        else:
            print('Please enter y or n')
