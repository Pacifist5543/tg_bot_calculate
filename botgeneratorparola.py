from telebot import TeleBot
from telebot import types
import string
import random

TOKEN = "7673919440:AAHbdd3UoD_FXuFDUOfym4hM8UKlfOMT-Lw"
bot =  TeleBot(TOKEN)

kb = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton("/start")
btn2 = types.KeyboardButton("/сгенерировать пароль")
kb.add(btn1, btn2)

def generate_password():
    password = ""
    symbol = string.ascii_letters + string.digits + string.punctuation

    for i in range(random.randint(10, 15)):
        password += random.choice(symbol)

    return password

@bot.message_handler(commands=["start"])
def handle_start(msg: types.Message):
    bot.send_message(
    msg.chat.id,
    "Привет! Я бот помогатор\n"
    "нажми на /generatepassword что бы я сгенерировал тебе пароль ", 
    reply_markup=kb )

@bot.message_handler(commands=["generatepassword"])
def handle_start(msg: types.Message):
    password = generate_password()
    bot.send_message(
        msg.chat.id,
        password 
    )








bot.polling()