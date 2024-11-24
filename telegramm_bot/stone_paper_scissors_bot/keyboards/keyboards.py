from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU


#-------Создаём клавиатуру через ReplyKeyboardBuilder------
button_yes = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])

yes_no_kb_builder = ReplyKeyboardBuilder()

yes_no_kb_builder.row(button_yes, button_no, width=2)

yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

#------Создаём игровую клавиатуру без использования билдера---
button_stone = KeyboardButton(text=LEXICON_RU['stone'])
button_paper = KeyboardButton(text=LEXICON_RU['paper'])
button_scissors = KeyboardButton(text=LEXICON_RU['scissors'])

# Создаем игровую клавиатуру с кнопками "Камень 🗿",
# "Ножницы ✂" и "Бумага 📜" как список списков
game_kb = ReplyKeyboardMarkup(
    keyboard=[[button_stone],
             [button_paper],
             [button_scissors]],
    resize_keyboard=True
)
