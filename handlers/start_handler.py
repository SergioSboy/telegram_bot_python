from telebot import types
from database.db import add_user


def start(bot, message):
    bot.send_message(message.chat.id, "Hello! What's your name?")
    bot.register_next_step_handler(message, lambda msg: get_name(bot, msg))


def get_name(bot, message):
    name = message.text
    add_user(name)
    bot.send_message(message.chat.id, f"Nice to meet you, {name}! You have been added to the database.")
