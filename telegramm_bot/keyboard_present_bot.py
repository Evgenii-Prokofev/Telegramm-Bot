from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from environs import Env


env = Env()
env.read_env()

bot = Bot(token=(env('BOT_TOKEN')))
dp = Dispatcher()

# Создаём объекты кнопок
button_1 = KeyboardButton(text='Собак 🦮')
button_2 = KeyboardButton(text='Огурцов 🥒')

# Создаём объект клавиатуры добавляя в него кнопки
keyboard = ReplyKeyboardMarkup(
    keyboard=[[button_1, button_2]],
    resize_keyboard=True,
    one_time_keyboard=True
    )

# Этот хэндлер будет срабатывать на команду /start
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Чего кошки бояться больше?',
        reply_markup=keyboard
    )


# Этот хэндлер будет срабатывать на ответ "Собак 🦮" и удалять клавиатуру
@dp.message(F.text == 'Собак 🦮')
async def process_dog_answer(message: Message):
    await message.answer(
        text='Да, несомненно, кошки боятся собак. '
             'Но вы видели как они боятся огурцов?',
    )


# Этот хэндлер будет срабатывать на ответ "Огурцов 🥒" и удалять клавиатуру
@dp.message(F.text == 'Огурцов 🥒')
async def process_cucumber_answer(message: Message):
    await message.answer(
         text='Да, иногда кажется, что огурцов '
             'кошки боятся больше',
    )


if __name__ == '__main__':
    dp.run_polling(bot)
