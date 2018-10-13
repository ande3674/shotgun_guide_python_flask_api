from flask import Flask, request, render_template
from apis import weather_api, maps_api
from googlemaps.client import geocode, reverse_geocode
#from flask_bootstrap import Bootstrap

app = Flask(__name__)
#bootstrap = Bootstrap(app)
URL_TEMPLATE_BY_ZIP = 'http://api.openweathermap.org/data/2.5/forecast?zip={CITYZIP}&APPID=8faf8df6a0906553e13e8a6689203f78'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/trip')
def get_trip():
    # Get info on the origin & destination locations: name, longitude and latitude
    origin = request.args.get('origin')
    #origin_lon, origin_lat = weather_api.get_lon_lat_for_place(origin)
    #origin_ditc = {'name':origin, 'lon':origin_lon, 'lat':origin_lat}
    dest = request.args.get('destination')
    #dest_lon, dest_lat = weather_api.get_lon_lat_for_place(dest)
    #dest_ditc = {'name': dest, 'lon': dest_lon, 'lat': dest_lat}

    # get weather info for these places
    ostatus1, ostatus2, otemp = weather_api.get_statuses_and_temp_at_place(origin)
    dstatus1, dstatus2, dtemp = weather_api.get_statuses_and_temp_at_place(dest)
    # get a map for these places
    ourl = maps_api.get_static_map_of_place(origin)
    durl = maps_api.get_static_map_of_place(dest)

    # get info about a point along the way
    midway_step = maps_api.get_directions(origin, dest)
    midway_lon, midway_lat = maps_api.get_midway_location(midway_step)
    # get the closest city to this place! TODO
    mplace = maps_api.reverse_geocode_place(midway_lon, midway_lat)
    mplace_name = mplace[0]['formatted_address']#['formatted_address']
    mstatus1, mstatus2, mtemp = weather_api.get_statuses_and_temp_at_coords(midway_lon, midway_lat)
    murl = maps_api.get_static_map_of_coords(midway_lon, midway_lat)

    return render_template('trip.html', city1=origin, key1=ostatus1, description1=ostatus2, temp1=otemp, url1=ourl,
                           city2=dest, key2=dstatus1, description2=dstatus2, temp2=dtemp, url2=durl,
                           city3=mplace_name, key3=mstatus1, description3=mstatus2, temp3=mtemp, url3=murl)


### This is just for testing - delete later ###
@app.route('/city')
def get_city():
    # get the user entry from the form
    zip1 = request.args.get('origin')
    zip2 = request.args.get('destination')
    # get city and weather info from weather api
    city1 = weather_api.get_city(URL_TEMPLATE_BY_ZIP.format(CITYZIP=zip1))
    w1 = weather_api.get_weather(URL_TEMPLATE_BY_ZIP.format(CITYZIP=zip1))
    city2 = weather_api.get_city(URL_TEMPLATE_BY_ZIP.format(CITYZIP=zip2))
    w2 = weather_api.get_weather(URL_TEMPLATE_BY_ZIP.format(CITYZIP=zip2))
    # set the variables that the form needs from the weather dictionary
    key1 = w1['key']
    description1 = w1['description']
    temp1 = w1['temp']
    key2 = w2['key']
    description2 = w2['description']
    temp2 = w2['temp']

    return render_template('city.html', city1=city1, key1=key1, description1=description1, temp1=temp1,
                           city2=city2, key2=key2, description2=description2, temp2=temp2)


if __name__ == '__main__':
    app.run()