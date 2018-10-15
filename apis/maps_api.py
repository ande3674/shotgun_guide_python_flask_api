import requests, googlemaps

# Google Maps API
GOOGLE_KEY = 'AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc'
GOOGLE_KEY2 = "AIzaSyBRkvf3BQmjTKQ2Lbxt97ZmFgCIAILuIP0"
DIRECTIONS_URL_TEMPLATE = 'https://maps.googleapis.com/maps/api/directions/json?origin={ORIGIN}' \
                         '&destination={DESTINATION}&key=AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc'
STATIC_MAP_URL = 'https://maps.googleapis.com/maps/api/staticmap?center={CENTER}' \
                 '&zoom={ZOOM}&size=600x400&maptype={TYPE}&key=AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc' #types:roadmap, satellite, hybrid, terrain,

def reverse_geocode_place(lat, lon):
    l = str(lat) + "," + str(lon)
    U = 'https://maps.googleapis.com/maps/api/geocode/json?latlng={LL}&key=AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc'.format(LL=l)
    response = requests.get(U).json()
    return response
def get_static_map_of_place(place):
    place = split_up(place)
    url = STATIC_MAP_URL.format(CENTER=place, ZOOM=10, TYPE='roadmap')
    return url
def get_static_map_of_coords(lat, lon):
    url = STATIC_MAP_URL.format(CENTER=str(lat)+','+str(lon), ZOOM=10, TYPE='roadmap')
    return url
def get_directions(place1, place2):
    url = DIRECTIONS_URL_TEMPLATE.format(ORIGIN=place1, DESTINATION=place2)
    response = requests.get(url).json()
    routes = response['routes'][0]
    legs = routes['legs'][0]
    steps = legs['steps']
    return steps
def get_directions1(url):
    response = requests.get(url).json()
    routes = response['routes'][0]
    legs = routes['legs'][0]
    steps = legs['steps']
    return steps
def get_midway_location(steps):
    num_steps = len(steps)
    location_data = steps[round(num_steps/2)]
    lat = location_data['end_location']['lat']
    long = location_data['end_location']['lng']
    return lat, long

def get_stops(place1, place2):
    url = DIRECTIONS_URL_TEMPLATE.format(ORIGIN=place1, DESTINATION=place2)
    response = requests.get(url).json()
    routes = response['routes'][0]
    legs = routes['legs'][0]
    seconds = legs['duration']['value']
    #
    max_num_stops = int(seconds / 7200)-1
    steps = legs['steps']
    stops = []
    timer = 0
    num_stops = 0
    for i in range(len(steps)):
        timer += steps[i]['duration']['value']
        if len(stops) >= max_num_stops:
            break
        if int(timer/7200) > num_stops:
            num_stops += 1
            # add a stop by getting the lat and lon at this current location
            loc = (steps[i]['end_location']['lat'], steps[i]['end_location']['lng'])
            stops.append(loc)
    return stops

def split_up(s):
    split = s.split(" ")
    return_string = ''
    for i in range(len(split)):
        if i == len(split)-1:
            return_string += split[i]
        else:
            return_string += (split[i] + '+')
    return return_string

##############
# TEST STUFF #
##############
# from pygeocoder import Geocoder
# import pygeolib
# import reverse_geocode as rg
# from googlemaps.client import geocode, reverse_geocode#, MANY MORE?
# from datetime import datetime
# import geocoder
# DIRECTIONS_URL_EXAMPLE1 = 'https://maps.googleapis.com/maps/api/directions/json?origin=44.9778,93.2650' \
#'&destination=25.7617,80.1918&key=AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc'
# DIRECTIONS_URL_EXAMPLE2 = 'https://maps.googleapis.com/maps/api/directions/json?origin=minneapolis&destination=miami&key=AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc'

# gmaps = googlemaps.Client(key=GOOGLE_KEY2)
# def geocode_place(place):
#     return geocode(gmaps, place)
# def reverse_geocode_place(long, lati):
#     #base = "http://maps.googleapis.com/maps/api/geocode/json?"
#     #params = "latlng={lat},{lon}&sensor=false".format(lat=lati, lon=long)
#     #url = "{base}{params}".format(base=base, params=params)
#     #response = requests.get(url).json()
#     #return response
#     return reverse_geocode(gmaps, (long, lati))
#s = get_directions(DIRECTIONS_URL_EXAMPLE2)
#lat, long = get_midway_location(s)
#print('lat: ' + str(lat) + ", long: " + str(long))
#gp = geocode_place('Paris, France')
#print(gp)
#p = reverse_geocode_place(gp)
# #print(p)
#p = reverse_geocode_place(44.9778, 93.2650)
#print(p)
# s = get_stops('boston', 'miami')
# for i in range(len(s)):
#     print(s[i])