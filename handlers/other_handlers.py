from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
from keyboards import yes_no_keyboard


router: Router = Router()


@router.message()
async def other_answers_process(message: Message):
    await message.answer(text=LEXICON_RU['other_answers'],
                         reply_markup=yes_no_keyboard)
