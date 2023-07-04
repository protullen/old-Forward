# (c)  Lx 0980

import logging
logger = logging.getLogger(__name__)

from info import AUTH_USERS 
from pyrogram import Client, filters

@Client.on_message(filters.command("start") & filters.private & filters.incoming)
async def start(client, message):
    if message.from.user.id not in AUTH_USERS:
        return await message.reply("This bot is not for public use")
    await message.reply(
        text=f"""Hello {message.from.user.mention}
<i>I'm Simple Auto file Forward User Bot
This Bot forward all old videos from One channel to Your Personal channel
More details <code>/userbot_help</code></i>
        """,
        disable_web_page_preview=True,
        quote=True

@Client.on_message(filters.command("userbot_help") & filters.private & filters.incoming)
async def help(client, message):
    await message.reply(
        text="""<b>Follow These Steps!!</b>
<b>• Currectly fill your Heroku Config vars</b> <code>FROM_CHANNEL</code> and <code>TO_CHANNEL</code> <b>and other Vars</b>
<b>• Then give admin permission in your personal telegram channel</b>
<b>• Then send any message In your personal telegram channel</b>
<b>• Then use /clone command in your bot</b>

<b><u>Available Command</b></u>

* /userbot_start - <b>Bot Alive</b>
* /userbot_help - <b>more help</b>
* /clone - <b>start forward</b>
       format = <code>/clone from_id to_id start_id end_id delay_second</code> <b> separate with space</b> example : <code> /clone -10077775444 -10073774747 34 3747 23</code>

* /userbot_about - <b>About Me</b>

<b>@Lx0980AI</b>        
        """,
        disable_web_page_preview=True,
        quote=True
    )
    
