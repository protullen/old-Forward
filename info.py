import os
import logging
from logging.handlers import RotatingFileHandler


API_HASH = os.environ.get("API_HASH")
APP_ID = int(os.environ.get("APP_ID"))
BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
USER_SESSION = os.environ.get("TG_USER_SESSION")
AUTH_USERS = ["5326801541", "5924365859"]

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "OldForwardBot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
