# This script simulates a Magic 8 Ball
def magic8ball():  # Creates the function to play with the Magic Ball
    import random

    # The following list shows the 20 answers found on the icosahedron (20-sided figure) inside the ball
    messages = ["As I see it, yes.", "Ask again later.", "Better not tell you now.",
                "Cannot predict now.", "Concentrate and ask again.", "Don’t count on it.",
                "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.",
                "My sources say no.", "Outlook not so good.", "Outlook good.",
                "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.",
                "Without a doubt.", "Yes.", "Yes – definitely.", "You may rely on it."]

    input("Shake the ball and ask a question:\n")  # Asks user to insert a question for the Magic Ball
    print(messages[random.randint(0, len(messages) - 1)])


while True:
    magic8ball()
    replay = input("Do you want to ask the Magic Ball another question?\n")
    if replay == "yes" or replay == "Yes" or replay == "y":
        print("Alright.")
    elif replay == "no" or replay == "No" or replay == "n":
        print("Very good, thanks for playing.")
        break