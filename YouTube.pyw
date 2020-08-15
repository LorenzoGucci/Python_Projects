from tkinter import *
from tkinter import filedialog
from pytube import YouTube

root = Tk()
root.title('YouTube Downloader')
root.geometry('400x230')

# string variable for storing user input
url_var = StringVar()
folder_path = StringVar()


# Allow user to select a directory and store it in global var
# called folder_path
def browse_button(event=None):
    global folder_path
    global filename
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    # show the selected save path
    savePath.config(state=NORMAL)
    savePath.delete(0, END)
    savePath.insert(0, filename)
    savePath.config(state='readonly')


# create a function that prints the user input
def yt_download(event=None):
    url = url_entry.get()  # stores user input
    # print(url)
    video = YouTube(url)
    video.streams.first().download(filename)


# executes the function yt_download when Enter is pressed
root.bind('<Return>', yt_download)

# -------- Widgets -------- #

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)


# create "Browse" button
urlButton = Button(root, text='Browse', command=browse_button)
urlButton.grid(row=1, pady=5, columnspan=2)


# create widget to input url
url_entry = Entry(root, textvariable=url_var)
url_entry.grid(row=5, padx=5, pady=5, columnspan=2, sticky=W + E)


# create "Download" button
buttonUrl = Button(root, text='Download', command=yt_download)
buttonUrl.grid(row=6, pady=5, columnspan=2)

# -------- Labels -------- #

# YouTube url
label_url = Label(root, text='Insert video url:')
label_url.grid(row=4, pady=5, columnspan=2)

# save path
label_save = Label(root, text='Select the save path:')
label_save.grid(row=0, pady=5, columnspan=2)
label_savepath = Label(root, text='Selected path:')
label_savepath.grid(row=2, pady=5, columnspan=2)

savePath = Entry(root, state=DISABLED)
savePath.grid(row=3, pady=5, padx=5, columnspan=2, sticky=W + E)


root.mainloop()
