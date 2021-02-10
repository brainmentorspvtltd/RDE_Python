import tkinter
from tkinter import *

window = Tk()
window.geometry('400x400')

label = Label(window, text="Hello Python", foreground='red',
              font=('Arial',28,'bold'))
# label.pack()
# label.grid(row=0,column=0)
label.place(x = 10, y = 10)

window.mainloop()