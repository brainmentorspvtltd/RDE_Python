import urllib.request as url
import bs4

response = url.urlopen('https://www.flipkart.com/search?q=tv')

page = bs4.BeautifulSoup(response, 'lxml')
page.find('div', class_='_4rR01T')

'''
title = page.find('div', class_='_4rR01T')
print(title.text)
'''
titles = page.findAll('div', class_='_4rR01T')
priceList = page.findAll('div', class_='_30jeq3 _1_WHN1')
'''
for item in titles:
    print(item.text)
    print('*' * 20)
'''

for i in range(len(titles)):
    print(titles[i].text)
    print(priceList[i].text)
    print('*' * 20)













