from pyrogram import Client
from pyrogram.enums import ParseMode
from info import API_HASH, APP_ID, LOGGER, SESSION

class User(Client):  
    def __init__(self):
        super().__init__(
            name="SearchUser",
            in_memory=True,
            session_string=TG_USER_SESSION,
            api_hash=API_HASH,
            api_id=APP_ID,
            workers=4,
            sleep_threshold=10,
            parse_mode=ParseMode.HTML
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = self.me
        self.LOGGER(__name__).info(
            f"{usr_bot_me} started! 👤 "
        )
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("User stopped. Bye."
