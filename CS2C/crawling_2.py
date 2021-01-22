import bs4
import urllib.request as url

response = url.urlopen('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc')
page_source = bs4.BeautifulSoup(response, 'lxml')

'''
title = page_source.find('h3', class_='lister-item-header')
print(title.text.replace('\n', ''))
'''
titles = page_source.findAll('h3', class_='lister-item-header')
ratings = page_source.findAll('div', class_='ratings-imdb-rating')

'''
for item in titles:
    print(item.text.replace('\n', ''))
'''
for i in range(len(titles)):
    print(titles[i].text.replace('\n', ''))
    print("Rating :",ratings[i].text.replace('\n', ''))
    print('*' * 50)
    






