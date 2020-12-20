from pyowm import OWM
from pyowm.utils import timestamps

from misc import dp

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from weather import keyboards


class TomorrowStates(StatesGroup):
    start = State()


@dp.message_handler(text_contains=['Tomorrow'])
async def get_city(message):
    await message.answer("Send your City name, choose City from defaults or tap Back to return to main menu"
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
        #w = owm.weather_manager().weather_at_place(message.text).get_weather_at(timestamps.tomorrow())

        mgr = owm.weather_manager()
        daily_forecaster = mgr.forecast_at_place('Berlin,DE', 'daily')
        tomorrow = timestamps.tomorrow()  # datetime object for tomorrow
        w = daily_forecaster.get_weather_at(tomorrow)

        await message.answer("Weather for tomorrow"
                             + "\nPlace: " + message.text
                             + "\nTemperature: " + str(w.temperature('celsius').get("temp"))
                             + "\n" + str(w.detailed_status)
                             + "\nHumidity: " + str(w.humidity)
                             + "\nWind speed: " + str(w.wind().get("speed")))

