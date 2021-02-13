from tkinter import *
import tkinter.font as font

window = Tk()
window.geometry('300x400')
window.title('Basic Calc')
window.resizable(0,0)

expression = StringVar()
customFont = font.Font(size=16)

text_box = Entry(window, text=expression, width=25, justify='right',
                 font=(12))
text_box.grid(row=0, columnspan=4, padx=10, pady=10, ipady=5)

buttons = [
    ['c', '<-', '%', '='],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '/'],
    ['1', '2', '3', '-'],
    ['.', '0', 'e', '+'],
]

def calculate(event):
    # print(event.widget.cget('text'))
    expression = event.widget.cget('text')
    if expression == "=":
        result = eval(text_box.get())
        text_box.delete(0, END)
        text_box.insert(0, result)
    else:
        value = text_box.get()
        text_box.insert(len(value), expression)


buttons_dict = {}
for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        current_btn = 'btn_{}'.format(buttons[i][j])
        btn = Button(window, text = str(buttons[i][j]),
                     font = customFont, bg='red', width=3)
        buttons_dict[current_btn] = btn

        buttons_dict[current_btn].grid(row = i + 1, column = j,
                                       padx = 5, pady = 5, ipadx = 5, ipady = 5)

        buttons_dict[current_btn].bind('<Button-1>', calculate)

window.mainloop()




