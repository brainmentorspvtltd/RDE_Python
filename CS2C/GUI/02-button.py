import tkinter
from tkinter import *

window = Tk()
window.geometry('400x400')

label = Label(window, text="Hello Python", fg='red',
              font=('Arial',28,'bold'))
label.place(x = 10, y = 10)

def change_text():
    label.configure(text = "Bye Python")

btn = Button(window, text="Click Here", command=change_text)
btn.place(x=10,y=70)

window.mainloop()