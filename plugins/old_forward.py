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
        FROM = int(FROM)
        try:
            is_member = await bot.get_chat_member(FROM, "me")
            if is_member.status == enums.ChatMemberStatus.ADMINISTRATOR:
                get_from_chat = await bot.get_chat(FROM)
                from_chat_id = get_from_chat.id
                str_fro_chat = str(from_chat_id)
                from_chat_name = get_from_chat.title
              # if str_fro_chat.startswith("-100")      
                rm_from_chat = str_fro_chat.replace("-100", "")  # remove "-100" from chat id
                start_msg_link = f"https://t.me/c/{rm_from_chat}/{start_id}"
                end_msg_link = f"https://t.me/c/{rm_from_chat}/{stop_id}"
            else:
                await message.reply_text("Add me as an admin in Source Chat", quote=True)
        except Exception as e:
            logger.exception(e)
            await message.reply_text('Some error occurred!.', quote=True)
            return               
    else:
        from_chat_id = FROM
        if not from_chat_id.startswith("@"):
            from_chat_id = "@" + from_chat_id
        from_chat_name = from_chat_id
        if from_chat_id.startswith("@"):     
            rm_from_chat_usrnm = from_chat_name[len("@"):]
            start_msg_link = f"https://t.me/{rm_from_chat_usrnm}/{start_id}"
            end_msg_link = f"https://t.me/{rm_from_chat_usrnm}/{stop_id}"

    try:
        to_chat = await bot.get_chat(TO)
    except Exception as e:
        print(e)
        return await message.reply("Make Me Admin In Your Target Channel")                                       
    to_chat_id = to_chat.id
    forward_msg = await bot.send_message(
        text=f""" Forwarding Started! ✅
        
<b>From Chat:</b> {from_chat_name}
<b>To Chat:</b> {to_chat.title}
<b>start msg ID:</b> <a href='{start_msg_link}'>{start_id}</a>
<b>end msg ID:</b> <a href='{end_msg_link}'>{stop_id}</a>
        """,
        chat_id=message.chat.id,
        disable_web_page_preview=True,
        parse_mode=enums.ParseMode.HTML
    )
    
    user_id = str(message.from_user.id)
    get_forward_type = user_file_types.get(user_id)
    try:
        forward_type = get_forward_type.get("file_type")
    except:
        forward_type = "videos"
        pass        
    if forward_type:          
        forward_type = forward_type.lower()
        if forward_type == "document":
            file_types = enums.MessagesFilter.DOCUMENT
        elif forward_type == "videos":
            file_types = enums.MessagesFilter.VIDEO
    else:
        await message.reply_text("First Set Forward type which type media U want to forward")
        return
        
    files_count = 0
    is_forwarding = True
    forward_status = await bot.send_message(
        text=f"Total Forwarded: {files_count}",
        chat_id=message.chat.id
    )
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
            if message.caption:
                m_caption = f"**{message.caption}**"
            else:
                m_caption = file_name
            await bot.copy_message(
                chat_id=to_chat_id,
                from_chat_id=from_chat_id,
                parse_mode=enums.ParseMode.MARKDOWN,       
                caption=m_caption,
                message_id=message.id
            )
            files_count += 1
            await asyncio.sleep(delay_time)
            await forward_status.edit(text=f"Total Forwarded: {files_count}")
        except FloodWait as e:
            await asyncio.sleep(e.value) 
        except Exception as e:
            print(e)
            pass

    is_forwarding = False
    
    await forward_msg.edit(
        text=f"<u><i>Successfully Forwarded:</i></u> {files_count} {forward_type}",        
    )


@Client.on_message(filters.private & filters.command(["stop"]))
async def stop_forward(bot, message):
    global is_forwarding
    if message.from_user.id not in AUTH_USERS:
        return

    if not is_forwarding:
        await message.reply_text("No forwarding process is currently active.")
        return

    is_forwarding = False
    await message.reply_text("Forwarding process stopped successfully.")
