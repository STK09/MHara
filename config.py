#Recoded by @Soutick_09

import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7605638686:AAFKKl61lf8M26SRHRCzH644BorMnfHLzIo")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28450765"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "36f00f11f9d5c65e69b81fd804453a93")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002377657105"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5827289728"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Mizuhara:Mizuhara@cluster0.3uq9p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1002341196202"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1002418914562"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#pics
START_PIC = os.environ.get("START_PIC", "https://envs.sh/YVM.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/CDA.jpg")

#text
HELP_TXT = "<b>Hello Dude 😎!\n\nTo use this bot you just have to join both channels that's it..\nWatch Tutorial to Open Link »»» <a href=https://t.me/+75PHDBuMxzFkMTA1>CLICK HERE</a></b>"
ABOUT_TXT = """<b>○ Creator: <a href=https://t.me/Soutick_09>Soutick</a>\n○ Backup Channel: <a href=https://t.me/AIO_Backup>AIO Backup</a>\n○ Best Friend: <a href=tg://settings>This Person</a>\n○ Watch Online Anime: <a href=https://anitown4u.com>AniTown4U</a></b>"""
SHORT_MSG = "Your Link is down here click on Short URL.."

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Ara! Ara! {first}! 💥\n\nI am That Bot Who can Make Your Day Happy 😂...!\n\n Made With ♥️ By <a href=https://t.me/AIO_Backup>AIO Backup</a></b>")
try:
    ADMINS=[5827289728]
    for x in (os.environ.get("ADMINS", "5827289728 7272399911").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}!⚡\n\n🫧 ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ʙᴏᴛʜ ᴏꜰ ᴏᴜʀ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ...!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

#Short Url or Api
SHORT_URL = os.environ.get("SHORTNER_URL", "speedlinkurl.com")
SHORT_API = os.environ.get("SHORTNER_API", "f057d06e680b696948fd121f6335ea77744f58f4")

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<i>What Do You Think that I am Your Notepad? Why You Message Here?</i>"

AUTO_DEL = os.environ.get("AUTO_DEL", "True")
DEL_TIMER = int(os.environ.get("DEL_TIMER", "120"))
DEL_MSG = """<b>Made With ♥️ By <a href=https://t.me/AIO_Backup>AIO Backup</a></b>"""

ADMINS.append(OWNER_ID)
ADMINS.append(5827289728)

LOG_FILE_NAME = "filesharingbot.txt"

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

#Bhen ke lavdo Credit hataya na ma choddunga wahi aakr salo use karo bas 
