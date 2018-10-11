import requests
# Google Maps API
GOOGLE_KEY = 'AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc'
# MapQuest API
MAPQUEST_KEY = '8ET6X9Q2Uwf6TCAQHk5FNeDrjT1SC5Id'
MAPQUEST_SECRET = 'BAIytvgECoeYE8EK'

DIRECTIONS_URL_TEMPLATE = 'https://maps.googleapis.com/maps/api/directions/json?origin={ORIGIN}' \
                         '&destination={DESTINATION}&key=AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc'
STATIC_MAP_URL = 'https://maps.googleapis.com/maps/api/staticmap?center={CENTER}' \
                 '&zoom={ZOOM}&size=600x400&maptype={TYPE}&key=AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc' #types:roadmap, satellite, hybrid, terrain,
DIRECTIONS_URL_EXAMPLE1 = 'https://maps.googleapis.com/maps/api/directions/json?origin=44.9778,93.2650' \
                         '&destination=25.7617,80.1918&key=AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc'
DIRECTIONS_URL_EXAMPLE2 = 'https://maps.googleapis.com/maps/api/directions/json?origin=minneapolis&destination=miami&key=AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc'

#https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key=AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc
def get_static_map_of_place(place):
    place = split_up(place)
    url = STATIC_MAP_URL.format(CENTER=place, ZOOM=10, TYPE='roadmap')
    #response = requests.get(url)
    return url

def split_up(s):
    split = s.split(" ")
    return_string = ''
    for i in range(len(split)):
        if i == len(split)-1:
            return_string += split[i]
        else:
            return_string += (split[i] + '+')
    return return_string

def get_directions(url):
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


s = get_directions(DIRECTIONS_URL_EXAMPLE2)
lat, long = get_midway_location(s)
print('lat: ' + str(lat) + ", long: " + str(long))
