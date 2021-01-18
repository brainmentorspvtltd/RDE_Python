import bs4
import urllib.request as url

page_url = 'https://www.imdb.com/title/tt7838252/?ref_=nv_sr_srsg_0'
response = url.urlopen(page_url)

page = bs4.BeautifulSoup(response, 'lxml')

title = page.find('div', class_='title_wrapper')
title = title.text
title = title.split()
print(' '.join(title))
