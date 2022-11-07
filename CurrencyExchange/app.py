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
                            f'Hello, <b>{message.from_user.first_name}</b>! Let\'s change the currency. \n'
                            f'Select the currency you want to transfer from:', parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(mess, choose_second_currency)


def choose_second_currency(message):
    if message.text == 'Euro':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Dollar', 'Ruble')
        mess = bot.send_message(message.chat.id, 'Select the currency you want to transfer to:', reply_markup=markup)
        bot.register_next_step_handler(mess, amount_euro)
    elif message.text == 'Dollar':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Euro', 'Ruble')
        mess = bot.send_message(message.chat.id, 'Select the currency you want to transfer to:', reply_markup=markup)
        bot.register_next_step_handler(mess, amount_dollar)
    elif message.text == 'Ruble':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Euro', 'Dollar')
        mess = bot.send_message(message.chat.id, 'Select the currency you want to transfer to:', reply_markup=markup)
        bot.register_next_step_handler(mess, amount_ruble)
    else:
        mess = bot.send_message(message.chat.id, 'You must select by clicking:')
        bot.register_next_step_handler(mess, choose_second_currency)


def amount_euro(message):
    close_button = telebot.types.ReplyKeyboardRemove()
    if message.text == 'Dollar':
        mess = bot.send_message(message.chat.id, 'Enter the quantity:', reply_markup=close_button)
        bot.register_next_step_handler(mess, convert_euro_dollar)
    elif message.text == 'Ruble':
        mess = bot.send_message(message.chat.id, 'Enter the quantity:', reply_markup=close_button)
        bot.register_next_step_handler(mess, convert_euro_ruble)
    else:
        mess = bot.send_message(message.chat.id, 'You must select by clicking:')
        bot.register_next_step_handler(mess, amount_euro)
def convert_euro_dollar(message):
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=EUR&tsyms=USD')
    ans = json.loads(r.text)[keys['Dollar']]
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('START')
    if message.text != float:
        try:
            bot.send_message(message.chat.id, f'The value of your currency is <b>{str(round(float(message.text) * ans, 2))}</b> dollars.', parse_mode ='html')
            mess = bot.send_message(message.chat.id,
                                    f'<b>{message.from_user.first_name}</b>, press start to select a currency.',
                                    parse_mode='html', reply_markup=markup)
            bot.register_next_step_handler(mess, start)
        except ValueError:
            mess = bot.send_message(message.chat.id, 'Enter a number')
            bot.register_next_step_handler(mess, convert_euro_dollar)
def convert_euro_ruble(message):
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=EUR&tsyms=RUB')
    ans = json.loads(r.text)[keys['Ruble']]
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('START')
    if message.text != float:
        try:
            bot.send_message(message.chat.id, f'The value of your currency is <b>{str(round(float(message.text) * ans, 2))}</b> rubles.', parse_mode='html')
            mess = bot.send_message(message.chat.id,
                                    f'<b>{message.from_user.first_name}</b>, press start to select a currency.',
                                    parse_mode='html', reply_markup=markup)
            bot.register_next_step_handler(mess, start)
        except ValueError:
            mess = bot.send_message(message.chat.id, 'Enter a number:')
            bot.register_next_step_handler(mess, convert_euro_ruble)

def amount_dollar(message):
    close_button = telebot.types.ReplyKeyboardRemove()
    if message.text == 'Euro':
        mess = bot.send_message(message.chat.id, 'Enter the quantity:', reply_markup=close_button)
        bot.register_next_step_handler(mess, convert_dollar_euro)
    elif message.text == 'Ruble':
        mess = bot.send_message(message.chat.id, 'Enter the quantity:', reply_markup=close_button)
        bot.register_next_step_handler(mess, convert_dollar_ruble)
    else:
        mess = bot.send_message(message.chat.id, 'You must select by clicking:')
        bot.register_next_step_handler(mess, amount_dollar)

def convert_dollar_euro(message):
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=USD&tsyms=EUR')
    ans = json.loads(r.text)[keys['Euro']]
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('START')
    if message.text != float:
        try:
            bot.send_message(message.chat.id, f'The value of your currency is <b>{str(round(float(message.text) * ans, 2))}</b> euros.', parse_mode='html')
            mess = bot.send_message(message.chat.id,
                                f'<b>{message.from_user.first_name}</b>, press start to select a currency.',
                                parse_mode='html', reply_markup=markup)
            bot.register_next_step_handler(mess, start)
        except ValueError:
            mess = bot.send_message(message.chat.id, 'Enter a number:')
            bot.register_next_step_handler(mess, convert_dollar_euro)

def convert_dollar_ruble(message):
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=USD&tsyms=RUB')
    ans = json.loads(r.text)[keys['Ruble']]
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('START')
    if message.text != float:
        try:
            bot.send_message(message.chat.id, f'The value of your currency is <b>{str(round(float(message.text) * ans, 2))}</b> rubles.', parse_mode='html')
            mess = bot.send_message(message.chat.id,
                                    f'<b>{message.from_user.first_name}</b>, press start to select a currency.',
                                    parse_mode='html', reply_markup=markup)
            bot.register_next_step_handler(mess, start)
        except ValueError:
            mess = bot.send_message(message.chat.id, 'Enter a number:')
            bot.register_next_step_handler(mess, convert_dollar_ruble)

def amount_ruble(message):
    close_button = telebot.types.ReplyKeyboardRemove()
    if message.text == 'Euro':
        mess = bot.send_message(message.chat.id, 'Enter the quantity:', reply_markup=close_button)
        bot.register_next_step_handler(mess, convert_ruble_euro)
    elif message.text == 'Dollar':
        mess = bot.send_message(message.chat.id, 'Enter the quantity:', reply_markup=close_button)
        bot.register_next_step_handler(mess, convert_ruble_dollar)
    else:
        mess = bot.send_message(message.chat.id, 'You must select by clicking:')
        bot.register_next_step_handler(mess, amount_ruble)


def convert_ruble_euro(message):
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=RUB&tsyms=EUR')
    ans = json.loads(r.text)[keys['Euro']]
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('START')
    if message.text != float:
        try:
            bot.send_message(message.chat.id, f'The value of your currency is <b>{str(round(float(message.text) * ans, 2))}</b> euros.', parse_mode='html')
            mess = bot.send_message(message.chat.id,
                                    f'<b>{message.from_user.first_name}</b>, press start to select a currency.',
                                    parse_mode='html', reply_markup=markup)
            bot.register_next_step_handler(mess, start)
        except ValueError:
            mess = bot.send_message(message.chat.id, 'Enter a number:')
            bot.register_next_step_handler(mess, convert_ruble_euro)

def convert_ruble_dollar(message):
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=RUB&tsyms=USD')
    ans = json.loads(r.text)[keys['Dollar']]
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('START')
    if message.text != float:
        try:
            bot.send_message(message.chat.id, f'The value of your currency is <b>{str(round(float(message.text) * ans, 2))}</b> dollars.', parse_mode='html')
            mess = bot.send_message(message.chat.id,
                                    f'<b>{message.from_user.first_name}</b>, press start to select a currency.',
                                    parse_mode='html', reply_markup=markup)
            bot.register_next_step_handler(mess, start)
        except ValueError:
            mess = bot.send_message(message.chat.id, 'Enter a number:')
            bot.register_next_step_handler(mess, convert_ruble_dollar)


bot.polling(non_stop=True)


