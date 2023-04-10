from tkinter import *
import os
from playsound import playsound
from tkinter import filedialog
import threading
from pygame import mixer


root = Tk()
root.title("Music Player")
root.geometry("250x170")
label = Label(root,text="Music Player",fg = "#B5485D",font=('Helvetica', 15))


path = filedialog.askdirectory()
playlist = []
if path:
    os.chdir(path)
    songs = os.listdir(path)

for song in songs:
    if song.endswith(".mp3"):
        playlist.append(song)


def play_song():
    global current_song
    global path
    mixer.init()
    os.chdir(path)
    song = os.path.join(os.getcwd(),playlist[current_song])
    mixer.music.load(song)
    mixer.music.play()
    
def next():
    global current_song
    current_song += 1
    if current_song > len(playlist) - 1:
        current_song = 0
    t = threading.Thread(target=play_song)
    t.start()
def previous():
    global current_song
    current_song -= 1
    if current_song < 0:
        current_song = len(playlist) - 1
    t = threading.Thread(target=play_song)
    t.start()
def music():
    try:
        global current_song
        os.getcwd()
        file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])   
        filename = os.path.basename(file_path)
        current_song = playlist.index(filename)
        t = threading.Thread(target=play_song)
        t.start()
    except Exception as e:
        myLabel = Label(root,text = "Error! while playing the song",fg = "blue")
        root.geometry("300x200")
        myLabel.grid(row=3,column=1)

def resume():
    mixer.music.unpause()
def pause():
    mixer.music.pause()

myButton1 = Button(root,text = "previous",font=('Helvetica', 10),fg="#064E3B",bd=2,width = 5, height = 1,command = previous)
myButton2 = Button(root,text = "select",font=('Helvetica', 11),fg="#064E3B",bd=2,width = 5,height = 1,command = music )
myButton3 = Button(root,text = "next",font=('Helvetica', 11),fg="#064E3B",bd=2,width = 5, height = 1,command = next )
myButton4 = Button(root,text = "pause",font=('Helvetica', 11),fg="#064E3B",bd=2,width = 5, height = 1,command = pause)
myButton5 = Button(root,text = "resume",font=('Helvetica', 11),fg = "#064E3B",bd=2,width = 5, height = 1,command = resume)

myButton1.grid(row=1, column=0,padx=2,pady=10)
myButton2.grid(row=1, column=1,padx=2,pady=10)
myButton3.grid(row=1, column=2,padx=2,pady=10)
myButton4.grid(row=2,column=0,padx=2,pady=10)
myButton5.grid(row=2,column=1,padx=2,pady=10)
label.grid(row=0,column=1,padx=10,pady=10)
    

root.mainloop()
