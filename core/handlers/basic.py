from aiogram import Bot
from aiogram.types import Message
import asyncio
from core.gpt_model import generate, model,tok

async def get_started(message: Message, bot: Bot):
    await message.reply(f'Здаров')


async def get_text(message: Message):
    generated = generate(model, tok, message.text , num_beams=10)
    generated[0]
    await message.reply(generated[0])