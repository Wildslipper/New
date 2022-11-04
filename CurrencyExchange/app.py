import telebot
from config import keys, TOKEN
import requests
import json

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'choose_first_currency'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Euro', 'Dollar', 'Ruble')
    mess = bot.send_message(message.chat.id,
                            f'Hi, <b>{message.from_user.first_name}</b>! Let\'s change the currency. \n'
                            f'Выберете валюту из которой хотите перевести:', parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(mess, choose_second_currency)


def choose_second_currency(message):
    if message.text == 'Euro':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Dollar', 'Ruble')
        mess = bot.send_message(message.chat.id, 'Выберете валюту в которую хотите перевести', reply_markup=markup)
        bot.register_next_step_handler(mess, amount_euro)
    elif message.text == 'Dollar':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Euro', 'Ruble')
        mess = bot.send_message(message.chat.id, 'Выберете валюту в которую хотите перевести', reply_markup=markup)
        bot.register_next_step_handler(mess, amount_dollar)
    elif message.text == 'Ruble':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Euro', 'Dollar')
        mess = bot.send_message(message.chat.id, 'Выберете валюту в которую хотите перевести', reply_markup=markup)
        bot.register_next_step_handler(mess, amount_ruble)


def amount_euro(message):
    if message.text == 'Dollar':
        mess = bot.send_message(message.chat.id, 'Введите количество')
        bot.register_next_step_handler(mess, convert_euro_dollar)
    elif message.text == 'Ruble':
        mess = bot.send_message(message.chat.id, 'Введите количество')
        bot.register_next_step_handler(mess, convert_euro_ruble)


def convert_euro_dollar(message):
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=EUR&tsyms=USD')
    answ = json.loads(r.text)[keys['Dollar']]
    if message.text != float:
        bot.send_message(message.chat.id, f'Стоимость вашей валюты: {str(float(message.text) * answ)} долларов')


def convert_euro_ruble(message):
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=EUR&tsyms=RUB')
    answ = json.loads(r.text)[keys['Ruble']]
    if message.text != float:
        bot.send_message(message.chat.id, f'Стоимость вашей валюты: {str(float(message.text) * answ)} рублей')


def amount_dollar(message):
    if message.text == 'Euro':
        mess = bot.send_message(message.chat.id, 'Введите количество')
        bot.register_next_step_handler(mess, convert_dollar_euro)
    elif message.text == 'Ruble':
        mess = bot.send_message(message.chat.id, 'Введите количество')
        bot.register_next_step_handler(mess, convert_dollar_ruble)


def convert_dollar_euro(message):
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=USD&tsyms=EUR')
    answ = json.loads(r.text)[keys['Euro']]
    if message.text != float:
        bot.send_message(message.chat.id, f'Стоимость вашей валюты: {str(float(message.text) * answ)} евро')


def convert_dollar_ruble(message):
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=USD&tsyms=RUB')
    answ = json.loads(r.text)[keys['Ruble']]
    if message.text != float:
        bot.send_message(message.chat.id, f'Стоимость вашей валюты: {str(float(message.text) * answ)} рублей')


def amount_ruble(message):
    if message.text == 'Euro':
        mess = bot.send_message(message.chat.id, 'Введите количество')
        bot.register_next_step_handler(mess, convert_ruble_euro)
    elif message.text == 'Dollar':
        mess = bot.send_message(message.chat.id, 'Введите количество')
        bot.register_next_step_handler(mess, convert_ruble_dollar)


def convert_ruble_euro(message):
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=RUB&tsyms=EUR')
    answ = json.loads(r.text)[keys['Euro']]
    if message.text != float:
        bot.send_message(message.chat.id, f'Стоимость вашей валюты: {str(float(message.text) * answ)} евро')


def convert_ruble_dollar(message):
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=RUB&tsyms=USD')
    answ = json.loads(r.text)[keys['Dollar']]
    if message.text != float:
        bot.send_message(message.chat.id, f'Стоимость вашей валюты: {str(float(message.text) * answ)} долларов')


bot.polling(non_stop=True)
