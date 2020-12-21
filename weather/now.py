from helpers import get_current_weather
from misc import dp

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from weather import keyboards


class NowStates(StatesGroup):
    start = State()


@dp.message_handler(text_contains=['Now'])
async def get_city(message):
    await message.answer("Send your City name, choose City from defaults or tap Back to return to main menu",
                         reply_markup=keyboards.default_cities())
    await NowStates.start.set()


@dp.message_handler(state=NowStates.start)
async def get_forecast(message, state: FSMContext):
    if message.text == "Back" or message.text == "/Back":
        await message.answer("Ok", reply_markup=keyboards.start_keyboard())
        await state.finish()
        return
    elif message.text.lower() == "nightcity":
        await message.answer_photo(photo="https://i.ytimg.com/vi/itQcAKnKnxY/maxresdefault.jpg", caption="Go back to "
                                                                                                         "sleep, "
                                                                                                         "Samurai",
                                   reply_markup=keyboards.start_keyboard())
        await state.finish()
        return

    try:
        city_name = message.text.lstrip("/")
        w = get_current_weather(city_name)
        await message.answer(w.to_string())
    except:
        await message.answer("City not found")
