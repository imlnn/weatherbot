from pyowm import OWM
from helpers import get_current_weather, create_weather_desc
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
        city_name = message.text
        w = get_current_weather(city_name)
        await message.answer(create_weather_desc(city_name, w))
    except:
        await message.answer("City not found")
