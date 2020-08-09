# ----- Encrypts messages using the Caesar Cipher method ----- #
from tkinter import *

root = Tk()
root.title('Caesar Cipher')
root.geometry('')


# encrypt text
def encrypt(event=None):
    user_text = user_text_entry.get(1.0, END)
    key = key_input_entry.get(1.0, END)
    global enc_text
    enc_text = ''

    for i in user_text:
        if i.isalpha() and i.isupper():
            enc_text += chr((ord(i) + int(key) - 65) % 26 + 65)
        elif i.isalpha() and i.islower():
            enc_text += chr((ord(i) + int(key) - 97) % 26 + 97)
        elif i == ' ' or i == ',' or i == '?' or i == '!' or i == '.' or i == ':' or i == ';':
            enc_text += i
        elif i.isnumeric():
            enc_text += i

    result.config(state=NORMAL)
    result.delete(1.0, END)
    result.insert(1.0, enc_text)
    result.config(state=DISABLED)
    resultDe.config(state=NORMAL)
    resultDe.delete(1.0, END)
    resultDe.config(state=DISABLED)


# decrypt text
def decrypt(event=None):
    result.config(state=NORMAL)
    resultDe.config(state=NORMAL)
    resultDe.delete(1.0, END)
    resultDe.config(state=DISABLED)
    text2decrypt = result.get(1.0, END)

    c = 0
    while c <= 26:
        decText = ''
        for n in text2decrypt:
            if n.isalpha() and n.isupper():
                decText += chr((ord(n) + c - 65) % 26 + 65)
            elif n.isalpha() and n.islower():
                decText += chr((ord(n) + c - 97) % 26 + 97)
            elif n == ' ' or n == ',' or n == '?' or n == '!' or n == '.' or n == ':' or n == ';':
                decText += n
            elif n.isnumeric():
                decText += n
        c += 1

        result.config(state=DISABLED)
        resultDe.config(state=NORMAL)
        resultDe.insert(1.0, decText + '\n')
        resultDe.config(state=DISABLED)


# executes the function encrypt when Enter is pressed
root.bind('<Return>', encrypt)

# configure columns and rows proportions
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=0)
root.rowconfigure(3, weight=0)
root.rowconfigure(5, weight=1)

# widgets
user_text_entry = Text(root, height=5)
user_text_entry.grid(row=0, column=1, sticky=N+S+W+E)
key_input_entry = Text(root, height=1)
key_input_entry.grid(row=1, column=1, sticky=W+E)
buttonEncrypt = Button(root, text='Press to encrypt', command=encrypt)
buttonEncrypt.grid(columnspan=2)
result = Text(root, state=DISABLED, height=5)
result.grid(row=3, column=1, sticky=N+S+W+E)
buttonDecrypt = Button(root, text='Press to decrypt', command=decrypt)
buttonDecrypt.grid(row=4, columnspan=2)
resultDe = Text(root, state=DISABLED, height=5)
resultDe.grid(row=5, column=1, sticky=N+S+W+E)

# labels
user_text_label = Label(root, text='Insert text here:')
user_text_label.grid(row=0, column=0, sticky=E)
key_input_label = Label(root, text='Insert the key here:')
key_input_label.grid(row=1, column=0)
result_label = Label(root, text='Encrypted text:')
result_label.grid(row=3, column=0, sticky=E)
resultDe_label = Label(root, text='Possible decrypted text:')
resultDe_label.grid(row=5, column=0, sticky=E)

root.mainloop()
