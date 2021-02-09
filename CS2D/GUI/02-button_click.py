import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry('300x300')

label = Label(window, text="Hello Python", foreground='red', background='yellow')
label.grid(row=0, column=0)

label = Label(window, text="Enter your name ", foreground='red')
label.grid(row=1, column=0)
textbox = Entry(window)
textbox.grid(row=1, column=2)

label_2 = Label(window, text="Hello : ", foreground='red')
label_2.grid(row=3, column=0)

def changeText():
    text = label_2['text']
    text = text + " " + textbox.get()
    label_2.configure(text = text)

button = Button(window, text="Click Here", command=changeText)
button.grid(row=2, column=1)

window.mainloop()