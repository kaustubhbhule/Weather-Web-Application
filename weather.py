from flask import Flask, render_template, request

# import json to load JSON data to a python dictionary
import json

# urllib.request to make a request to api
import urllib.request

# for time
from datetime import datetime

from urllib.error import HTTPError

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
        if city != "":

            # our API key
            api = '508452150c6f6217bad24dcdedc2998b'

            source = None
            try:
                # source contain json data from api
                source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api).read()
            except HTTPError:
                return render_template('index.html', data = { "success": 'False', })

            # converting JSON data to a dictionary
            list_of_data = json.loads(source)
  

            e = datetime.now()
            # data for variable list_of_data
            data = {
                "success": 'True',
                "city": city,
                "country_code": str(list_of_data['sys']['country']),
                "temp": str(int(float(list_of_data['main']['temp']) - 273.15)),
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
                "main": str(list_of_data['weather'][0]['main']),
                "wind_speed": str(float(list_of_data['wind']['speed'])),
                "time": str(e.strftime("%I:%M %p")),
            }
        else:
            # for empty value of city
            data = { "success": 'False', }
    else:
        # for empty value of city
        data = { "success": 'False', }
        
    print(data, '\n')
    return render_template('index.html', data = data)
  
if __name__ == '__main__':
    app.run(debug = True)