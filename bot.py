# bot.py
import telebot
from config import TOKEN
from database.db import init_db
from handlers import start_handler, help_handler

bot = telebot.TeleBot(TOKEN)

init_db()


@bot.message_handler(commands=['start'])
def handle_start(message):
    start_handler.start(bot, message)


@bot.message_handler(commands=['help'])
def handle_help(message):
    help_handler.help(bot, message)


# Запуск бота
if __name__ == '__main__':
    print("Bot is running...")
    bot.polling(none_stop=True)
