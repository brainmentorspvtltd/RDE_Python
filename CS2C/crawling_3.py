import bs4
import urllib.request as url

movie = input("Enter movie name : ")
movie = movie.replace(' ', '+')
path = 'https://www.imdb.com/find?q={}&ref_=nv_sr_sm'.format(movie)

res = url.urlopen(path)
page = bs4.BeautifulSoup(res, 'lxml')
td = page.find('td', class_='result_text')
a_tag = td.find('a')
href = a_tag.attrs['href']
path = 'https://www.imdb.com/' + href

response = url.urlopen(path)
page_source = bs4.BeautifulSoup(response, 'lxml')

title = page_source.find('h1')
print(title.text)

rating = page_source.find('div', class_='ratingValue')
print(rating.text)

summary = page_source.find('div', class_='summary_text')
print(summary.text)

