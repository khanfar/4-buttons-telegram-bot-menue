from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

def start(update, context):
    keyboard = [
        [
            InlineKeyboardButton("start", callback_data='start'),
            InlineKeyboardButton("Reset", callback_data='reset'),
        ],
        [
            InlineKeyboardButton("Stats", callback_data='stats'),
            InlineKeyboardButton("Resend", callback_data='resend'),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose a command:', reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query

    query.answer()
    query.edit_message_text(text=f"/{query.data}")

def main():
    
    updater = Updater("6242520155:AAFpGmoE6Z2MTnW9B9l-9bApQlBhuEIVFg0")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()