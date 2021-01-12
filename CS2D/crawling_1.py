import bs4
import urllib.request as url

path = 'https://www.imdb.com/title/tt2631186/?ref_=nv_sr_srsg_0'
response = url.urlopen(path)

page_source = bs4.BeautifulSoup(response)

title_bar = page_source.find('div', class_='title_bar_wrapper')
#print(title_bar.text)
print(' '.join(title_bar.text.split()))
