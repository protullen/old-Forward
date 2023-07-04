# Lx 0980
# Year: 2023

import asyncio
import sys
import os
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from info import AUTH_USERS

import logging
logger = logging.getLogger(__name__)

user_file_types = {}
is_forwarding = False

@Client.on_message(filters.private & filters.command(["clone"]))
async def run(bot, message):
    global is_forwarding
    if message.from_user.id not in AUTH_USERS:
        return

    # Get start and stop message IDs from command
    message_text = message.text.split()
    if len(message_text) < 5:
        await message.reply_text("Please provide From Channel ID, To Channel ID, start and stop message IDs, and delay time in seconds.")
        return
    FROM = int(message_text[1])
    FROM = int(message_text[1])
    TO = int(message_text[2])
    start_id = int(message_text[3])
    stop_id = int(message_text[4])
    delay_time = int(message_text[5])

    try:
        from_chat = await bot.get_chat(FROM)
        to_chat = await bot.get_chat(TO)
    except Exception as e:
        from_chat = FROM
        to_chat = TO

    try:
        chat_name = from_chat.name
        if chat_name:
            forward_msg = await bot.send_message(
                text=ChatMSG.FORWARDING,
                chat_id=message.chat.id
            )
        else:
            forward_msg = await bot.send_message(
                text="<i>File Forwarding Started😉</i>",
                chat_id=message.chat.id
            )
    except Exception as e:
        print(e)
        await message.reply_text("Error starting file forwarding. Please try again later.")

            
        

    files_count = 0
    is_forwarding = True
    user_id = str(message.from_user.id)
    forward_type = user_file_types.get(user_id)
    if "document" in forward_type:
        file_types = enums.MessagesFilter.DOCUMENT
    elif "videos" in forward_type:
        file_types = enums.MessagesFilter.VIDEO
    else:
        file_types = enums.MessagesFilter.VIDEO

    forward_status await message.reply_text(f"Total Forwarded: {files_count}")
    async for message in bot.USER.search_messages(chat_id=FROM, filter=file_types):
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
            await bot.copy_message(
                chat_id=to_chat,
                from_chat_id=from_chat,
                parse_mode=enums.ParseMode.MARKDOWN,
                caption=f"**{message.caption}**",
                message_id=message.id
            )
            files_count += 1
            await asyncio.sleep(delay_time)
            await forward_status.edit(
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except Exception as e:
            print(e)
            pass

    is_forwarding = False

    await m.edit(
        text=f"<u><i>Successfully Forwarded</i></u>\n\n<b>Total Forwarded Files: {files_count}</b> Files\n<b>Thanks For Using Me ❤️</b>",
    )


@Client.on_message(filters.private & filters.command(["stop"]))
async def stop_forwarding(bot, message):
    global is_forwarding
    if message.from_user.id not in AUTH_USERS:
        return

    if is_forwarding:
        is_forwarding = False
        await message.reply_text("File forwarding process stopped.")
    else:
        await message.reply_text("File forwarding process is not running.")


@Client.on_message(filters.private & filters.command(["set_file_type"]))
async def set_file_type(bot, message):
    if message.from_user.id not in AUTH_USERS:
        return await message.reply_text("You are not authorized to use this command.")
    user_id = str(message.from_user.id)
    text = message.text.lower()
    if "files" in text or "file" in text:
        file_type = "document"
    elif "video" in text or "videos" in text:
        file_type = "videos"
    else:
        await message.reply_text("Invalid file type. Please specify either 'files' or 'videos'.")
        return
    user_file_types[user_id] = file_type
    forward_type = user_file_types.get(user_id)
    if not forward_type:
        return await message.reply_text("Error setting document forwarding type\n❌ ❌ ❌")
    await message.reply_text(f"Forward type set to: {forward_type.capitalize()} ✅ ✅ ✅")
