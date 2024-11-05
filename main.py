import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет!')

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