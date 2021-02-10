import bs4
import urllib.request as url

import tkinter
from tkinter import *

window = Tk()
window.geometry('1000x600')

response = url.urlopen('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc')
page_source = bs4.BeautifulSoup(response, 'lxml')

titles = page_source.findAll('h3', class_='lister-item-header')
ratings = page_source.findAll('div', class_='ratings-imdb-rating')

for i in range(20):
    # print(titles[i].text.replace('\n', ''))
    # print("Rating :", ratings[i].text.replace('\n', ''))
    # print('*' * 50)
    m_name = titles[i].text.replace('\n', '')
    m_name = m_name + " | Rating : " + ratings[i].text.replace('\n', '')
    label = Label(window, text=m_name, fg='red',
                  font=('Arial', 14, 'bold'))
    # label.grid(row=i, column=0)
    label.place(x=10, y=25*i)

window.mainloop()



