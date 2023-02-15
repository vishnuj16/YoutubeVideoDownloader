from os import path
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
from pydub.playback import play
from pytube import YouTube

import shutil

def download_file():
    get_link = link_field.get()
    screen.title('Downloading...')
    user_path = path_label.cget("text")
    mp4_vid = YouTube(get_link).streams.get_highest_resolution().download()
    vid = VideoFileClip(mp4_vid)
    vid.close()
    
    shutil.move(mp4_vid, user_path)
    screen.title('Download Complete!')

def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

screen = Tk()
title = screen.title('Youtube Downloader')
canvas = Canvas(screen, width= 500, height=600)
canvas.pack()

logo_img = PhotoImage(file='youtube.png')
canvas.create_image(250, 80, image=logo_img)

link_field = Entry(screen, width=50)
link_label = Label(screen, text = "Enter the Youtube link!", font=('Helvetica', 15, "bold"))

path_label = Label(screen, text = "Select path for the Download", font=('Helvetica', 12, "bold"))
select_btn = Button(
    screen,
    text="Select",
    relief="ridge",
    bg="white",
    fg="black", 
    activeforeground="black",
    activebackground="red",
    font= "helvetica",
    pady = 5,
    width = 10,
    command = select_path)

# mb=  Menubutton ( screen, text="Video", relief=RAISED )
# mb.grid()
# mb.menu =  Menu ( mb, tearoff = 0 )
# mb["menu"] =  mb.menu

# mayoVar = IntVar()
# ketchVar = IntVar()
# option = StringVar()

# mb.menu.add_checkbutton ( label="Video", variable=option )
# mb.menu.add_checkbutton ( label="ketchup", variable=option)

# mb.pack()

canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

canvas.create_window(250, 280, window= path_label)
canvas.create_window(250, 340, window= select_btn)

download_btn = Button(screen, text = "Download", relief="ridge",
    bg="white",
    fg="black", 
    activeforeground="black",
    activebackground="red",
    font= "helvetica",
    pady = 5,
    width = 10,
    command = download_file)
canvas.create_window(250, 410, window=download_btn,)


screen.mainloop()