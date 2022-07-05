from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

batton_load = KeyboardButton('/Загрузить')
batton_delete = KeyboardButton('/Удалить')

batton_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(batton_load).add(batton_delete)