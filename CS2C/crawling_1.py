import bs4
import urllib.request as url

response = url.urlopen('https://www.imdb.com/title/tt0371746/?ref_=nv_sr_srsg_0')
page_source = bs4.BeautifulSoup(response)

title = page_source.find('h1')
print(title.text)

rating = page_source.find('div', class_='ratingValue')
print(rating.text)

summary = page_source.find('div', class_='summary_text')
print(summary.text)
