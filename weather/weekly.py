from datetime import datetime, timedelta

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from pyowm import OWM

from misc import dp
from weather import keyboards


class WeeklyStates(StatesGroup):
    start = State()


@dp.message_handler(text_contains=['Weekly'])
async def get_city(message):
    await message.answer("Send your City name, choose City from defaults or tap Back to return to main menu"
                         , reply_markup=keyboards.default_cities())
    await WeeklyStates.start.set()


@dp.message_handler(state=WeeklyStates.start)
async def get_forecast(message, state: FSMContext):
    if message.text == "Back":
        await message.answer("Ok", reply_markup=keyboards.start_keyboard())
        await state.finish()
        return

    else:
        owm = OWM("a6b276fe520849040672b888ec1f1cb6")
        mgr = owm.weather_manager()
        try:
            cw = owm.weather_manager().weather_at_place(message.text)

            forecast = mgr.one_call(lat=cw.location.lat, lon=cw.location.lon, exclude='hourly', units='metric').forecast_daily

            i = 0

            for w in forecast:
                i += 1
                date = (datetime.now() + timedelta(days=i)).date()
                await message.answer("Weather for " + str(date.day) + "." + str(date.month) + "." + str(date.year)
                                     + "\nPlace: " + message.text
                                     + "\nTemperature: " + str("%.2f" % (w.temperature('celsius').get('day')))
                                     + "\n" + str(w.status)
                                     + "\nHumidity: " + str(w.humidity)
                                     + "\nWind speed: " + str(w.wind().get("speed")))
        except:
            message.answer("City not found")
