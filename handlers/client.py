from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from create_bot import bot, dp
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_baze import sqlite_db

#@dp.message_handler(commands=['start','help'])
async def command_start(message: types.Message):
     try:
          await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup= kb_client)
          await message.delete()
     except:
          await message.reply('Общение с ботом в ЛС, напишите ему:\n https://t.me/Pizza_ItallianoBot')

#@dp.message_handler(commands=['Режим_работы'])
async def pizza_open(message: types.Message):
     await bot.send_message(message.from_user.id, 'Пн-Пт c 11:00 до 22:00, Сб-Вс(праздничные дни) с 12:00 до 23:30')

#@dp.message_handler(commands=['Расположение'])
async def pizza_adress(message: types.Message):
     await bot.send_message(message.from_user.id, 'г. Казань, ул. Мира, д. 23')          

#@dp.message_handler(Text(equals='Меню', ignore_case=True))
async def pizza_menu_command(message: types.Message):
     await sqlite_db.sql_read(message)

def register_handles_client(dp: Dispatcher):
    dp.register_message_handler(command_start, Text(equals='start', ignore_case=True))
    dp.register_message_handler(pizza_open, Text(equals='Режим работы', ignore_case=True))
    dp.register_message_handler(pizza_adress, Text(equals='Расположение', ignore_case=True))
    dp.register_message_handler(pizza_menu_command, Text(equals='Меню', ignore_case=True))