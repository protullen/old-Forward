# (c) Lx 0980
# Github : https://github.com/protullen/old-Forward

import logging
logger = logging.getLogger(__name__)

from info import AUTH_USERS
from pyrogram import Client, filters
from .old_forward import is_forwarding, user_file_types

@Client.on_message(filters.command("start") & filters.private & filters.incoming)
async def start(client, message):
    if message.from_user.id not in AUTH_USERS:
        return await message.reply("This bot is not for public use")
    await message.reply(
        text=f"""Hello {message.from_user.mention}
<i>I can Forward existing media from Onc Channel To Another Channel,
You can also clone media from public channels without admin permission
More details use /userbot_help</i>
        """,
        disable_web_page_preview=True,
        quote=True
    )

@Client.on_message(filters.command("userbot_help") & filters.private & filters.incoming)
async def help(client, message):
    await message.reply(
        text="""<b>Follow These Steps!!</b>
<b>• use /clone command given format 
<b>• give admin permission in your personal telegram channel</b>
<b>• Then send any message In your personal telegram channel</b>

<b><u>Available Commands</b></u>

* /start - <b>Bot Alive</b>
* /set_forward_type <b> set which type media You want to forward</b> 
  <b>Available type:</b> '<code>videos</code>' or '<code>files</code>' default is <b>videos</b>
* /userbot_help - <b>for this message help</b>
* /clone - <b>start forward</b>
       format = <code>/clone from_id to_id start_id end_id delay_second</code> <b> separate with space</b> example: <code>/clone -10077775444 -10073774747 34 3747 23</code>


<b>Lx 0980</b>        
        """,
        disable_web_page_preview=True,
        quote=True
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


@Client.on_message(filters.private & filters.command(["set_forward_type"]))
async def set_file_type(bot, message):
    user_id = str(message.from_user.id)
    if int(user_id) not in AUTH_USERS:
        await message.reply_text("You are not authorized to use this command.")
        return
    message_text = message.text.split()
    if len(message_text) < 1:
        await message.reply_text("Please provide forward type: <code>files</code> or <code>videos</code>")
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

