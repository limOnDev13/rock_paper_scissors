from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton
from lexicon.lexicon_ru import LEXICON_RU


# --Клавиатура с положительным или отрицательным ответами--
keyboard_yes_no_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

yes_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
no_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['no_button'])

keyboard_yes_no_builder.row(*[yes_button, no_button], width=2)
yes_no_keyboard = keyboard_yes_no_builder.as_markup(one_time_keyboard=True,
                                                    resize_keyboard=True)


# --Клавиатура с вариантами ответа для игры в камень, ножницы, бумага
game_keyboard_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

rock_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
scissors_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])
paper_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])

game_keyboard_builder.row(*[rock_button, scissors_button, paper_button])
game_keyboard = game_keyboard_builder.as_markup(resize_keyboard=True)
