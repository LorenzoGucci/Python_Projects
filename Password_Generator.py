# generates passwords based on User choices

import random
import string
import time

# asks the user the length of the password
length = int(input('How many characters should the password be?\n'))

time.sleep(0.5)

# asks the user about numbers
numb = input('Do you want it to include numbers? [y/n]\n')

time.sleep(0.5)

# asks the user about capital letters
cap = input('Do you want it to include capital letters? [y/n]\n')

time.sleep(0.5)

# asks the user about special characters
special = input('Do you want it to include special characters? [y/n]\n')

time.sleep(0.5)

# with numbers
if numb == 'y' and cap == 'n' and special == 'n':
    pwd_n = string.ascii_lowercase + string.digits
    print('The password is: ' + ''.join(random.choice(pwd_n) for i in range(length)))
# with capital letters
elif numb == 'n' and cap == 'y' and special == 'n':
    pwd_n = string.ascii_lowercase + string.ascii_uppercase
    print('The password is: ' + ''.join(random.choice(pwd_n) for i in range(length)))
# with special characters
elif numb == 'n' and cap == 'n' and special == 'y':
    pwd_n = string.ascii_lowercase + string.punctuation
    print('The password is: ' + ''.join(random.choice(pwd_n) for i in range(length)))
# with numbers and capital letters
elif numb == 'y' and cap == 'y' and special == 'n':
    pwd_n = string.ascii_lowercase + string.ascii_uppercase + string.digits
    print('The password is: ' + ''.join(random.choice(pwd_n) for i in range(length)))
# with numbers and special characters
elif numb == 'y' and cap == 'n' and special == 'y':
    pwd_n = string.ascii_lowercase + string.digits + string.punctuation
    print('The password is: ' + ''.join(random.choice(pwd_n) for i in range(length)))
# with capital letters and special characters
elif numb == 'n' and cap == 'y' and special == 'y':
    pwd_n = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
    print('The password is: ' + ''.join(random.choice(pwd_n) for i in range(length)))
# with numbers, capital letters and special characters
elif numb == 'y' and cap == 'y' and special == 'y':
    pwd_n = string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase
    print('The password is: ' + ''.join(random.choice(pwd_n) for i in range(length)))
