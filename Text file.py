import requests
r = requests.get('https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key')
with open('weather.py','wb') as f:
    f.write(r.content)
