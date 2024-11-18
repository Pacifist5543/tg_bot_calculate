import telebot
import json
import mini

TOKEN = "7673919440:AAHbdd3UoD_FXuFDUOfym4hM8UKlfOMT-Lw"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands= ["start"])
def handle_start(message):
    kb = telebot.types.InlineKeyboardMarkup()
    mini.set_menu_btns(kb)
    bot.send_message(message.chat.id, 'Доступные команды: ', reply_markup= kb)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    print(call.data)
    kb = telebot.types.InlineKeyboardMarkup()
    if call.data == "teachers_rate":
        mini.show_rate(kb, call, bot)


    if call.data == "set_mark":
        mini.set_courses_btns(kb)
        bot.edit_message_text('Доступные курсы:', call.message.chat.id, call.message.id)

    if 'set_mark' in call.data and 'selected_course' in call.data:
        selected_course = call.data.split('=')[-1]
        mini.set_teachers_btns(kb, selected_course)
        bot.edit_message_text('Доступные преподователи:', call.message.chat.id, call.message.id)

    if 'go_back' in call.data:
        bot.edit_message_text('Доступные команды:', call.message.chat.id, call.message.id)
        kb = telebot.types.InlineKeyboardMarkup()
        mini.set_menu_btns(kb)

        
    bot.edit_message_reply_markup(  call.message.chat.id,
                                    call.message.id,
                                    reply_markup= kb  )

bot.polling(non_stop= True, interval=1)
