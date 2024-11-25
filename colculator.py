from telebot import TeleBot
from telebot import types
score = 0

TOKEN = "7673919440:AAHbdd3UoD_FXuFDUOfym4hM8UKlfOMT-Lw"
bot =  TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def handle_start(msg: types.Message):
    kb = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton (
        "Начать викторину",
        callback_data= "start_viktor"
    )
    kb.row(btn)
    bot.send_message(
    msg.chat.id,
    "Привет! Я бот викторина",  reply_markup=kb)


@bot.callback_query_handler(func = lambda call: True )
def handle_coollback(call:types.CallbackQuery):
    global score
    if call.data == "start_viktor":
        kb = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton (
            "ответ 1: 72",
            callback_data= "true-1"
        )
        btn2 = types.InlineKeyboardButton (
            "ответ 2: 89",
            callback_data= "false-1"
        )
        kb.row(btn1)
        kb.row(btn2)
        bot.send_message(
            call.message.chat.id,
            "Сколько будет 8*9 ",  reply_markup=kb)

    
    if call.data.endswith('1'):
        if "true" in call.data:
            bot.send_message(
            call.message.chat.id,"Правильно")
            score += 1
        else:
            bot.send_message(
            call.message.chat.id,"Неправильно")
        kb = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton (
            "ответ 1: 7573",
            callback_data= "true-2"
        )
        btn2 = types.InlineKeyboardButton (
            "ответ 2: 7561",
            callback_data= "false-2")
        kb.row(btn1)
        kb.row(btn2)
        bot.send_message(
            call.message.chat.id,
            "Сколько будет 8456-895 ",  reply_markup=kb)


    if call.data.endswith('2'):
        if "true" in call.data:
            bot.send_message(
            call.message.chat.id,"Правильно")
            score += 1
        else:
            bot.send_message(
            call.message.chat.id,"Неправильно")
        kb = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton (
            "ответ 1: 252",
            callback_data= "true-3"
        )
        btn2 = types.InlineKeyboardButton (
            "ответ 2: 268",
            callback_data= "false-3"
        )
        kb.row(btn1)
        kb.row(btn2)
        bot.send_message(
            call.message.chat.id,
            "Сколько будет 84*3 ",  reply_markup=kb)
        

    if call.data.endswith('3'):
        if "true" in call.data:
            bot.send_message(
            call.message.chat.id,"Правильно")
            score += 1
        else:
            bot.send_message(
            call.message.chat.id,"Неправильно")
        kb = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton (
            "ответ 1: 899",
            callback_data= "true-4"
        )
        btn2 = types.InlineKeyboardButton (
            "ответ 2: 999",
            callback_data= "false-4"
        )
        kb.row(btn1)
        kb.row(btn2)
        bot.send_message(
            call.message.chat.id,
            "Сколько будет 29*31 ",  reply_markup=kb)
        
        
    if call.data.endswith('4'):
        if "true" in call.data:
            bot.send_message(
            call.message.chat.id,"Правильно")
            score += 1
        else:
            bot.send_message(
            call.message.chat.id,"Неправильно")
        kb = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton (
            "ответ 1: 0",
            callback_data= "false-5"
        )
        btn2 = types.InlineKeyboardButton (
            "ответ 2: Деление на ноль невозможно",
            callback_data= "true-5"
        )
        kb.row(btn1)
        kb.row(btn2)
        bot.send_message(
            call.message.chat.id,
            "Сколько будет 8 / 0 ",  reply_markup=kb)
        
        
    if call.data.endswith('5'):
        if "true" in call.data:
            bot.send_message(
            call.message.chat.id,"Правильно")
            score += 1
        else:
            bot.send_message(
            call.message.chat.id,"Неправильно")
        kb = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton (
            "ответ 1: Деление на ноль невозможно",
            callback_data= "false-6"
        )
        btn2 = types.InlineKeyboardButton (
            "ответ 2: 0",
            callback_data= "true-6"
        )
        kb.row(btn1)
        kb.row(btn2)
        bot.send_message(
            call.message.chat.id,
            "Сколько будет 0 / 8 ",  reply_markup=kb)
        
        
    if call.data.endswith('6'):
        if "true" in call.data:
            bot.send_message(
            call.message.chat.id,"Правильно")
            score += 1
        else:
            bot.send_message(
            call.message.chat.id,"Неправильно")
        kb = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton (
            "ответ 1: 160",
            callback_data= "false-7"
        )
        btn2 = types.InlineKeyboardButton (
            "ответ 2: 170",
            callback_data= "true-7"
        )
        kb.row(btn1)
        kb.row(btn2)
        bot.send_message(
            call.message.chat.id,
            "Сколько будет 85/5*10",  reply_markup=kb)
        

    if call.data.endswith('7'):
        if "true" in call.data:
            bot.send_message(
            call.message.chat.id,"Правильно")
            score += 1
        else:
            bot.send_message(
            call.message.chat.id,"Неправильно")
        kb = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton (
            "ответ 1: 12048",
            callback_data= "true-8"
        )
        btn2 = types.InlineKeyboardButton (
            "ответ 2: 13322",
            callback_data= "false-8"
        )
        kb.row(btn1)
        kb.row(btn2)
        bot.send_message(
            call.message.chat.id,
            "Сколько будет 8451-6945*8 ",  reply_markup=kb)
        

    if call.data.endswith('8'):
        if "true" in call.data:
            bot.send_message(
            call.message.chat.id,"Правильно")
            score += 1
        else:
            bot.send_message(
            call.message.chat.id,"Неправильно")
        kb = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton (
            "ответ 1: -1765",
            callback_data= "false-9"
        )
        btn2 = types.InlineKeyboardButton (
            "ответ 2: -1802",
            callback_data= "true-9"
        )
        kb.row(btn1)
        kb.row(btn2)
        bot.send_message(
            call.message.chat.id,
            "Сколько будет 854-2656 ",  reply_markup=kb)
        
        
        

    if call.data.endswith('9'):
        if "true" in call.data:
            bot.send_message(
            call.message.chat.id,"Правильно")
            score += 1
        else:
            bot.send_message(
            call.message.chat.id,"Неправильно")
        kb = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton (
            "ответ 1: 210000",
            callback_data= "true-10"
        )
        btn2 = types.InlineKeyboardButton (
            "ответ 2: 267439",
            callback_data= "false-10"
        )
        kb.row(btn1)
        kb.row(btn2)
        bot.send_message(
            call.message.chat.id,
            "x - 347 * (2376/4) = 3882\n чему равен x ?",  reply_markup=kb)
    
    
    if call.data.endswith('10'):
        if "true" in call.data:
            bot.send_message(
            call.message.chat.id,"Правильно")
            score += 1
        else:
            bot.send_message(
            call.message.chat.id,"Неправильно")
                
        bot.send_message(call.message.chat.id,
            f'ваш счет: {score}/ 10')
    
bot.polling()