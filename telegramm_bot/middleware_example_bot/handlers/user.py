import logging

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from filters.filters import MyFalseFilter, MyTrueFilter
from lexicon.lexicon import LEXICON_RU


logger = logging.getLogger(__name__)

user_router = Router()


@user_router.message(CommandStart(), MyTrueFilter())
async def process_start_command(message: Message):
    logger.debug('Вошли в хэндлер, обрабатывающий команду /start')
    # Создаём объект инлайн-кнопки
    button = InlineKeyboardButton(
        text='Кнопка',
        callback_data='button_pressed'
    )
    # Создаём объект инлайн-клавиатуры
    markup = InlineKeyboardMarkup(inline_keyboard=[[button]])
    # Отправляем сообщение пользователю
    await message.answer(text=LEXICON_RU['/start'], reply_markup=markup)
    logger.debug('Выходим из хэндлера, обрабатывающего комманду /start')
    
    
@user_router.callback_query(F.data, MyTrueFilter())
async def process_button_click(callback: CallbackQuery):
    logger.debug('Вошли в хэндлер, обрабатывающий нажатие на инлайн-кнопку')
    await callback.answer(text=LEXICON_RU['button_pressed'])
    logger.debug('Выходим из хэндлера, обрабатывающего нажатие на инлайн-кнопку')


# Это хэндлер, который мог бы обрабатывать любой текст,
# но `MyFalseFilter` его не пропустит
@user_router.message(F.text, MyFalseFilter())
async def process_text(message: Message):
    logger.debug('Вошли в хэндлер, обрабатывающий текст')
    logger.debug('Вышли из хэндлера, обрабатывающий текст')
