import asyncio
import logging
import sys
import aiogram
import os

import json
from misc import dp, form_router, bot
import commands

async def main(bot, dp) -> None:
    delete_all_files_in_folder('utils/video/')

    await bot(aiogram.methods.DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)



def delete_all_files_in_folder(folder_path):
    if not os.path.exists(folder_path):
        return
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Не удалось удалить файл '{file_path}'. Причина: {e}")

if __name__ == "__main__":
    
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main(bot=bot, dp=dp))
    
