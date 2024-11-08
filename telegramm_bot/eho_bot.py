import os
import dotenv

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
dotenv.load_dotenv()


# Создаем объекты бота и диспетчера
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')
    
    
# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )
    
    
# Этот хэндлер будет срабатывать на отправку боту фото
#@dp.message(F.photo)
#async def send_photo_echo(message: Message):
#    print(message)
#    await message.reply_photo(message.photo[0].file_id)
    
    
# Этот хэндлер будет срабатывать на отправку боту стикера
#@dp.message(F.sticker)
#async def send_sticker_echo(message: Message):
#    print(message)
#    await message.reply_sticker(message.sticker.file_id)


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(
            text='Данный тип апдейтов не поддерживается '
                 'методом send_copy'
        )
    

#dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)


if __name__ == '__main__':
    dp.run_polling(bot)
