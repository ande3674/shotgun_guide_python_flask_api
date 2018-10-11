import requests
import pyowm
# OpenWeatherMap API
# https://openweathermap.org/appid#get
KEY = '8faf8df6a0906553e13e8a6689203f78'
URL_TEMPLATE_BY_ID = 'http://api.openweathermap.org/data/2.5/forecast?id={CITYID}&APPID=8faf8df6a0906553e13e8a6689203f78'
URL_TEMPLATE_BY_ZIP = 'http://api.openweathermap.org/data/2.5/forecast?zip={CITYZIP}&APPID=8faf8df6a0906553e13e8a6689203f78'
mpls_url = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=8faf8df6a0906553e13e8a6689203f78'
owm = pyowm.OWM(KEY)

def get_weather_at_place(place):
    obs = owm.weather_at_place(place)
    w = obs.get_weather()
    return w

def get_weather_at_coords(lat, lon):
    obs = owm.weather_around_coords(lat, lon)
    w = obs[0].get_weather()
    return w

def get_lon_lat_for_place(place):
    obs = owm.weather_at_place(place)
    lon = obs.get_lon()
    lat = obs.get_lat()
    return lon, lat

def get_statuses_and_temp_at_place(place):
    obs = owm.weather_at_place(place)
    w = obs.get_weather()
    status = w.get_status()
    det_status = w.get_detailed_status()
    temp = w.get_temperature('fahrenheit')['temp']
    return status, det_status, temp

def get_statuses_and_temp_at_coords(lon, lat):
    obs = owm.weather_around_coords(lon, lat)
    w = obs[0].get_weather()
    status = w.get_status()
    det_status = w.get_detailed_status()
    temp = w.get_temperature('fahrenheit')['temp']
    return status, det_status, temp


#################
### TEST CODE ###
#################
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

def print_current_weather(city, w):
    #city = get_city(URL_TEMPLATE_BY_ZIP.format(CITYZIP=57101))
    #w = get_weather(URL_TEMPLATE_BY_ZIP.format(CITYZIP=57101))
    print('Current weather in ' + city)
    print(w['key'] + ': ' + w['description'])
    print('Current temp is ' + str(w['temp']))
    print('Today\'s max temp: ' + str(w['max']) + ', min temp: ' + str(w['min']))

w = get_weather_at_place('Paris, France')
print(w)
print(w.get_status())
print(w.get_detailed_status())
print(w.get_temperature('fahrenheit')['temp'])
print(w.get_temperature('fahrenheit')['temp_max'])
print(w.get_temperature('fahrenheit')['temp_min'])

x= get_weather_at_coords(42.5, -90.5)
print(x)
print(x.get_status())
print(x.get_detailed_status())
print(x.get_temperature('fahrenheit')['temp'])
print(x.get_temperature('fahrenheit')['temp_max'])
print(x.get_temperature('fahrenheit')['temp_min'])

