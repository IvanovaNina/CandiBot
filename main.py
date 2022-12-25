from aiogram.utils import executor
from config import dp
import handlers


async def bot_start(_):
    print('Бот запущен.')


handlers.redistred_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=bot_start)
