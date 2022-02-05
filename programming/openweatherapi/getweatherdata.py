import requests
import json


def get_weather_data(city='', api_key=None):
    try:
        res = requests.get("https://api.openweathermap.org/data/2.5/weather",
                           params={'q': city, 'units': 'metric', 'APPID': api_key})
        data = res.json()
        d_timezone = int(data['timezone']) // 3600
        if d_timezone > 0:
            timezone_value = 'UTC+' + str(d_timezone)
        else:
            timezone_value = 'UTC' + str(d_timezone)
        return json.dumps({'name': data['name'], 'coord': data['coord'], 'country': data['sys']['country'],
                           'feels like': data['main']['feels_like'],
                           'timezone': timezone_value})
    except Exception as error:
        print("Exception:", error)
        pass
