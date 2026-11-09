import os
from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")
REPLY_TEXT = os.getenv(
    "REPLY_TEXT",
    "Hello! I'm currently unavailable. I'll reply when I'm back."
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

    port = int(os.environ.get("PORT", 10000))
    base_url = os.environ.get("RENDER_EXTERNAL_URL")

    if not base_url:
        raise ValueError("RENDER_EXTERNAL_URL is missing!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        MessageHandler(filters.ALL, auto_reply)
    )

    print("Bot is starting with Webhook...")

    app.run_webhook(
        listen="0.0.0.0",
        port=port,
        url_path=TOKEN,
        webhook_url=f"{base_url}/{TOKEN}",
        drop_pending_updates=True,
    )

if __name__ == "__main__":
    main()
