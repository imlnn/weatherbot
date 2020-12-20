from datetime import datetime, timedelta

from pyowm import OWM

import weather_obj

OWM_OBJ = OWM("a6b276fe520849040672b888ec1f1cb6")


def get_current_weather(city_name):
    w = OWM_OBJ.weather_manager().weather_at_place(city_name).weather
    return weather_obj.Weather(get_date_string()
                               , city_name
                               , w.temp['temp']
                               , w.status
                               , w.humidity
                               , w.wind().get("speed"))


def get_city_geocode(city_name):
    weather = OWM_OBJ.weather_manager().weather_at_place(city_name).weather
    return {'lat': weather.location.lat, 'lon': weather.location.lon}


def get_weekly_weather(city_name, geocode):
    forecast = OWM_OBJ.weather_manager().one_call(lat=geocode['lat'], lon=geocode['lon'], exclude='hourly',
                                                  units='metric').forecast_daily
    weather_array = []
    lamb = 0
    for f in forecast:
        weather_array.append(weather_obj.Weather(get_date_string(lamb)
                                                 , city_name
                                                 , f.temp.get('day')
                                                 , f.status
                                                 , f.humidity
                                                 , f.wind().get("speed")))
        lamb += 1


def get_weather_for_tomorrow(city_name, geocode):
    forecast = OWM_OBJ.weather_manager().one_call(lat=geocode['lat'], lon=geocode['lon'], exclude='hourly',
                                                  units='metric').forecast_daily
    return weather_obj.Weather(get_date_string()
                               , city_name
                               , forecast[1].temp.get('day')
                               , forecast[1].status
                               , forecast[1].humidity
                               , forecast[1].wind().get("speed"))


def get_date_string(lamb=0):
    date = (datetime.now() + timedelta(days=lamb)).date()
    return str(date.day) + "." + str(date.month) + "." + str(date.year)
