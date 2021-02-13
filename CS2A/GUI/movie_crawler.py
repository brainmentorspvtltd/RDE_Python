import bs4
import urllib.request as url

def search_movie(movie):
    movie = movie.replace(' ', '+')
    path = 'https://www.imdb.com/find?q={}&ref_=nv_sr_sm'.format(movie)
    response = url.urlopen(path)
    page = bs4.BeautifulSoup(response, 'lxml')
    td = page.find('td', class_='result_text')
    a_tag = td.find('a')
    #print(a_tag)

    path = 'https://www.imdb.com'+a_tag.attrs['href']
    response = url.urlopen(path)

    page = bs4.BeautifulSoup(response, 'lxml')

    title = page.find('div', class_='title_wrapper')
    title = title.text
    title = title.split()
    # print(' '.join(title))
    rating = page.find('div', class_='ratingValue')
    # print("Rating :", rating.text)

    img_div = page.find('div', class_='poster')
    img_src = img_div.find('img').attrs['src']
    url.urlretrieve(img_src, 'img_1.jpg')

    return title, rating.text
