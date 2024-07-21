from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandObject, Command, CommandStart
from misc import dp, bot
from aiogram import F, types

@dp.message(CommandStart())
async def start(message: Message, state: FSMContext) -> None:
    await message.answer(text='Чтобы скачать видео, тебе нужно отправить ссылку на видео в этот чат.\n\nБот был создан @roozzz1m\nTelegram канал - https://t.me/roozzz1m_tt')
