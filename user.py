from pyrogram import Client
from pyrogram.enums import ParseMode
from info import API_HASH, APP_ID, LOGGER, USER_SESSION

class User(Client):  
    def __init__(self):
        super().__init__(
            name="SearchUser",
            session_string=USER_SESSION,
            api_hash=API_HASH,
            api_id=APP_ID,
            workers=4,
            sleep_threshold=10,
            parse_mode=ParseMode.HTML
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.LOGGER(__name__).info(
            f"{me.username} Userbot started! 👤 "
        )
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("User stopped. Bye.")
