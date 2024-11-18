import telebot
import json


def set_menu_btns(kb):
    btn_rate = telebot.types.InlineKeyboardButton(
        "Райтинг преподователей",
        callback_data= "teachers_rate"
    )

    btn_set_mark = telebot.types.InlineKeyboardButton(
        'Поставить оценку: ',
        callback_data= "set_mark"
    )

    kb.row(btn_rate)
    kb.row(btn_set_mark)

def show_rate(kb, call, bot):
    with open("teachers.json", 'r', encoding="UTF-8") as db_file:
        teachers = json.load(db_file)

    teachers_list = sorted(teachers.values(), key = lambda t: t.get('likes') - t.get("dislikes"),
                           reverse= True)
    

    text = "Рейтинг; \n\n"
    for teachers in teachers_list:
        rate = teachers.get("likes") - teachers.get('dislikes')
        if rate < 0: rate = 0
        text += f"{teachers.get("name")} {teachers.get("lastname")} : {rate}\n"

    back_btn = telebot.types.InlineKeyboardButton('Назад',
                                                  callback_data= "go_back")
    kb.row(back_btn)

    bot.edit_message_text(text, call.message.chat.id, call.message.id)    

def set_courses_btns(kb):
    with open ("courses.json", 'r', encoding= 'UTF-8') as db_file:
        courses = json.load(db_file)

    for k, v in courses.items():
        btn = telebot.types.InlineKeyboardButton(
            v, callback_data= f'set_mark&selected_course={k}')
        kb.row(btn)

def set_teachers_btns(kb, selected_course):
    with open('teachers.json', 'r', encoding='UTF-8') as db_file:
        teachers = json.load(db_file)

    selected_teachers = []
    for id, t in teachers.items():
        if selected_course in t.get('courses'):
            selected_teachers.append((id, t))

    for id, t in selected_teachers:
        btn = telebot.types.InlineKeyboardButton(
            f'{t.get("name")} {t.get("lastname")}',
            callback_data=f'set_mark&selected_teacher={id}')
        kb.row(btn)
