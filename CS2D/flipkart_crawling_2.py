import bs4
import urllib.request as url

query = input("Enter your query : ")
query = query.replace(' ', '+')
for i in range(1,5):
    print('Page : {}'.format(i))
    path = 'https://www.flipkart.com/search?q={}&page={}'.format(query,i)
    response = url.urlopen(path)

    page = bs4.BeautifulSoup(response, 'lxml')

    #title = page.find('div', class_='_4rR01T')

    titles = page.findAll('div', class_='_4rR01T')
    priceList = page.findAll('div', class_='_30jeq3 _1_WHN1')

    for j in range(len(titles)):
        print(titles[j].text)
        print(priceList[j].text)
        print('*' * 40)

    







