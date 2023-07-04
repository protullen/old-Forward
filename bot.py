from pyrogram import (
    Client,
    __version__
)
from pyrogram.enums import ParseMode
from info import (
    API_HASH,
    APP_ID,
    LOGGER,
    TG_BOT_SESSION,
    TG_BOT_TOKEN,
    TG_BOT_WORKERS,
    TG_SLEEP_THRESHOLD
)
from .user import User


class Bot(Client):
    BOT_ID: int = None
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            name=TG_BOT_SESSION,
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins",
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN,
            sleep_threshold=TG_SLEEP_THRESHOLD,
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
        self.LOGGER(__name__).info("Bot stopped. Bye."
