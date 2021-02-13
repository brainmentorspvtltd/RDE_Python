from tkinter import *

window = Tk()
window.geometry('500x400')

label = Label(window, text="Greet App", foreground='red',
              font=('Arial', 25), bg='yellow')
label.pack(fill=BOTH)

entry = Entry(window, font=('Arial', 18))
entry.place(x=10, y=100)

label_2 = Label(window, text="", foreground='red',
              font=('Arial', 25), bg='yellow')
label_2.place(x=10, y=200)

def greet():
    name = entry.get()
    msg = "Hello " + name
    label_2.configure(text=msg)

btn = Button(window, text="Click Here",fg='white', bg='red',
             font=('Arial',14), command=greet)
btn.place(x=340, y=100)

window.mainloop()