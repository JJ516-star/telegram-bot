import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN 没有设置，请检查 Railway Variables")
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

if __name__ == "__main__":
    main()
print("BOT_TOKEN set?", bool(TOKEN), "len=", 0 if not TOKEN else len(TOKEN))
