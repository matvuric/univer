def get_weather_data(lat=33.44, lon=-94.04, api_key=None, dt=0, city='', days_range=0):
    import requests
    import json

    if api_key:
        result = dict()
        result['city'] = city
        result['temps'] = []
        for i in range(days_range):
            req = requests.get(
                f'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={dt}&'
                f'appid={api_key}&lang=ru&units=metric')
            req_obj = json.loads(req.text)
            measures = [{"dt": str(measure['dt']), "temp": str(measure['temp'])} for measure in req_obj["hourly"]]
            result['temps'].append(measures)
            dt += 86400
        visualise_data(json.dumps(result), days_range)


def visualise_data(json_data='', days_range=0):
    if json_data:
        import matplotlib.pyplot as pplt
        import pandas
        from datetime import datetime

        data = pandas.read_json(json_data)
        dates = [_d['dt'] for _d in data['temps'][0][:]]
        city_name = data['city'].get(0)
        dates_hours, all_temps = [], []

        for i in dates:
            dates_hours.append(datetime.utcfromtimestamp(int(i)).strftime('%H:%M'))

        date1 = datetime.utcfromtimestamp(int(dates[0])).strftime('%d/%m/%Y')
        date2 = datetime.utcfromtimestamp(int(dates[0]) + 86400 * (days_range - 1)).strftime('%d/%m/%Y')

        pplt.figure(figsize=(15, 5))
        pplt.title(f'График температуры в городе {city_name}\nПериод: {date1} - {date2}')
        pplt.xlabel("Время")
        pplt.ylabel("Температура, °C")
        colors = {'g': '1 день', 'r': '2 день', 'b': '3 день', 'y': '4 день', 'm': '5 день'}
        for i in range(days_range):
            temps = [float(_t['temp']) for _t in data['temps'][i][:]]
            all_temps.append(temps)
            pplt.scatter(dates_hours, temps, c=list(colors.keys())[i], label=colors.get(list(colors.keys())[i]))
        pplt.legend(loc='lower right')
        pplt.show()

        avg_temps = [(i - i) for i in range(len(all_temps[0]))]

        for i in all_temps:
            for j in range(len(i)):
                avg_temps[j] += i[j]

        for i in range(len(avg_temps)):
            avg_temps[i] /= 5

        pplt.figure(figsize=(15, 5))
        pplt.title(f'График средней температуры в городе {city_name}\nПериод: {date1} - {date2}')
        pplt.xlabel("Время")
        pplt.ylabel("Температура, °C")
        pplt.scatter(dates_hours, avg_temps)
        pplt.show()


if __name__ == '__main__':
    get_weather_data(55.7522, 37.6156, 'd204de47e2ed49257fc3f7cc51a8dda7', 1637712000, 'Moscow', 5)
