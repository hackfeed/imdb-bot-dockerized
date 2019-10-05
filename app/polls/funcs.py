# -*- coding: utf-8 -*-
from telebot import types
from .config import lang, messages
from functools import reduce
from imdb import IMDb
from imp import reload
import subprocess
import sys

reload(sys)
# sys.setdefaultencoding('utf-8')

hide_markup = types.ReplyKeyboardRemove(selective=False)


def send_msg(bot, obj_msg, msg, *argv):
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)
    argv = list(argv)

    list(map(lambda x: markup.add(x), argv))
    # for i in range(len(argv)):
    # markup.add(argv[i])

    bot.send_message(obj_msg.chat.id, msg,
                     reply_markup=markup, parse_mode="markdown")


def change_lang(bot, message, user):
    if message.text not in lang:
        bot.send_message(
            message.chat.id, "❗ Выберите корректный язык из списка / Select available language.")
    else:
        if message.text == "English":
            user.language = "en"
        else:
            user.language = "ru"

        user.save()
        phr_dict = messages[user.expected_cmd]
        user.expected_cmd = "main_menu"
        user.save()
        dict_fl = messages[user.expected_cmd]
        send_msg(bot, message, phr_dict[user.language], dict_fl[user.language])


def find_films(msg, films):
    return reduce(lambda x, y: x + u"📌 " + str(y) + "\n", films[:8], msg)


def who_is(person):
    return person[3:person.index(':') - 1]


def form_message(id_act, ia, user):
    person = ia.get_person(id_act)
    dict_phr = messages["last_films"]
    msg = dict_phr[user.language]
    films = person["filmography"]

    if "actor" not in str(films) and "actress" not in str(films):
        return "NONE"

    for film in films:
        activity = who_is(str(film))

        if activity == u"actor":
            fin_flm = film["actor"]
            break
        elif activity == u"actress":
            fin_flm = film["actress"]
            break

    msg = find_films(msg, fin_flm)
    msg += "\n🔦 IMDb: https://www.imdb.com/name/nm" + id_act

    return msg


def find_actor(bot, message, user):
    dict_phr = messages["load"]
    bot.send_message(
        message.chat.id, dict_phr[user.language], reply_markup=hide_markup)
    bot.send_chat_action(message.chat.id, "typing")

    ia = IMDb()
    persons = ia.search_person(message.text, results=1)

    if persons[0]["name"] == message.text:
        bot.send_chat_action(message.chat.id, "typing")
        msg = form_message(persons[0].personID, ia, user)
    else:
        dict_phr = messages["no_man"]
        bot.send_message(
            message.chat.id, dict_phr[user.language], reply_markup=hide_markup)
        return

    if "NONE" == msg:
        dict_phr = messages["not_actor"]
        bot.send_message(
            message.chat.id, dict_phr[user.language], reply_markup=hide_markup)
        return

    if user.expected_cmd == "first_actor":
        user.expected_cmd = "confirm_actor"
        user.first_act = message.text
    else:
        user.expected_cmd = "confirm_actor2"
        user.second_act = message.text
    user.save()
    dict_phr = messages[user.expected_cmd]
    send_msg(bot, message, msg, *dict_phr[user.language])


def format_id(id_act):
    return '0' * (7 - len(id_act)) + id_act


def pars_ids(msg, user, act1, act2):
    dict_phr = messages["link_info"]
    arr_msg = msg.split()
    imdb_ex = " ([IMDb](https://www.imdb.com/name/nm"

    if "NO_ACT" in arr_msg[0]:
        dict_err = messages["err_info"]

        return dict_err[user.language]

    if "NO_CNCT" in arr_msg[0]:
        dict_cnct = messages["no_cnct"]

        return dict_cnct[user.language]

    fin_msg = dict_phr[user.language][0] + act1 + \
        dict_phr[user.language][1] + act2 + "\n\n"
    fin_msg += dict_phr[user.language][2] + \
        str(arr_msg[0]) + dict_phr[user.language][3] + "\n\n"
    fin_msg = reduce(lambda x, y: x + "💼 " + arr_msg[y].replace('_', ' ') + imdb_ex +
                     format_id(arr_msg[y + 1]) + ")) ➡ \n", range(1, len(arr_msg), 2), fin_msg)

    return fin_msg


def find_link(bot, message, user, act1, act2):
    bot.send_chat_action(message.chat.id, "typing")
    res = subprocess.check_output(
        ["/root/IMDBbot/IMDBgame/./game.out", act1, act2])

    dict_phr = messages["try_more"]
    list_phr = dict_phr[user.language]
    msg = pars_ids(res, user, act1, act2)
    send_msg(bot, message, msg, *[list_phr[0] +
                                  act1, list_phr[0] + act2, list_phr[1]])


def pars_name(msg):
    return msg[msg.index(':') + 2:]
