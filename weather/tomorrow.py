from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from pyowm import OWM
from helpers import get_city_geocode

from misc import dp
from weather import keyboards


class TomorrowStates(StatesGroup):
    start = State()


@dp.message_handler(text_contains=['Tomorrow'])
async def get_city(message):
    await message.answer("Send your City name, choose city from defaults or tap Back to return to main menu"
                         , reply_markup=keyboards.default_cities())
    await TomorrowStates.start.set()


@dp.message_handler(state=TomorrowStates.start)
async def get_forecast(message, state: FSMContext):
    if message.text == "Back":
        await message.answer("Ok", reply_markup=keyboards.start_keyboard())
        await state.finish()
        return

    else:
        owm = OWM("a6b276fe520849040672b888ec1f1cb6")
        try:
            gc = get_city_geocode(message.text)
            forecast = owm.weather_manager().one_call(lat=gc['lat'], lon=gc['lon'], exclude='hourly',
                                                      units='metric').forecast_daily
            w = forecast[1]
            await message.answer("Weather for tomorrow"
                                 + "\nPlace: " + message.text
                                 + "\nTemperature: " + str("%.2f" % w.temp.get('day'))
                                 + "\n" + str(w.status)
                                 + "\nHumidity: " + str(w.humidity)
                                 + "\nWind speed: " + str(w.wind().get("speed")))
        except:
            await message.answer("City not found")
