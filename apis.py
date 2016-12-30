import requests
import json 
import sys

def fetch_weather(city):
    pp = pprint.PrettyPrinter(indent=4)

    #get your key from http://api.openweathermap.org/
    API_KEY = "key"


    CITY_NAME = city



    try:
        f = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' \
                        + CITY_NAME + '&units=metric' + '&APPID=' +  API_KEY)
        respond_raw = f.read()
    except:
            print 'Execption: URL is not correct!'
            raise



    weather_dict = json.loads(respond_raw)



    #pp.pprint(weather_dict)



    print('\n\n' + weather_dict['name']+" is "+ \
          weather_dict['weather'][0]['description'] + \
          ', temperature: ' + str(weather_dict['main']['temp']) + \
          ', humidity: ' + str(weather_dict['main']['humidity']) + '%.' )


def fetch_stocks(ticker):
    return "1 gazillon dollars" # TODO? 

# TODO: More integrations
