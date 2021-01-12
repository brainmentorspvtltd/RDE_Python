import urllib.request as url
import bs4

query = input("Enter your query : ")
query = query.replace(' ', '+')
for i in range(1,5):
    print(f"Page : {i}")
    response = url.urlopen('https://www.flipkart.com/search?q={}&page={}'.format(query,i))

    page = bs4.BeautifulSoup(response, 'lxml')
    page.find('div', class_='_4rR01T')

    titles = page.findAll('div', class_='_4rR01T')
    priceList = page.findAll('div', class_='_30jeq3 _1_WHN1')
    for j in range(len(titles)):
        print(titles[j].text)
        print(priceList[j].text)
        print('*' * 20)













