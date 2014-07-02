import sys, requests, json

weather_uri = "http://api.openweathermap.org/data/2.5/weather?q="

args 	= sys.argv
largs 	= len(args)
if largs < 2:
	print "You have to provide a city's name to check the weather"
	sys.exit(1)

city = args[1]
print "Getting weather in", city

request_uri = weather_uri + city.capitalize()
#print request_uri
requesty = requests.get(request_uri)

open_weather_json = json.loads(requesty.text)

print "=============================================================="
print "City:", open_weather_json['name']
print "Country:", open_weather_json['sys']['country']
print "Coords:", open_weather_json['coord']['lat'], " / ",open_weather_json['coord']['lon']
print ""
print "Weather:"
print "  Now:", open_weather_json['main']['temp'] - 273.15, "Celcius", " - ", 1.8 * (open_weather_json['main']['temp'] - 273) + 32, "F"
print "  High:", open_weather_json['main']['temp_max'] - 273.15, "Celcius", " - ", 1.8 * (open_weather_json['main']['temp'] - 273) + 32, "F"
print "  Low:", open_weather_json['main']['temp_min'] - 273.15, "Celcius", " - ", 1.8 * (open_weather_json['main']['temp'] - 273) + 32, "F"
print "  Humidity:", open_weather_json['main']['humidity'], "%"
print " ",open_weather_json['weather'][0]['description'], " ....."
print "=============================================================="
sys.exit(1)

