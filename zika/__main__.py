import time
import importlib 
from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from zika import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots, app, ids
from zika.split.misc import create_botlog, git, heroku
from zika.modules import ALL_MODULES

MSG_ON = """
✔️ **Zika Userbot Activated**
╼┅━━━━━━━━━╍━━━━━━━━━┅╾
🤖 **Userbot Version -** `{}`
⌨️ **Ketik** `{}alive` **untuk Mengecheck Bot**
╼┅━━━━━━━━━╍━━━━━━━━━┅╾
"""
MSG_BOT = (f"**Zika Assistant**\nis alive...")


async def main():
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module(f"ling.modules.{all_module}")
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("storyQi")
            await bot.join_chat("HyperSupportQ")
            ids.append(bot.me.id)
            try:
                await bot.send_message(
                    BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER)
                )
                await app.send_message(BOTLOG_CHATID, MSG_BOT)
            except BaseException:
                pass
            LOGGER("✔️").info(
                f"masuk sebagai {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("master").warning(a)
    LOGGER("✔️").info(f"ZikaRobot v{BOT_VER} [✨ UDAH AKTIF ✨]")
    if not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("✔️").info("Starting ZikaRobot")
    install()
    heroku()
    LOOP.run_until_complete(main())
