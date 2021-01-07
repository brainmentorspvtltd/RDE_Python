Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import bs4
>>> import urllib.request as url
>>> url.urlopen('https://www.imdb.com/title/tt3501632/?ref_=nv_sr_srsg_0')
<http.client.HTTPResponse object at 0x000001D142257EB0>
>>> response = url.urlopen('https://www.imdb.com/title/tt3501632/?ref_=nv_sr_srsg_0')
>>> page_source = bs4.BeautifulSoup(response)
>>> page_source.find('div', class_='ipc-html-content')
>>> page_source.find('div', class_='summary_text')
<div class="summary_text">
                    Imprisoned on the planet Sakaar, Thor must race against time to return to Asgard and stop Ragnarök, the destruction of his world, at the hands of the powerful and ruthless villain Hela.
            </div>
>>> summary = page_source.find('div', class_='summary_text')
>>> summary.text
'\n                    Imprisoned on the planet Sakaar, Thor must race against time to return to Asgard and stop Ragnarök, the destruction of his world, at the hands of the powerful and ruthless villain Hela.\n            '
>>> print(summary.text)

                    Imprisoned on the planet Sakaar, Thor must race against time to return to Asgard and stop Ragnarök, the destruction of his world, at the hands of the powerful and ruthless villain Hela.
            
>>> 