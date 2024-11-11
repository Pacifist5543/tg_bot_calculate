from telebot import TeleBot
from telebot import types

TOKEN = "7673919440:AAHbdd3UoD_FXuFDUOfym4hM8UKlfOMT-Lw"
bot =  TeleBot(TOKEN)

kb = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton("калькулятор")
btn2 = types.KeyboardButton("кнопка2")
kb.add(btn1, btn2)

@bot.message_handler(commands=["start"])
def handle_start(msg: types.Message):
    bot.send_message(
    msg.chat.id,
    "Привет! Я бот помогатор", 
    reply_markup=kb )


@bot.message_handler(content_types= ["text"])
def hendle_text(msg: types.Message):
    text = msg.text
    if text == "калькулятор":
        bot.send_message(msg.chat.id,
    "напиши пример который нужно решить",
    reply_markup=types.ReplyKeyboardRemove()
      )
        bot.register_next_step_handler(msg, calculate)
    else:
        bot.send_message(msg.chat.id, "не понял вас")


def calculate(msg: types.Message):
    try:
        result = eval(msg.text)
    except ZeroDivisionError:
        bot.send_message(msg.chat.id, "Нельзя делить на 0, попробуй другой пример")
        bot.register_next_step_handler(msg, calculate)
    except SyntaxError:
        bot.send_message(msg.chat.id, "Некоректный пример попробуй другой")
        bot.register_next_step_handler(msg, calculate)
    except NameError:
        bot.send_message(msg.chat.id, "Некоректный пример попробуй другой")
        bot.register_next_step_handler(msg, calculate)
    else:
        bot.send_message(msg.chat.id, f"Ответ: {result}", reply_markup= kb )


bot.polling()