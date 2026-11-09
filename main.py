import os
from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.getenv("BOT_TOKEN")
REPLY_TEXT = os.getenv(
    "REPLY_TEXT",
    "Hello! I'm currently unavailable. I'll reply when I'm back. ❤️"
)

async def auto_reply(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    if update.message:
        await update.message.reply_text(REPLY_TEXT)

def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN is missing!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        MessageHandler(filters.ALL, auto_reply)
    )

    print("Bot is running!")
    app.run_polling()

if __name__ == "__main__":
    main()
