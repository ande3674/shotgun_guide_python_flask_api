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
    zip = request.args.get('city')
    # get city and weather info from weather api
    city = weather_api.get_city(URL_TEMPLATE_BY_ZIP.format(CITYZIP=zip))
    w = weather_api.get_weather(URL_TEMPLATE_BY_ZIP.format(CITYZIP=zip))
    # set the variables that the form needs from the weather dictionary
    key = w['key']
    description = w['description']
    temp = w['temp']

    return render_template('city.html', city=city, key=key, description=description, temp=temp)


if __name__ == '__main__':
    app.run()