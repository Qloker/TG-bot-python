import requests

API_KEY = '1d442f5e38536b0955c89d1f7fd0f83c'
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(lat, lon):
    params = {'lat': lat, 'lon': lon, 'appid': API_KEY}
    response = requests.get(WEATHER_URL, params = params)
    if response.status_code == 200:
        data = response.json()
        weather_desc = data['weather'][0]['description']
        print(data['weather'])
        temperature = data['main']['temp'] - 273.15
        return weather_desc, temperature
       # return data['weather'][0]['description'], data['main']['temp'] - 273.15
    else:
        return 0, 0


test = get_weather(59, 30)
