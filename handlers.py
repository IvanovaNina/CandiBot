from aiogram import types, Dispatcher
import commands


def redistred_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start_bot, commands=['start'])
    dp.register_message_handler(commands.welcome_game, commands=['game'])
    dp.register_message_handler(commands.lottery, commands=['Yes'])
    dp.register_message_handler(commands.no_answer, commands=['No'])
