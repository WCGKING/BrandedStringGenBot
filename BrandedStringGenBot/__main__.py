import asyncio
import importlib

from pyrogram import idle

from BrandedStringGenBot import app, db, logger
from BrandedStringGenBot.modules import all_modules


async def BrandedStringGenBot_boot():
    try:
        await app._start()
    except Exception as ex:
        raise RuntimeError(ex)
    await db.connect()

    for module in all_modules:
        importlib.import_module(f"BrandedStringGenBot.modules.{module}")
    logger.info(f"Loaded {len(all_modules)} modules.")

    await idle()
    await app._stop()
    await db.close()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(BrandedStringGenBot_boot())
    logger.info("Stopping String Gen Bot...")
