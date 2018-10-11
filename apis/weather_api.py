import requests
# OpenWeatherMap API
KEY = '8faf8df6a0906553e13e8a6689203f78'
URL_TEMPLATE_BY_ID = 'http://api.openweathermap.org/data/2.5/forecast?id={CITYID}&APPID=8faf8df6a0906553e13e8a6689203f78'
URL_TEMPLATE_BY_ZIP = 'http://api.openweathermap.org/data/2.5/forecast?zip={CITYZIP}&APPID=8faf8df6a0906553e13e8a6689203f78'
mpls_url = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=8faf8df6a0906553e13e8a6689203f78'


def get_city(url):
    response = requests.get(url).json()
    return response['city']['name']
def get_weather(url):
    response = requests.get(url).json()
    weather_list = response['list']
    weather_obj = weather_list[0]
    temp = convert_to_fahrenheit(weather_obj['main']['temp'])
    temp_min = convert_to_fahrenheit(weather_obj['main']['temp_min'])
    temp_max =  convert_to_fahrenheit(weather_obj['main']['temp_max'])
    weather_main_desc = weather_obj['weather'][0]['main']
    weather_desc = weather_obj['weather'][0]['description']
    weather_dict = {'key' : weather_main_desc, 'description' : weather_desc, 'temp' : round(temp), 'max': round(temp_max), 'min': round(temp_min) }
    return weather_dict
def convert_to_fahrenheit(kel):
    return (1.8 * (kel - 273)) + 32

### TEST CODE ###
def print_current_weather(city, w):
    #city = get_city(URL_TEMPLATE_BY_ZIP.format(CITYZIP=57101))
    #w = get_weather(URL_TEMPLATE_BY_ZIP.format(CITYZIP=57101))
    print('Current weather in ' + city)
    print(w['key'] + ': ' + w['description'])
    print('Current temp is ' + str(w['temp']))
    print('Today\'s max temp: ' + str(w['max']) + ', min temp: ' + str(w['min']))

