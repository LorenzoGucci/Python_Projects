# ----- Encrypts messages using the Caesar Cipher method ----- #
from tkinter import *

root = Tk()
root.title('Caesar Cipher')
root.geometry('')


# encrypted text
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
        elif i == ' ':
            enc_text += '#'
        elif i == ',':
            enc_text += '|'
        elif i == '?':
            enc_text += '£'
        elif i == '!':
            enc_text += '$'

    result.config(state=NORMAL)
    result.delete(1.0, END)
    result.insert(1.0, enc_text)
    result.config(state=DISABLED)


# executes the function encrypt when Enter is pressed
root.bind('<Return>', encrypt)

# configure columns and rows proportions
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(3, weight=1)

# widgets
user_text_entry = Text(root, height=5)
user_text_entry.grid(row=0, column=1, sticky=N+S+W+E)
key_input_entry = Text(root, height=1)
key_input_entry.grid(row=1, column=1, sticky=N+S+W+E)
buttonEncrypt = Button(root, text='Press to encrypt', command=encrypt)
buttonEncrypt.grid(columnspan=2)
result = Text(root, state=DISABLED, height=5)
result.grid(row=3, column=1, sticky=N+S+W+E)

# labels
user_text_label = Label(root, text='Insert text here:')
user_text_label.grid(row=0, column=0, sticky=E)
key_input_label = Label(root, text='Insert the key here:')
key_input_label.grid(row=1, column=0)
result_label = Label(root, text='Encrypted text:')
result_label.grid(row=3, column=0, sticky=E)

root.mainloop()
