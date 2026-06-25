from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "8905509516:AAGFTLo7hg4DFrN2BgzV82B36W2ZX1EAWc4"

async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Manga image receive ho gayi!")

app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.PHOTO, photo_handler))

print("Bot Running...")
app.run_polling()
