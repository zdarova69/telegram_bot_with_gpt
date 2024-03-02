from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ContentType
import asyncio
from core.handlers.basic import *
from core.settings import settings
import numpy as np
import torch
from aiogram.filters import Command

np.random.seed(42)
torch.manual_seed(42)



async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, 'бот запущен')

async def stop_bot(bot: Bot): 
    await bot.send_message(settings.bots.admin_id, 'бот выключен')



async def start():
    bot = Bot(token=settings.bots.bot_token)
    
    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    # dp.message.register(get_started, commands={'/start'})
    dp.message.register(get_text)
    
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ =='__main__':
    asyncio.run(start())