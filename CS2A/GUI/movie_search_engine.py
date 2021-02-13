from tkinter import *
import movie_crawler
import PIL
from PIL import ImageTk

window = Tk()
window.geometry('1000x500')

label = Label(window, text="Movie Search App", foreground='red',
              font=('Arial', 25), bg='yellow')
label.pack(fill=BOTH)

entry = Entry(window, font=('Arial', 18))
entry.place(x=10, y=100)

label_2 = Label(window, text="", foreground='red',
              font=('Arial', 15), wraplength=400)
label_2.place(x=10, y=200)

label_3 = Label(window, text="", foreground='red',
              font=('Arial', 15))
label_3.place(x=10, y=250)

def search():
    name = entry.get()
    title, rating = movie_crawler.search_movie(name)
    label_2.configure(text=title)
    label_3.configure(text=rating)

    img = PIL.Image.open('img_1.jpg')
    render = ImageTk.PhotoImage(img)

    label_4 = Label(window, foreground='red',
                    font=('Arial', 15), image=render)
    label_4.image = render
    label_4.place(x=600, y=150)

btn = Button(window, text="Click Here",fg='white', bg='red',
             font=('Arial',14), command=search)
btn.place(x=340, y=100)

window.mainloop()