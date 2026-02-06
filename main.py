import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")
USERNAME = "JJ_367"   # 你的telegram用户名（不含@）
REPLY = "please wait a moment ❤️"

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
    text = update.message.text
    if f"@{USERNAME}" in text:
        await update.message.reply_text(REPLY)

def main():
    # 这里先打印检查（跑通后你再删掉这一行）
    print("BOT_TOKEN exists?", bool(TOKEN), "len=", 0 if not TOKEN else len(TOKEN))

    if not TOKEN:
        raise ValueError("BOT_TOKEN 没有设置，请检查 Railway Variables（Production 环境）")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    app.run_polling()

if __name__ == "__main__":
    main()
