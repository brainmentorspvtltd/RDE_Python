Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> msg = 'open facebook'
>>> website = 'facebook'
>>> import webbrowser
>>> webbrowser.open(website+'.com')
True
>>> msg = 'open twitter'
>>> website = 'twitter'
>>> webbrowser.open(website+'.com')
True
>>> 'open' in msg
True
>>> msg.startswith('open')
True
>>> 