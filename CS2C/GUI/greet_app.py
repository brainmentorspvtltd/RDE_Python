import tkinter
from tkinter import *

window = Tk()
window.geometry('400x400')

label = Label(window, text="Hello Python", fg='red',
              font=('Arial',28,'bold'))
label.place(x = 10, y = 10)

text_box = Entry(window, width=20, font=('Arial', 20, 'bold'))
text_box.place(x=10, y=70)

def change_text():
    value = text_box.get()
    label.configure(text = "Hello {}".format(value))

btn = Button(window, text="Click Here", command=change_text)
btn.place(x=10,y=130)

window.mainloop()