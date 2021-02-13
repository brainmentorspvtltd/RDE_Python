import bs4
import urllib.request as url

from tkinter import *

window = Tk()
window.geometry('800x400')

response = url.urlopen('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc')
page_source = bs4.BeautifulSoup(response, 'lxml')

titles = page_source.findAll('h3', class_='lister-item-header')
ratings = page_source.findAll('div', class_='ratings-imdb-rating')

scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)

movies_list = Listbox(window, yscrollcommand=scrollbar.set,
                      width=700,
                      font=('Arial', 15))

for i in range(len(titles)):
    m_name = titles[i].text.replace('\n', '')
    # m_name = m_name + " | Rating : " + ratings[i].text.replace('\n', '')
    m_rating = "Rating : " + ratings[i].text.replace('\n', '')
    # label = Label(window, text=m_name, fg='red',
    #               font=('Arial', 14, 'bold'))
    # label.grid(row=i, column=0)
    # label.place(x=10, y=25*i)
    movies_list.insert(END, m_name)
    movies_list.insert(END, m_rating)
    movies_list.insert(END, '*' * 100)

movies_list.pack(side=LEFT, fill = BOTH)
scrollbar.config(command = movies_list.yview)

window.mainloop()



