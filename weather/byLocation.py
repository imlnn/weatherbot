import pyowm as owm
from aiogram.dispatcher.filters import state
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import types
from misc import dp
from weather import keyboards


class ByLocationStates(StatesGroup):
    start = State()


@dp.message_handler(commands=['ByCurrentLocation'])
async def get_format_of_forecast(message):
    await message.answer("Send ur location")
    await ByLocationStates.start.set()

@dp.message_handler(state=ByLocationStates.start)
async def get_format_of_forecast(message):
    owm.owm.OWM.weather_manager().forecast_at_coords(message.chat_location.Location.longitude, message.chat_location.Location.latitude)
    await state.finish()
