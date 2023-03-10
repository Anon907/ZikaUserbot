from distutils.util import strtobool
from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


ALIVE_EMOJI = getenv("ALIVE_EMOJI", "👑")
ALIVE_LOGO = getenv("ALIVE_LOGO", "https://telegra.ph//file/22f35f48a7f9900d555be.jpg")
ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "Hey bro, I am Zika.")
API_HASH = getenv("API_HASH", "34efb38c74d5e6b25d1bb6234396a8af")
API_ID = getenv("API_ID", "")
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001507828862]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_VER = "1.0.3@zika"
BRANCH = getenv("BRANCH", "main") # jangan di ganti kalo ga mau error tolol
CH_SFS = getenv("CH_SFS", "heinoob") # kalo lu mau ganti minimal follow dulu lah kontol
IG_ALIVE = getenv("IG_ALIVE", "zikanih") # kalo lu mau ganti minimal follow dlu lah kontol
CHANNEL = getenv("CHANNEL", "heinoob") # kalo lu mau ganti minimal follow dulu lah kontol
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "")
GIT_TOKEN = getenv("GIT_TOKEN", "") # optional punya lo ya kontol
GROUP = getenv("GROUP", "ZikaSupportGroup") # kontol klo lu ganti 
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
OPENAI_API_KEY = getenv("OPENAI_API_KEY", "")
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
REPO_URL = getenv("REPO_URL", "https://github.com/Anon907/ZikaUserbot")
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
