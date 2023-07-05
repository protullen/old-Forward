from pyrogram import Client, __version__
from pyrogram.enums import ParseMode
from info import API_HASH, APP_ID, LOGGER, BOT_TOKEN
from user import User


class Bot(Client):
    BOT_ID: int = None
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            name="Old-Forward",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins",
            },
            workers=4,
            bot_token=BOT_TOKEN,
            sleep_threshold=10,
            parse_mode=ParseMode.HTML
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = self.me
        self.BOT_ID = usr_bot_me.id
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username} started!"
        )
        self.USER, self.USER_ID = await User().start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
