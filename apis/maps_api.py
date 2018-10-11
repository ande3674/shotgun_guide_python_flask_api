import requests
# Google Maps API
GOOGLE_KEY = 'AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc'
# MapQuest API
MAPQUEST_KEY = '8ET6X9Q2Uwf6TCAQHk5FNeDrjT1SC5Id'
MAPQUEST_SECRET = 'BAIytvgECoeYE8EK'

DIRECTIONS_URL_TEMPLATE = 'https://maps.googleapis.com/maps/api/directions/json?origin={ORIGIN}' \
                         '&destination={DESTINATION}&key=AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc'

DIRECTIONS_URL_EXAMPLE1 = 'https://maps.googleapis.com/maps/api/directions/json?origin=44.9778,93.2650' \
                         '&destination=25.7617,80.1918&key=AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc'
DIRECTIONS_URL_EXAMPLE2 = 'https://maps.googleapis.com/maps/api/directions/json?origin=minneapolis&destination=miami&key=AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc'

#https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key=AIzaSyCUzzNpRfSkRPbdOHtrjnlfCaCZ26cNKnc


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
