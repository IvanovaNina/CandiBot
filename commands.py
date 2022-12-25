from config import dp, bot
from aiogram import types

from random import randint as rnd

take_candy = 0
count_of_candy = 150
started = False


@dp.message_handler(commands='start')
async def start_bot(message: types.Message):
    print(message.text)
    print(message)
    await message.answer('Привет! Если хочешь поиграть, напиши /game')


@dp.message_handler(commands=['game'])
async def welcome_game(message: types.Message):
    global count_of_candy
    global take_candy
    count_of_candy = 150
    take_candy = 0
    await message.answer(f'Правила игры: на столе лежит 150 конфет. \n'
                         f' Мы делаем ход по очереди. Первый ход определяется жеребьёвкой. \n'
                         f' За один ход можно взять не более 28 конфет. \n'
                         f' Выиграет тот, кто забирает конфеты последним. \n'
                         f' Начинаем жеребьёвку? \n'
                         f' /Yes /No ')


@dp.message_handler(commands=['No'])
async def no_answer(message: types.Message):
    await message.answer('Если хочешь поиграть, напиши /game')


@dp.message_handler(commands=['Yes'])
async def lottery(message: types.Message):
    global count_of_candy
    global take_candy
    global started
    random_number = rnd(1, 2)
    started = True
    if random_number != 1:
        await message.answer('Прошла жеребьёвка я начинаю.')
        await bot_turn(message)
    else:
        await message.answer('Прошла жеребьёвка ты начинаешь.')
        await message.answer(f'Твой ход! Сейчас на столе {count_of_candy} конфет. Сколько возьмёшь?')


@dp.message_handler()
async def player_turn(message: types.Message):
    global count_of_candy
    global take_candy
    global started
    if started:
        take_candy = input_number(message.text)
        if take_candy < 1 or take_candy > 28 or take_candy > count_of_candy:
            await message.answer('Не жульничай! Возьми разрешенное количество конфет.')
        else:
            count_of_candy -= take_candy
            await message.reply(f'Ты взял {take_candy} конфет. На столе осталось {count_of_candy} конфет. ')
            if count_of_candy <= 0:
                started = False
                await message.answer('Ты выиграл! Если хочешь поиграть, напиши /game')
            else:
                await bot_turn(message)


def input_number(number_text):
    try:
        return int(number_text)
    except ValueError:
        return 0


async def bot_turn(message: types.Message):
    global count_of_candy
    global take_candy
    global started
    if count_of_candy % 29 != 0:
        take_candy = count_of_candy % 29
    else:
        take_candy = rnd(1, 28)
    count_of_candy -= take_candy
    await message.answer(f'Я взял {take_candy} конфет. На столе осталось {count_of_candy} конфет. ')
    if count_of_candy <= 0:
        started = False
        await message.answer('Я выиграл! Если ещё хочешь поиграть, напиши /game')

    else:
        await message.answer(f'Твой ход! Сейчас на столе {count_of_candy} конфет. Сколько возьмёшь?')
