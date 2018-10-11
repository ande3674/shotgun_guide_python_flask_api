from flask import Flask, request, render_template
from apis import weather_api

app = Flask(__name__)
URL_TEMPLATE_BY_ZIP = 'http://api.openweathermap.org/data/2.5/forecast?zip={CITYZIP}&APPID=8faf8df6a0906553e13e8a6689203f78'

@app.route('/')
def home():
    return render_template('index.html')

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