#make a text to speech speaker with tkinter gui

# import tkinter
from tkinter import *
# import pyttsx3
import pyttsx3

# function to make a text to speech
def speak():
    # get the text from the entry box
    text = entry.get()
    # create a engine
    engine = pyttsx3.init()
    # set the voice of the engine
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    # set the rate of the engine
    engine.setProperty('rate', 150)
    # speak the text
    engine.say(text)
    # save the text
    engine.save_to_file(text, 'output.wav')
    # play the text
    engine.runAndWait()
# create a window
window = Tk()
# set the title of the window
window.title("Text to Speech")
# set the size of the window
window.geometry("500x500")
# set the background color of the window
window.configure(background='#ffffff')
# set the text of the label
label = Label(window, text="Enter the text to speak", bg='#ffffff')
# set the position of the label
label.place(x=100, y=100)
# set the position of the entry box
entry = Entry(window, width=50)
entry.place(x=100, y=150)
# set the position of the button
button = Button(window, text="Speak", command=speak)
button.place(x=100, y=200)
# run the window
window.mainloop()
# end of the program

# @author: Yerik Velez
# @version: 1.0
# @date: 2022-3-27
# @description: text to speech speaker