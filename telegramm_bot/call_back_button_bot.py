from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton, 
                           Message, CallbackQuery)

from environs import Env


env = Env()  # Создаём экземпляр класса Env 
env.read_env()  # Методом read_env() читаем файл .env и загружаем из него переменные в окружение

# Создаем объекты бота и диспетчера
bot = Bot(token=env('BOT_TOKEN'))
dp = Dispatcher()

big_button_1 = InlineKeyboardButton(
    text='Большая кнопка 1',
    callback_data='big_button_1_pressed'
)

big_button_2 = InlineKeyboardButton(
    text='Большая кнопка 2',
    callback_data='big_button_2_pressed'
)

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_1],
                     [big_button_2]]
)


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру с инлайн-кнопками
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Это инлайн-кнопки. Нажми на любую!',
        reply_markup=keyboard
)


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_1_pressed'
@dp.callback_query(F.data == 'big_button_1_pressed')
async def process_button_1_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 1':
        await callback.message.edit_text(
            text='Была нажата БОЛЬШАЯ КНОПКА 1',
            reply_markup=callback.message.reply_markup
        )
    await callback.answer(text='Ура! Нажата кнопка 1')


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_2_pressed'
@dp.callback_query(F.data == 'big_button_2_pressed')
async def process_button_2_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 2':        
        await callback.message.edit_text(
            text='Была нажата БОЛЬШАЯ КНОПКА 2',
            reply_markup=callback.message.reply_markup
        )
    await callback.answer(
        text='Ура! Нажата кнопка2',
        show_alert=True
    )


if __name__ == '__main__':
    dp.run_polling(bot, allowed_updates=['message', 'callback_query'])
