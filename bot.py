import asyncio
import logging
from config_data.config import Config, get_config_data
from handlers import other_handlers, user_handlers
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand


# Инициализируем логгер
logger = logging.getLogger(__name__)


async def main():
    # Конфигурируем логгирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s - %(name)s - %(message)s'
    )

    # Выводим в консоль инфу о начале запуска бота
    logger.info('Starting bot')

    config: Config = get_config_data(None)
    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    main_menu_commands = [
        BotCommand(command='/start',
                   description='Запустить бота'),
        BotCommand(command='/help',
                   description='Справка')
    ]

    await bot.set_my_commands(main_menu_commands)

    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
