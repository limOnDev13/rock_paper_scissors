import random


def random_bot_choice() -> str:
    return random.choice(['rock', 'scissors', 'paper'])


def _normalized_user_answer(user_answer: str) -> str:
    translating: dict = {
        'Камень': 'rock',
        'Ножницы': 'scissors',
        'Бумага': 'paper'
    }
    for key in translating:
        if key == user_answer:
            return translating[key]


def define_winner(user_choice: str, bot_choice: str) -> str:
    rules: dict[str, str] = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    en_user_choice: str = _normalized_user_answer(user_choice)
    if rules[en_user_choice] == bot_choice:
        return 'user'
    elif en_user_choice == bot_choice:
        return 'nobody'
    else:
        return 'bot'

