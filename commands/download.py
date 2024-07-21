from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile, InputMediaVideo
from misc import dp, bot
from aiogram import F, types
import requests
from utils import Download

@dp.message()
async def get_url(message: Message, state: FSMContext) -> None:
    url = message.text
    
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return await message.answer('Некорректная ссылка')
    except:
        return await message.answer('Неверный формат ссылки.')
    
    start = await message.answer(text='Начинаю загрузку видео.')
    try:
        filename = Download(url=url).download_youtube_video()

        video = FSInputFile(path=f'utils/video/{filename}', filename=filename)
        
        await start.delete()
        await message.answer_document(document=video, caption="Видео было скачено из @yt_roozzz1m_bot")
    except:
        await start.delete()
        await message.answer(text='Произошла неизвестная ошибка. Попробуйте ещё раз или подождите немного.')
