# -*- coding: utf-8 -*-

from core.models import User
from .funcs import *
from .config import messages

hide_markup = types.ReplyKeyboardRemove(selective=False)


def main_func(bot, message):
    user = User.objects.get(login=message.from_user.username)

    # Выбор языка
    if user.expected_cmd == "language":
        change_lang(bot, message, user)

    # Главное меню
    if user.expected_cmd == "main_menu":
        if u"⭐️" in message.text:
            user.expected_cmd = "first_actor"
            user.save()
            dict_phr = messages[user.expected_cmd]
            bot.send_message(
                message.chat.id, dict_phr[user.language], reply_markup=hide_markup)

    # Ввод имени первого актера
    if user.expected_cmd == "first_actor" and u"⭐️" not in message.text:
        find_actor(bot, message, user)

    # Подтверждение имени первого актера
    if user.expected_cmd == "confirm_actor":
        if u"✅" in message.text:
            user.expected_cmd = "second_actor"
        elif u"🔙" in message.text:
            user.expected_cmd = "first_actor"
            user.first_act = "None"
        else:
            return

        user.save()
        dict_phr = messages[user.expected_cmd]
        bot.send_message(
            message.chat.id, dict_phr[user.language], reply_markup=hide_markup)

    # Ввод имени второго актера
    if user.expected_cmd == "second_actor" and u"✅" not in message.text:
        if message.text != user.first_act:
            find_actor(bot, message, user)
        else:
            dict_phr = messages["same_act"]
            bot.send_message(
                message.chat.id, dict_phr[user.language], reply_markup=hide_markup)

    # Подтверждение имени второго актера
    if user.expected_cmd == "confirm_actor2":
        if u"🔥" in message.text:
            user.expected_cmd = "find_link"
        elif u"🔙" in message.text:
            user.expected_cmd = "second_actor"
            user.second_act = "None"
        else:
            return

        user.save()
        dict_phr = messages[user.expected_cmd]
        bot.send_message(
            message.chat.id, dict_phr[user.language], reply_markup=hide_markup)

    # Поиск связи
    if user.expected_cmd == "find_link":
        find_link(bot, message, user, user.first_act, user.second_act)
        user.expected_cmd = "try_more"
        user.save()

    # Вывод сообщения после поиска связи
    if user.expected_cmd == "try_more":
        if u"⏪" in message.text:
            user.expected_cmd = "main_menu"
        elif u"⚡" in message.text:
            user.expected_cmd = "second_actor"
        else:
            return

        user.save()
        dict_phr = messages[user.expected_cmd]

        if user.expected_cmd == "main_menu":
            dict_menu = messages["menu_phr"]
            send_msg(bot, message,
                     dict_menu[user.language], dict_phr[user.language])
        else:
            name = pars_name(message.text)
            user.first_act = name
            user.second_act = "None"
            user.save()
            bot.send_message(
                message.chat.id, dict_phr[user.language], reply_markup=hide_markup)
