import asyncio
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = "8905509516:AAHCAPiDOPA3IseS6TI2WD

ZE97a6m6TExjc"

async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Manga image receive ho gayi!")

async def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        MessageHandler(filters.PHOTO, photo_handler)
    )

    print("Bot Running...")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())