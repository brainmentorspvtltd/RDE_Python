import bs4
import urllib.request as url

page_url = 'https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc'
response = url.urlopen(page_url)

page = bs4.BeautifulSoup(response, 'lxml')
'''
title = page.find('h3', class_='lister-item-header')
print(title.text.replace('\n',''))
'''
titles = page.findAll('h3', class_='lister-item-header')
ratings = page.findAll('div', class_='ratings-imdb-rating')
for i in range(len(titles)):
    print(titles[i].text.replace('\n',''))
    print("Rating :",ratings[i].text.replace('\n',''))
    print('*' * 40)








