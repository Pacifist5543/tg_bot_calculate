from telebot import TeleBot
from telebot import types

TOKEN = "7673919440:AAHbdd3UoD_FXuFDUOfym4hM8UKlfOMT-Lw"
bot =  TeleBot(TOKEN)

kb = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton("/start")
btn2 = types.KeyboardButton("/help")
kb.add(btn1, btn2)

@bot.message_handler(commands=["start"])
def handle_start(msg: types.Message):
    bot.send_message(
    msg.chat.id,
    (
        "Привет! Я бот помогатор\n"
        "Доступные команды: /start, /help"
    ),
    reply_markup=kb )

@bot.message_handler(commands=["help"])
def handle_start(msg: types.Message):
    bot.send_message(
    msg.chat.id,
    (
        "Есть еще одна команда"
    ),
    reply_markup=kb )





bot.polling()