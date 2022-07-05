from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin, other
from data_baze import sqlite_db

async def on_startup(_):
     print('Бот онлайн')
     sqlite_db.sql_start()

client.register_handles_client(dp)
admin.register_handlers_admin(dp)
other.register_handles_other(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)