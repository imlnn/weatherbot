from helpers import *
from weather_obj import Weather


def test_check_get_data():
    today = datetime.now().strftime("%d.%m.%Y")
    w = get_date_string(0)
    assert w == today


def test_check_get_geocode():
    coords = get_city_geocode("Moscow")
    assert coords['lat'] == 55.75 and coords['lon'] == 37.62


def test_get_current_weather():
    weather = get_current_weather("London")
    assert weather != {}
    assert "London" in weather.to_string()
    assert "Temperature" in weather.to_string()
    assert "Humidity" in weather.to_string()


def test_get_tomorrow_weather():
    city_name = "Moscow"
    coords = get_city_geocode(city_name)
    weather = get_weather_for_tomorrow(city_name, coords)
    assert weather != {}
    assert city_name in weather.to_string()
    assert "Temperature" in weather.to_string()
    assert "Humidity" in weather.to_string()


def test_get_weekly_weather():
    city_name = "Moscow"
    coords = get_city_geocode(city_name)
    weather = get_weekly_weather(city_name, coords)
    assert len(weather) == 8
    for w in weather:
        assert city_name in w.to_string()
        assert "Temperature" in w.to_string()
        assert "Humidity" in w.to_string()


def test_weather_class_methods():
    city_name = "Kiev"
    w = OWM_OBJ.weather_manager().weather_at_place(city_name).weather
    weather = Weather(get_date_string(0),
                      city_name,
                      w.temp['temp'],
                      w.status,
                      w.humidity,
                      w.wind().get("speed"))

    assert -100 < weather.temperature < 100
    assert weather.date == get_date_string(0)
    assert weather.place == city_name
    assert isinstance(weather.humidity, int)
    assert isinstance(weather.wind_speed, int)
