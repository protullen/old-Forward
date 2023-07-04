# Lx 0980
# Year : 2023

import asyncio, sys, os
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from info import AUTH_USERS 

import logging

logger = logging.getLogger(__name__)

DOCUMENT = enums.MessagesFilter.DOCUMENT 
VIDEOS = enums.MessagesFilter.VIDEO

is_forwarding = False

@Client.on_message(filters.private & filters.command(["clone"]))
async def run(bot, message):
    global is_forwarding
    if str(message.from_user.id) not in str(AUTH_USERS):
        return

    # Get start and stop message IDs from command
    message_text = message.text.split()
    if len(message_text) < 5:
        await message.reply_text("Please provide From Channel ID, To Channel ID, start and stop message IDs, and delay time in seconds.")
        return
    FROM = int(message_text[1])
    TO = int(message_text[2])
    start_id = int(message_text[3])
    stop_id = int(message_text[4])
    delay_time = int(message_text[5])

    m = await bot.send_message(
        text="<i>File Forwarding Started😉</i>",        
        chat_id=message.chat.id
    )

    files_count = 0
    is_forwarding = True
    async for message in bot.USER.search_messages(chat_id=FROM, filter=VIDEOS):
        try:
            if not is_forwarding:
                break
            if message.id < start_id or message.id > stop_id:
                continue
            if message.video:
                file_name = message.video.file_name
            elif message.document:
                file_name = message.document.file_name
            elif message.audio:
                file_name = message.audio.file_name 
            else:
                file_name = None
            try:
                await bot.copy_message(
                    chat_id=TO,
                    from_chat_id=FROM,
                    parse_mode=enums.ParseMode.MARKDOWN,
                    caption=f"**{message.caption}**",
                    message_id=message.id
                )
            except Exception:
                await bot.USER.copy_message(
                    chat_id=TO,
                    from_chat_id=FROM,
                    parse_mode=enums.ParseMode.MARKDOWN,
                    caption=f"**{message.caption}**",
                    message_id=message.id
                )
            files_count += 1
            await asyncio.sleep(delay_time)
        except FloodWait as e:
            await asyncio.sleep(e.value) 
        except Exception as e:
            print(e)
            pass

    is_forwarding = False
    
    await m.edit(
        text=f"<u><i>Successfully Forwarded</i></u>\n\n<b>Total Forwarded Files:-</b> <code>{files_count}</code> <b>Files</b>\n<b>Thanks For Using Me❤️</b>",        
    )

 
@Client.on_message(filters.private & filters.command(["stop"]))
async def stop_forwarding(bot, message):
    global is_forwarding
    if str(message.from_user.id) not in Config.OWNER_ID:
        return
    
    if is_forwarding:
        is_forwarding = False
        await message.reply_text("File forwarding process stopped.")
    else:
        await message.reply_text("File forwarding process is not running.")





