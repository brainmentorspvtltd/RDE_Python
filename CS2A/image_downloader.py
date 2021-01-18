import bs4
import urllib.request as url

path = 'https://www.marvel.com/'
response = url.urlopen(path)

page = bs4.BeautifulSoup(response)

images = page.findAll('img')
for i in range(len(images)):
    img_src = images[i].attrs['src']
    url.urlretrieve(img_src, 'img_{}.jpg'.format(i))
    print("Downloaded :",i)
