from flask import Flask, request, render_template
from apis import weather_api, maps_api, bing_api, places_api
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
    try:
        # Get info on the origin & destination locations: name, longitude and latitude
        origin = request.args.get('origin')
        #origin_lat, origin_lon = weather_api.get_lon_lat_for_place(origin)
        #origin_ditc = {'name':origin, 'lon':origin_lon, 'lat':origin_lat}
        dest = request.args.get('destination')
        #dest_lat, dest_lon = weather_api.get_lon_lat_for_place(dest)
        #dest_ditc = {'name': dest, 'lon': dest_lon, 'lat': dest_lat}
        all_coords = maps_api.get_origin_dest_coords(origin, dest)
        origin_coords = all_coords[0]
        dest_coords = all_coords[1]

        # get weather info for these places
        ostatus1, ostatus2, otemp = weather_api.get_statuses_and_temp_at_place(origin)
        dstatus1, dstatus2, dtemp = weather_api.get_statuses_and_temp_at_place(dest)
        # get a map for these places
        ourl = maps_api.get_static_map_of_place(origin)
        durl = maps_api.get_static_map_of_place(dest)
        # get something to do for these places
        otodo = places_api.get_place_name(origin_coords[0], origin_coords[1], 3)
        dtodo = places_api.get_place_name(dest_coords[0], dest_coords[1], 4)

         # get info about a point along the way
        midway_step = maps_api.get_directions(origin, dest)
        midway_lat, midway_lon = maps_api.get_midway_location(midway_step)
         # get the closest city to this place
        mplace = bing_api.reverse_geocode_place(midway_lat, midway_lon)
         # get weather
        mstatus1, mstatus2, mtemp = weather_api.get_statuses_and_temp_at_coords(midway_lat, midway_lon)
        murl = maps_api.get_static_map_of_coords(midway_lat, midway_lon)

        stops_in_between = maps_api.get_stops(origin, dest)
        stop_data_list = []
        for s in stops_in_between:
            lat = s[0]
            lon = s[1]
            place_name=bing_api.reverse_geocode_place(lat, lon)
            status1, status2, temp = weather_api.get_statuses_and_temp_at_coords(lat, lon)
            url = maps_api.get_static_map_of_coords(lat, lon)
            something_to_do = places_api.get_place_name(lat, lon)
            stop_data = {}
            stop_data['name']=place_name
            stop_data['key'] = status1
            stop_data['description'] = status2
            stop_data['temp'] = temp
            stop_data['url'] = url
            stop_data['todo'] = something_to_do
            stop_data_list.append(stop_data)

        all_stops = [origin_coords]
        for stop in stops_in_between:
            all_stops.append(stop)
        all_stops.append(dest_coords)
        main_map_url = maps_api.build_main_map_url(all_stops)

        return render_template('trip.html', mainmap=main_map_url, city1=origin, key1=ostatus1, description1=ostatus2, temp1=otemp, url1=ourl, todo1=otodo,
                               city2=dest, key2=dstatus1, description2=dstatus2, temp2=dtemp, url2=durl, todo2=dtodo,
                               city3=mplace, key3=mstatus1, description3=mstatus2, temp3=mtemp, url3=murl, stops=stop_data_list)

    except IndexError:
        return render_template('error.html')


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