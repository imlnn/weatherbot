from pyowm import OWM

from misc import dp

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from weather import keyboards


class NowStates(StatesGroup):
    start = State()


@dp.message_handler(text_contains=['Now'])
async def get_city(message):
    await message.answer("Send your City name, choose City from defaults or tap Back to return to main menu"
                         , reply_markup=keyboards.default_cities())
    await NowStates.start.set()


@dp.message_handler(state=NowStates.start)
async def get_forecast(message, state: FSMContext):
    if message.text == "Back":
        await message.answer("Ok", reply_markup=keyboards.start_keyboard())
        await state.finish()
        return

    try:
        owm = OWM("a6b276fe520849040672b888ec1f1cb6")

        w = owm.weather_manager().weather_at_place(message.text).weather

        await message.answer("Place: " + message.text
                                 + "\nTemperature: " + str("%.2f" % (w.temp['temp'] - 273.15))
                                 + "\n" + str(w.status)
                                 + "\nHumidity: " + str(w.humidity)
                                 + "\nWind speed: " + str(w.wind().get("speed")))

    except:
        await message.answer("City not found")
