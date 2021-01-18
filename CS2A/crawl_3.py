import bs4
import urllib.request as url

movie = input("Enter movie name : ")
movie = movie.replace(' ', '+')
path = 'https://www.imdb.com/find?q={}&ref_=nv_sr_sm'.format(movie)
response = url.urlopen(path)
page = bs4.BeautifulSoup(response, 'lxml')
td = page.find('td', class_='result_text')
a_tag = td.find('a')
#print(a_tag)

path = 'https://www.imdb.com'+a_tag.attrs['href']
response = url.urlopen(path)

page = bs4.BeautifulSoup(response, 'lxml')

title = page.find('div', class_='title_wrapper')
title = title.text
title = title.split()
print(' '.join(title))

