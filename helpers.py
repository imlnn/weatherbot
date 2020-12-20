from pyowm import OWM

ABS_ZERO = 273.1
OWM_OBJ = OWM("a6b276fe520849040672b888ec1f1cb6")


def get_current_weather(city_name):
    return OWM_OBJ.weather_manager().weather_at_place(city_name).weather


def get_city_geocode(city_name):
    weather = OWM_OBJ.weather_manager().weather_at_place(city_name).weather
    return {'lat': weather.location.lat, 'lon': weather.location.lon}


def create_weather_desc(city_name, w):
    return ("In " + city_name + ":"
            + "\nTemperature is " + str("%.2f" % (w.temp['temp'] - 273.15)) + "C"
            + "\n" + str(w.status)
            + "\nHumidity: " + str(w.humidity)
            + "\nWind speed: " + str(w.wind().get("speed")))
