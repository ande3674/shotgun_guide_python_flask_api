import requests, random
from apis import maps_api

GOOGLE_KEY = 'AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc'
PLACE_TYPE_LIST = [ 'restaurant', 'zoo', 'park', 'shoppng_mall', 'museum' ]
PLACE_SEARCH_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={LATLON}&radius=3000' \
                   '&type={TYPE}&keyword={KEY}&key=AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc'

def get_place_name(lat, lon):
    r = random.randint(0, len(PLACE_TYPE_LIST)-1)
    type = PLACE_TYPE_LIST[0]
    url = PLACE_SEARCH_URL.format(LATLON=format_lat_lon(lat, lon), TYPE=type, KEY='popular')
    response = requests.get(url).json()
    result = response['results'][0]
    name = result['name']
    return name

def format_lat_lon(lat, lon):
    return str(lat) + "," + str(lon)

# stops = maps_api.get_stops('minneapolis', 'chicago')
# p = get_place_name(stops[1][0], stops[1][1])
# print(p)