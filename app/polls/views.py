# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .funcs import send_msg, change_lang
from .config import TOKEN, lang, messages
from core.models import User
from .main import main_func
import json
import telebot
from telebot import types

hide_markup = types.ReplyKeyboardRemove(selective=False)
bot = telebot.TeleBot(TOKEN)


@csrf_exempt
def event(request):
    json_list = json.loads(request.body)
    update = telebot.types.Update.de_json(json_list)
    try:
        bot.process_new_messages([update.message])
    except:
        bot.process_new_callback_query([update.callback_query])
    return HttpResponse()


@bot.message_handler(commands=["start"])
def choose_lang(message):
    login_usr = message.from_user.username
    if not User.objects.filter(login=login_usr):
        send_msg(bot, message,
                 "💡 Select your preferred language / Выберите Ваш язык", *lang)
        reg_info = User.objects.create(login=login_usr, language="ru")
        reg_info.save()


@bot.message_handler(commands=["help"])
def help_message(message):
    user = User.objects.get(login=message.from_user.username)
    dict_phr = messages["help_info"]
    bot.send_message(message.chat.id, dict_phr[user.language])


@bot.message_handler(commands=["lang"])
def help_message(message):
    user = User.objects.get(login=message.from_user.username)
    user.expected_cmd = "language"
    user.save()
    send_msg(bot, message,
             "💡 Select your preferred language / Выберите Ваш язык", *lang)


@bot.message_handler(commands=["devs"])
def devs_info(message):
    user = User.objects.get(login=message.from_user.username)
    dict_phr = messages["devs_info"]
    bot.send_message(message.chat.id, dict_phr[user.language])


@bot.message_handler(content_types=["text"])
def main(message):
    main_func(bot, message)
