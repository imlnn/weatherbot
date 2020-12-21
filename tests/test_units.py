from helpers import *


def test_check_data():
    w = get_date_string(1)
    assert w != {}


def test_check_get_geocode():
    w = get_city_geocode("Moscow")
    assert w != {}
    assert w['lat'] == 55.75 and w['lon'] == 37.62
