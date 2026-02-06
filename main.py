import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("8502314659:AAEU9BZsepeZyjsOQXf8gTY8pNpx30QTtGo")
USERNAME = "JJ_367"   # 你的Telegram用户名
REPLY = "please wait a moment ❤️"

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text

    if f"@{USERNAME}" in text:
        await update.message.reply_text(REPLY)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    app.run_polling()

if name == "main":
    main()
