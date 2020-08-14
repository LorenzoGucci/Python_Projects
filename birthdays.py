# based on user choice, returns
# the birthday of the person

import time

# dictionary that contains names and birthdays
birthdays = {
    'Leonardo Da Vinci': '15-Apr-1452',
    'Isaac Newton': '04-Jan-1643',
    'Albert Einstein': '14-Mar-1879',
    'Nikola Tesla': '10-Jul-1856',
    'Thomas Edison': '11-Feb-1847',
}

# lists the known birthdays
print('Hi there, these are the people whose birthday I know:\n')
time.sleep(1)
for x in birthdays:
    print(x)
    time.sleep(0.5)

# asks whose birthday the user want to know
choice = input('\nWhose birthday would you like to know?\n')
choice = choice.title() # capitalise the initial letter of each word
time.sleep(0.5)
print(choice + "'s birthday is " + birthdays[choice])
time.sleep(0.5)

