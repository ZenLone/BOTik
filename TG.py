import asyncio
import threading
from Vk import listen_vk_updates
from aiogram import Dispatcher
import asyncio
import logging
import multiprocessing

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import BotCommand
TOKEN = ("7670393303:AAESGfFillmbUdCrukSlUd2eEKO2xydryjE")
if not TOKEN:
    raise ValueError("BOT_TOKEN is not set in environment variables.")
dp = Dispatcher()
chatId = 210531192
last_message = None

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Начать работу"),
        BotCommand(command="/rasp", description="Посмотреть расписание"),
    ]
    await bot.set_my_commands(commands)

@dp.message(Command("start"))
async def command_start_handler(message):
    await message.answer("Привет! Используйте меню команд для взаимодействия.")

def create_rasp_handler(queue):
    async def command_rasp_handler(message: types.Message):
        global last_message
        logging.info("Обработка команды /rasp")
        if not queue.empty():
            msg = queue.get()
            last_message = msg
            await message.answer(f"Расписание:\n{msg}")
        elif last_message is not None:
            await message.answer(f"Расписание:\n{last_message}")
        else:
            await message.answer("Сообщение ещё не получено.")
    return command_rasp_handler

async def main():
    queue = multiprocessing.Queue()

    process = multiprocessing.Process(target=listen_vk_updates, args=(queue,))
    process.start()

    bot = Bot(token=TOKEN)
    await set_commands(bot)

    dp.message.register(create_rasp_handler(queue), Command("rasp"))

    await dp.start_polling(bot)
    
    process.join()

    # vk_thread = threading.Thread(target=listen_vk_updates)
    # vk_thread = threading.Thread(target=lambda: asyncio.run(listen_vk_updates()))
    # vk_thread.start()

    await dp.start_polling(bot)

# Точка входа в программу

if __name__ == "__main__":
    asyncio.run(main())