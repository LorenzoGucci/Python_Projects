# this script asks the user
# the desired length of the
# Fibonacci sequence, and prints it

user = int(input('Insert the length of the Fibonacci sequence you want to display:\n'))
sequence = []
i = 0
while i <= user:
    if i == 0:
        sequence.append(0)
    elif i == 1:
        sequence.append(1)
    elif i == 2:
        sequence.append(1)
    else:
        n = sequence[i-1] + sequence[i-2]
        sequence.append(n)
    i += 1
print(sequence)
