import json
import urllib.request as url

path = 'https://cricapi.com/api/playerStats?apikey=b7CYzlyYOrUCIIdbSlU753oGKN12&pid=28081'

response = url.urlopen(path)
data = json.load(response)

data_1 = data['data']
bat = data_1['batting']
odi = bat['ODIs']
print(odi)
