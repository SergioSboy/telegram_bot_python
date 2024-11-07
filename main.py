import telebot
import sqlite3
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)
name = None


@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('data.sql')
    cur = conn.cursor()

    cur.execute(
        'CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), password varchar(50)')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'HI!')
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Type password!')
    bot.register_next_step_handler(message, user_pass)


def user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect('data.sql')
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, password) VALUES ('%s', '%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Users', callback_data='users'))
    bot.send_message(message.chat.id, 'Success', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('data.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''
    for user in users:
        info += f'Name: {user[1]}, Password: {user[2]}\n'
    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)


bot.polling(none_stop=True)

# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = telebot.types.ReplyKeyboardMarkup()
#     btn1 = types.KeyboardButton('Go site')
#     markup.add(btn1)
#     btn2 = types.KeyboardButton('Ответить')
#     btn3 = types.KeyboardButton('Изменить текст')
#     markup.add(btn2, btn3)
#     bot.send_message(message.chat.id, 'Hi!', reply_markup=markup)
#     bot.register_next_step_handler(message, on_click)
#
#
# def on_click(message):
#     if message.text == 'Go site':
#         bot.send_message(message.chat.id, 'Website is open')
#     elif message.text == 'Ответить':
#         bot.send_message(message.chat.id, 'Ответить')
#
#
# @bot.message_handler(content_types=['text'])
# def get_text(message):
#     markup = telebot.types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton('Go site', url='https://www.google.com')
#     markup.add(btn1)
#     btn2 = types.InlineKeyboardButton('Ответить', callback_data='1')
#     btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='2')
#     markup.add(btn2, btn3)
#     bot.reply_to(message, 'Nice text', reply_markup=markup)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(callback):
#     if callback.data == '1':
#         bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
#     elif callback.data == '2':
#         bot.edit_message_text("Edit text", callback.message.chat.id, callback.message.message_id)
#
#
# bot.infinity_polling()
