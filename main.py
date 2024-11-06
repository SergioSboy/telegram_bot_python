import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Go site')
    markup.add(btn1)
    btn2 = types.KeyboardButton('Ответить')
    btn3 = types.KeyboardButton('Изменить текст')
    markup.add(btn2, btn3)
    bot.send_message(message.chat.id, 'Hi!', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'Go site':
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == 'Ответить':
        bot.send_message(message.chat.id, 'Ответить')


@bot.message_handler(content_types=['text'])
def get_text(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Go site', url='https://www.google.com')
    markup.add(btn1)
    btn2 = types.InlineKeyboardButton('Ответить', callback_data='1')
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='2')
    markup.add(btn2, btn3)
    bot.reply_to(message, 'Nice text', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(callback):
    if callback.data == '1':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == '2':
        bot.edit_message_text("Edit text", callback.message.chat.id, callback.message.message_id)


bot.infinity_polling()
