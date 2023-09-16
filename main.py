import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from utils import (
    set_default_commands,
)


# Bot token can be obtained via https://t.me/BotFather
# TOKEN = getenv("BOT_TOKEN")
TOKEN = "6166859922:AAHTelA_UwYNMc9-BCL8vcwWf4cMViu4IKc"
TOKEN2 = "5732706081:AAHPzs12Iomtn4hgOIjEjxZPQVUqv4h8QCA"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    bot2 = Bot(TOKEN2, parse_mode=ParseMode.HTML)
    await set_default_commands(bot, bot2)
    # And the run events dispatching
    await dp.start_polling(bot, bot2)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
