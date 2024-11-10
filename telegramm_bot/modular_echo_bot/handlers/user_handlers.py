from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from lexicon.lexicon import LEXICON_RU


# Инициализируем роутер уровеня модуля
router = Router() 


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])
