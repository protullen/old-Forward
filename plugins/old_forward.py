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
    FROM = message_text[1]
    TO = int(message_text[2])
    start_id = int(message_text[3])
    stop_id = int(message_text[4])
    delay_time = int(message_text[5])

    if "-100" in FROM:
        try:
            get_from_chat = await bot.get_chat(int(FROM))
            from_chat_id = get_from_chat.id
            from_chat_name = get_from_chat.title
            if not from_chat_id:
                await message.reply("Make Me Admin In Your Source Channel")
                return
        except:
            await message.reply("Invalid Source Channel ID")
            return

    if "-100" not in FROM:
        from_chat_id = FROM
        if not from_chat_id.startswith("@"):
            from_chat_id = "@" + from_chat_id
        from_chat_name = from_chat_id
        
    
    try:
        to_chat = await bot.get_chat(TO)
    except:
        return await message.reply("Make Me Admin In Your Target Channel")                                       
    to_chat_id = to_chat.id
    forward_msg = await bot.send_message(
        text=f""" Forwarding Started! ✅
<b>From Chat:</b> {from_chat_name}
<b>To Chat:</b> {to_chat.title}
        """,
        chat_id=message.chat.id
    )
    
    user_id = str(message.from_user.id)
    get_forward_type = user_file_types.get(user_id)
    forward_type = get_forward_type.get("file_type")
    if forward_type:
        forward_type = forward_type.lower()
        if forward_type == "document":
            file_types = enums.MessagesFilter.DOCUMENT
        elif forward_type == "videos":
            file_types = enums.MessagesFilter.VIDEO
    else:
        file_types = enums.MessagesFilter.VIDEO

    files_count = 0
    is_forwarding = True
    # forward_status = await message.reply_text(f"Total Forwarded: {files_count}")
    async for message in bot.USER.search_messages(chat_id=from_chat_id, filter=file_types):
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
                chat_id=to_chat_id,
                from_chat_id=from_chat_id,
                parse_mode=enums.ParseMode.MARKDOWN,       
                caption=f"**{message.caption}**",
                message_id=message.id
            )
            files_count += 1
            await asyncio.sleep(delay_time)
            await forward_status.edit(f"Total Forwarded: {files_count}")
        except FloodWait as e:
            await asyncio.sleep(e.value) 
        except Exception as e:
            print(e)
            pass

    is_forwarding = False
    
    await forward_msg.edit(
        text=f"<u><i>Successfully Forwarded</i></u>\n\n<b>Total Forwarded > Files</b>\n<b>Thanks For Using Me❤️</b>",        
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
    user_id = str(message.from_user.id)
    if int(user_id) not in AUTH_USERS:
        await message.reply_text("You are not authorized to use this command.")
        return
    message_text = message.text.split()
    if len(message_text) < 1:
        await message.reply_text("Please provide forward type: files or video")
        return
    if not message_text:
        return
    message_text = message_text[1]
    
        
    if "files" in message_text:
        file_type = "document"
    elif "videos" in message_text:
        file_type = "videos"    
   
    if not file_type:
        await message.reply_text("Error to set forward type")
        return     
    user_file_types[user_id] = {"file_type": file_type}
    await message.reply_text(f"Forward type set to: {file_type.capitalize()} ✅ ✅ ✅")

@Client.on_message(filters.private & filters.command(["check_file_type"]))
async def check_file_type(bot, message):
    if message.from_user.id not in AUTH_USERS:
        await message.reply_text("You are not authorized to use this command.")
        return
    
    user_id = str(message.from_user.id)
    forward_type = user_file_types.get(user_id)
    
    if forward_type:
        file_type = forward_type.get("file_type")
        if file_type:
            await message.reply_text(f"Current file type: {file_type.capitalize()}")
        else:
            await message.reply_text("File type is not set.")
    else:
        await message.reply_text("File type is not set.")

@Client.on_message(filters.private & filters.command(["delete_file_type"]))
async def delete_file_type(bot, message):
    if message.from_user.id not in AUTH_USERS:
        return await message.reply_text("You are not authorized to use this command.")
    
    user_id = str(message.from_user.id)
    forward_type = user_file_types.get(user_id)
    
    if forward_type:
        file_type = forward_type.get("file_type")
        if file_type:
            del user_file_types[user_id]
            await message.reply_text(f"File type '{file_type.capitalize()}' deleted.")
        else:
            await message.reply_text("File type is not set.")
    else:
        await message.reply_text("File type is not set.")




