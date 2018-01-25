from gtts import gTTS
from playsound import playsound
import tkinter as tk
import pygame
import os
import stat


def onKeyPress(event):
    text = tk.Text(root, background='black', foreground='white')
    text.pack()
    letter = '%s'% (event.char, )
    name = letter + '.mp3'
    '''if os.path.isfile(name):
        playsound(name)'''
    if letter == "a":
        tts = gTTS(letter, lang='en-us', slow=True)
        tts.save(letter + '.mp3')
        playsound("sound/"+name)


    #removeFile(name)

def removeFile(file):
    os.remove(file)

root = tk.Tk()
root.geometry('300x200')
root.bind('<KeyPress>', onKeyPress)
root.mainloop()
'''while exit = False:
'''

#sayIt = input("What would you like me to say?")
#tts = gTTS(text = sayIt, lang = 'en-uk')
#tts.save("hello.mp3")



