import requests
import json 
import sys

def fetch_weather(city):
    	
	pp = pprint.PrettyPrinter(indent=4)
	API_KEY = "9294d3ed0680074c429b6f1e653d8800"     #get the key from openweeathermap.org
	CITY_NAME = city
	try:
	    f = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' \
		            + CITY_NAME + '&units=metric' + '&APPID=' +  API_KEY)
	    respond_raw = f.read()
	except:
    except Exception as e:
        print(e)
        sys.stderr.write("Couldn't load current conditions\n")
        return "Unknown"
	weather_dict = json.loads(respond_raw)
	pp.pprint(weather_dict)
	#", Lat "+str(weather_dict['coord']['lat']) + " Lon "+str(weather_dict['coord']['lon'])+
	line=('\n\n' +" \n, , "+ weather_dict['weather'][0]['description'] +',minimum temperature: ' + str(weather_dict['main']['temp_min'])+',maximum temperature: ' + str(weather_dict['main']['temp_max'])+', humidity: ' + str(weather_dict['main']['humidity']) + '%.' )
	print (line)
    return 


def fetch_stocks(ticker):
    return "1 gazillon dollars" # TODO? 

# TODO: More integrations
