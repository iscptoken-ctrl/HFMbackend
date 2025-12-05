from telegram import Update, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8364330882:AAFC1Sqe6wjt6I0ri-gv40W0ifWt03EEyzs"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            "Launch Game",
            web_app=WebAppInfo(url="https://USERNAME.github.io/holdforge-miniapp/")
        )
    ]])
    await update.message.reply_text("Hold Forge'a hoş geldin!", reply_markup=keyboard)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
