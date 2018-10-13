import requests, googlemaps
from googlemaps.client import geocode, reverse_geocode#, MANY MORE WILL BE USEFUL!!!!!!!
from datetime import datetime

# Google Maps API
GOOGLE_KEY = 'AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc'
DIRECTIONS_URL_TEMPLATE = 'https://maps.googleapis.com/maps/api/directions/json?origin={ORIGIN}' \
                         '&destination={DESTINATION}&key=AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc'
STATIC_MAP_URL = 'https://maps.googleapis.com/maps/api/staticmap?center={CENTER}' \
                 '&zoom={ZOOM}&size=600x400&maptype={TYPE}&key=AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc' #types:roadmap, satellite, hybrid, terrain,
DIRECTIONS_URL_EXAMPLE1 = 'https://maps.googleapis.com/maps/api/directions/json?origin=44.9778,93.2650' \
                         '&destination=25.7617,80.1918&key=AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc'
DIRECTIONS_URL_EXAMPLE2 = 'https://maps.googleapis.com/maps/api/directions/json?origin=minneapolis&destination=miami&key=AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc'

gmaps = googlemaps.Client(key='AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc')


def geocode_place(place):
    return geocode(gmaps, place)
def reverse_geocode_place(lon, lat):
    return reverse_geocode(gmaps, (lat, lon))

def get_static_map_of_place(place):
    place = split_up(place)
    url = STATIC_MAP_URL.format(CENTER=place, ZOOM=10, TYPE='roadmap')
    return url
def get_static_map_of_coords(lon, lat):
    url = STATIC_MAP_URL.format(CENTER=str(lon)+','+str(lat), ZOOM=10, TYPE='roadmap')
    return url
def get_directions(place1, place2):
    url = DIRECTIONS_URL_TEMPLATE.format(ORIGIN=place1, DESTINATION=place2)
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

def split_up(s):
    split = s.split(" ")
    return_string = ''
    for i in range(len(split)):
        if i == len(split)-1:
            return_string += split[i]
        else:
            return_string += (split[i] + '+')
    return return_string

def get_directions1(url):
    response = requests.get(url).json()
    routes = response['routes'][0]
    legs = routes['legs'][0]
    steps = legs['steps']
    return steps

##############
# TEST STUFF #
##############

#s = get_directions(DIRECTIONS_URL_EXAMPLE2)
#lat, long = get_midway_location(s)
#print('lat: ' + str(lat) + ", long: " + str(long))
#gp = geocode_place('Paris, France')
#print(gp)
#p = reverse_geocode_place(gp)
#print(p)
