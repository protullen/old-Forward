import os
import logging
from logging.handlers import RotatingFileHandler


API_HASH = os.environ.get("API_HASH", "dd47d5c4fbc31534aa764ef9918b3acd")
APP_ID = int(os.environ.get("APP_ID", "21288218"))
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6285956621:AAGkFHYXc_Rr4MKJoqOZQR7xQJS63E3PwuA")
USER_SESSION = os.environ.get("USER_SESSION")
AUTH_USERS = ["5326801541", "5924365859", "5163706369"]

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
