
import telebot
from telebot import types
from config import TOKEN
from main import variant_game

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])

def start(message):
    text = 'игра начинается'
    bot.send_message(message.chat.id, text)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('👊🏻')
    item2 = types.KeyboardButton('✌🏻')
    item3 = types.KeyboardButton('✋🏻')

    markup.add(item1, item2, item3)
    text = 'выбери свой вариант'
    bot.send_message(message.chat.id, text , reply_markup=markup)

@bot.message_handler(content_types=['text'])

def lalala(message):
    if message.chat.type == 'private':
        if message.text == '👊🏻':
            result = variant_game(1)
            bot.send_message(message.chat.id, result)
        elif message.text == '✌🏻':
            result = variant_game(2)
            bot.send_message(message.chat.id, result)
        elif message.text == '✋🏻':
            result = variant_game(3)
            bot.send_message(message.chat.id, result)
        
        else:
            bot.send_message(message.chat.id, 'Вы выбрали не тот смайл!')

bot.polling(non_stop=True)