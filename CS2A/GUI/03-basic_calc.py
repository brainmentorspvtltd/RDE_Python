from tkinter import *

window = Tk()
window.geometry('800x400')

label = Label(window, text="Basic Calc App", foreground='red',
              font=('Arial', 25), bg='yellow')
label.grid(row=0, column=0, columnspan=2)

label_2 = Label(window, text="Enter first number", foreground='red',
              font=('Arial', 18), bg='yellow')
label_2.grid(row=1, column=0, padx=20, pady=20, columnspan=2)
entry = Entry(window, font=('Arial', 18))
entry.grid(row=1, column=2, padx=20, pady=20, columnspan=2)

label_3 = Label(window, text="Enter second number", foreground='red',
              font=('Arial', 18), bg='yellow')
label_3.grid(row=2, column=0, padx=20, pady=20, columnspan=2)
entry_2 = Entry(window, font=('Arial', 18))
entry_2.grid(row=2, column=2, padx=20, pady=20, columnspan=2)

label_4 = Label(window, text="Result", foreground='red',
              font=('Arial', 18), bg='yellow')
label_4.grid(row=3, column=0, padx=20, pady=20, columnspan=2)
entry_3 = Entry(window, font=('Arial', 18))
entry_3.grid(row=3, column=2, padx=20, pady=20, columnspan=2)

def add():
    num_1 = int(entry.get())
    num_2 = int(entry_2.get())
    result = num_1 + num_2
    entry_3.delete(0, END)
    entry_3.insert(0,result)

def sub():
    num_1 = int(entry.get())
    num_2 = int(entry_2.get())
    result = num_1 - num_2
    entry_3.delete(0, END)
    entry_3.insert(0,result)

def div():
    num_1 = int(entry.get())
    num_2 = int(entry_2.get())
    result = num_1 / num_2
    entry_3.delete(0, END)
    entry_3.insert(0,result)

def mul():
    num_1 = int(entry.get())
    num_2 = int(entry_2.get())
    result = num_1 * num_2
    entry_3.delete(0, END)
    entry_3.insert(0,result)

btn_1 = Button(window, text="+", font=('Arial',14), width=4, command=add)
btn_1.grid(row=4, column=0)

btn_2 = Button(window, text="-", font=('Arial',14), width=4, command=sub)
btn_2.grid(row=4, column=1)

btn_3 = Button(window, text="/", font=('Arial',14), width=4, command=div)
btn_3.grid(row=4, column=2)

btn_4 = Button(window, text="*", font=('Arial',14), width=4, command=mul)
btn_4.grid(row=4, column=3)

window.mainloop()