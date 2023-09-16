from aiogram.types import BotCommand


async def set_default_commands(*bots):
    for bot in bots:
        await bot.set_my_commands(
            commands=[
                BotCommand(
                    command="start",
                    description="Почати новинний дайджест",
                ),
                BotCommand(
                    command="whattoread",
                    description="Обрати категорії новин",
                ),
                BotCommand(
                    command="randomtopic",
                    description="Мені повезе...",
                ),
            ],
        )
