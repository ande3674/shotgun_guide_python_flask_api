import requests, random
from apis import maps_api

GOOGLE_KEY = 'AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc'
PLACE_TYPE_LIST = [ 'restaurant', 'zoo', 'park', 'shopping_mall', 'museum' ]
PLACE_SEARCH_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={LATLON}&radius=3000' \
                   '&type={TYPE}&keyword={KEY}&key=AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc'
PLACE_SEARCH_URL1 = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={LATLON}&radius=17000' \
                   '&type={TYPE}&key=AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc'


def get_place_name(lat, lon, list_suggestion=0):
    try:
        r = random.randint(0, len(PLACE_TYPE_LIST)-1)
        typ = PLACE_TYPE_LIST[list_suggestion]
        # url = PLACE_SEARCH_URL.format(LATLON=format_lat_lon(lat, lon), TYPE=typ, KEY='popular')
        url = PLACE_SEARCH_URL1.format(LATLON=format_lat_lon(lat, lon), TYPE=typ)
        response = requests.get(url).json()
        result = response['results'][0]
        name = result['name']
        return name
    except IndexError:
        return 'No suggestion for this area'


def format_lat_lon(lat, lon):
    return str(lat) + "," + str(lon)