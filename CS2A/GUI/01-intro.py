from tkinter import *

window = Tk()
window.geometry('400x400')

label = Label(window, text="Enter your name", foreground='red',
              font=('Arial', 25), bg='yellow')
# label.pack(fill = BOTH)
# label.grid(row=0, column=0, padx=20, pady=20)
label.place(x=20, y=40)

# pack
# grid
# place

window.mainloop()