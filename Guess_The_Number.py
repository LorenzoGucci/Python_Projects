import random
x = random.randint(1,100)
print("I have picked a number between 1 and 100, can you guess it?")
ys = input("Guess: ")
y = int(ys)
while y != x:
    if (y < x):
        print("That's too low, try again!")
        ys = input("Guess: ")
        y = int(ys)
    if (y > x):
        print("No way, too high, guess again!")
        ys = input("Guess: ")
        y = int(ys)
    if (y == x):
        print("Yep, that's the number I picked, well done!")