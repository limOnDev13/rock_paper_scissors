from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, Text
from lexicon import LEXICON_RU
from keyboards import yes_no_keyboard, game_keyboard
from services import random_bot_choice, define_winner


router: Router = Router()


@router.message(CommandStart())
async def start_command_process(message: Message):
    await message.answer(text=LEXICON_RU['start'],
                         reply_markup=yes_no_keyboard)


@router.message(Command(commands=['help']))
async def help_command_process(message: Message):
    await message.answer(text=LEXICON_RU['help'],
                         reply_markup=yes_no_keyboard)


@router.message(Text(['Хочу играть!']))
async def positive_answer_process(message: Message):
    await message.answer(text=LEXICON_RU['yes_answer'],
                         reply_markup=game_keyboard)


@router.message(Text(['Не хочу:(']))
async def negative_answer_process(message: Message):
    await message.answer(text=LEXICON_RU['no_answer'])


@router.message(Text(['Камень', 'Ножницы', 'Бумага']))
async def game_answers_process(message: Message):
    bot_choice: str = random_bot_choice()
    winner: str = define_winner(message.text, bot_choice)

    if winner == 'user':
        await message.answer(text=LEXICON_RU['user_wins'],
                             reply_markup=yes_no_keyboard)
    elif winner == 'bot':
        await message.answer(text=LEXICON_RU['bot_wins'],
                             reply_markup=yes_no_keyboard)
    else:
        await message.answer(text=LEXICON_RU['nobody_wins'],
                             reply_markup=yes_no_keyboard)
