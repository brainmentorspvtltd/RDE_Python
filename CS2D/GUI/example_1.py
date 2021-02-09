import bs4
import urllib.request as url
from tkinter import *
import tkinter as tk

path = 'https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc'
response = url.urlopen(path)
page_source = bs4.BeautifulSoup(response)
movie_name = page_source.find_all('h3', class_='lister-item-header')
ratings = page_source.find_all('div', class_='ratings-imdb-rating')

window = tk.Tk()
window.geometry('500x500')

for i in range(10):
    label_1 = Label(window, text = movie_name[i].text.strip().replace("\n",""))
    label_1.grid(row=i,column=0)
    # label_2 = Label(window, text="-----------------------------------")
    # label_2.grid(row=i + 1,column=0)
    label_3 = Label(window, text="Rating : "+ratings[i].text.strip().replace("\n",""))
    label_3.grid(row=i,column=1)
    # print(movie_name[i].text.strip())
    # print("Rating :",ratings[i].text.strip())
    # print('-'*20)

window.mainloop()



