from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from helpers import get_city_geocode, get_weekly_weather
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

    try:
        city_name = message.text
        gc = get_city_geocode(city_name)
        weather = get_weekly_weather(city_name, gc)

        for w in weather:
            await message.answer(w.to_string())
    except:
        await message.answer("City not found")
