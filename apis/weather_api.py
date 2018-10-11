import requests
# OpenWeatherMap API

KEY = '8faf8df6a0906553e13e8a6689203f78'
URL_TEMPLATE_BY_ID = 'http://api.openweathermap.org/data/2.5/forecast?id={CITYID}&APPID=8faf8df6a0906553e13e8a6689203f78'
URL_TEMPLATE_BY_ZIP = 'http://api.openweathermap.org/data/2.5/forecast?zip={CITYZIP}&APPID=8faf8df6a0906553e13e8a6689203f78'
mpls_url = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=8faf8df6a0906553e13e8a6689203f78'


def get_city(url):
    response = requests.get(url).json()
    return response['city']['name']
city = get_city(URL_TEMPLATE_BY_ZIP.format(CITYZIP=33101))
print(city)