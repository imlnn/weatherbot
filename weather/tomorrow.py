from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from helpers import get_city_geocode, get_weather_for_tomorrow
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
        try:
            city_name = message.text
            gc = get_city_geocode(city_name)
            w = get_weather_for_tomorrow(city_name, gc)
            await message.answer(w.to_string())
        except:
            await message.answer("City not found")
