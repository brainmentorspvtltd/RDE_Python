import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry('300x300')

# Label - used to display text
# Entry - Textbox - Single line Edit
# Text  - Comments, Messages - Multi line Edit
# Button - make clickable buttons

label = Label(window, text="Hello Python", foreground='red', background='yellow')
# label.pack()
label.grid(row=0, column=0)

label = Label(window, text="Hello This is Tkinter", fg='blue', bg='yellow')
# label.pack()
label.grid(row=1, column=1)

# pack
# grid
# place

window.mainloop()