from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def send_other_message(message: Message):
    await message.answer(text='Это бот-книга {message.text}')
