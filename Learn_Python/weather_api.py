from pprint import pprint
import requests


s = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Chicago&APPID=289d79262f138bd6ebb226285fd277e3')

#print(s.json())
# pprint(s.json())


print(s.json()['base'])
