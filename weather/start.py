from misc import dp
from weather import keyboards


@dp.message_handler(commands=['start'])
async def send_welcome(message):
    await message.answer("Hello, " + message.from_user.first_name + "!")
    await message.answer("Pick ur option on the keyboard", reply_markup=keyboards.start_keyboard())


@dp.message_handler(commands=['info'])
async def send_info(message):
    await message.answer("You can check the weather in any location with this bot! Use keyboard or type in city name.")
