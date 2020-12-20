from aiogram import types


def start_keyboard():
    start_buttons = types.ReplyKeyboardMarkup(row_width=1)
    btn1 = types.KeyboardButton("Now")
    btn2 = types.KeyboardButton("Tomorrow")
    btn3 = types.KeyboardButton("Weekly")

    return start_buttons.add(btn1, btn2, btn3)


def default_cities():
    dcs = types.ReplyKeyboardMarkup(row_width=3)
    btn1 = types.KeyboardButton("Moscow")
    btn2 = types.KeyboardButton("Saint Petersburg")
    btn3 = types.KeyboardButton("Nizhnevartovsk")
    btn4 = types.KeyboardButton("Back")

    return dcs.add(btn1, btn2, btn3, btn4)
