import bs4
import urllib.request as url

path = 'https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc'
response = url.urlopen(path)

page_source = bs4.BeautifulSoup(response)

movie_name = page_source.find_all('h3', class_='lister-item-header')

ratings = page_source.find_all('div', class_='ratings-imdb-rating')

'''
for item in movie_name:
    print(item.text)
    print('-'*20)
'''

for i in range(len(movie_name)):
    print(movie_name[i].text.strip())
    print("Rating :",ratings[i].text.strip())
    print('-'*20)





