import json
import urllib.request as url

response = url.urlopen('https://cricapi.com/api/playerStats?apikey=b7CYzlyYOrUCIIdbSlU753oGKN12&pid=253802')
data = json.load(response)
print(data['profile'])
