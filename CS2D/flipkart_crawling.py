import bs4
import urllib.request as url

path = 'https://www.flipkart.com/search?q=iphone11'
response = url.urlopen(path)

page = bs4.BeautifulSoup(response, 'lxml')

#title = page.find('div', class_='_4rR01T')

titles = page.findAll('div', class_='_4rR01T')
priceList = page.findAll('div', class_='_30jeq3 _1_WHN1')
'''
for item in titles:
    print(item.text)
    print('-'*20)
'''

for i in range(len(titles)):
    print(titles[i].text)
    print(priceList[i].text)
    print('*' * 40)








