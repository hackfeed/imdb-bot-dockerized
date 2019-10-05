# -*- coding: utf-8 -*-

TOKEN = "INSERT_YOUR_TOKEN_HERE"

lang = [u"Русский", "English"]

bacon_info_ru = "🎬 Данный бот находит число Бейкона для любых двух актеров, " \
                "основываясь на открытой базе данных IMDb.\n\n" \
                "⁉ Что такое число Бейкона? https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon\n\n" \
                "📌 Доступные команды: \n" \
                "⚠️ /lang - изменение языка.\n" \
                "⚙️ /devs - информация о разработчиках."

bacon_info_en = "🎬 Find the Bacon Number for any actors in IMDb database.\n" \
                "⁉️ What's that? https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon\n\n" \
                "📌 Available commands: \n" \
                "⚠️ /lang - to change language.\n" \
                "⚙️ /devs - info about developers."

devs_ru = "📒 Бот был разработан командой студентов первого (ныне уже второго) курса, " \
    "учащихся в МГТУ им. Баумана, каф. «Программная инженерия» (ИУ7)\n\n" \
    "🖍 Основной алгоритм поиска, работы с данными и т.д написан на языке СИ.\n\n" \
    "🐍 Алгоритм бота написан на языке Python, с использованием фреймворка " \
    "Django, библиотек IMDbPy и Telebot.\n\n" \
    "🛠 Разработчики: \n\n" \
    "🔱 Павел Пересторонин @Justarone\n✅ Сергей Кононенко @hackfeed\n" \
    "🤠 Алексей Романов @mrrvz1\n✅ Влад Кривозубов @dliosh\n" \
    "✅ Любовь Прохорова @lyubaxapro\n✅ Павел Топорков @ptrk09\n\n" \
    "📮 Локализация:\n🐲 Михаил Нитенко @VASYA_VAN"

devs_en = "📒 Бот был разработан командой студентов первого (ныне уже второго) курса, " \
    "учащихся в МГТУ им. Баумана, каф. «Программная инженерия» (ИУ7)\n\n" \
    "🖍 Основной алгоритм поиска, работы с данными и т.д написан на языке СИ.\n\n" \
    "🐍 Алгоритм бота написан на языке Python, с использованием фреймворка " \
    "Django, библиотек IMDbPy и Telebot.\n\n" \
    "🛠 Разработчики: \n\n" \
    "🔱 Павел Пересторонин @Justarone\n✅ Сергей Кононенко @hackfeed\n" \
    "🤠 Алексей Романов @mrrvz1\n✅ Влад Кривозубов @dliosh\n" \
    "✅ Любовь Прохорова @lyubaxapro\n✅ Павел Топорков @ptrk09\n\n" \
    "📮 Локализация:\n🐲 Михаил Нитенко @VASYA_VAN"


messages = {"language": {"en": "✅ Language selected successfully. Use /lang to change it.",
                         "ru": "✅ Язык успешно установлен. Используйте /lang для изменения языка."},

            "help_info": {"en": bacon_info_en,
                          "ru": bacon_info_ru},

            "main_menu": {"en": "⭐️ Find link",
                          "ru": u"⭐️ Найти связь"},

            "first_actor": {"en": "💬 Enter the name of the first actor: ",
                            "ru": "💬 Введите имя первого актера, с которым Вы хотите найти связь (на английском языке):"},

            "second_actor": {"en": "💬 Enter the name of the second actor:",
                             "ru": "💬 Введите имя второго актера, с которым Вы хотите найти связь (на английском языке):"},

            "confirm_actor": {"en": ["✅ Select", "🔙 Back"],
                              "ru": ["✅ Выбрать", "🔙 Назад"]},

            "confirm_actor2": {"en": ["🔥 Find connection between actors", "🔙 Back"],
                               "ru": ["🔥 Установить связь между актерами", "🔙 Назад"]},

            "find_link": {"en": "⏳ Finding connection. Please wait.",
                          "ru": "⏳ Поиск связи. Пожалуйста, подождите несколько секунд."},

            "last_films": {"en": "🎬 Latest movies: \n\n",
                           "ru": "🎬 Последние 10 фильмов: \n\n"},

            "no_man": {"en": "⚠ There is no such person in IMDb database. Please try again.",
                       "ru": "⚠ Такого человека нет в базе данных IMDb. Попробуйте еще раз."},

            "load": {"en": "⏳ Please wait, your request is being processed.",
                     "ru": "⏳ Ваш запрос обрабатывается. Пожалуйста, подождите несколько секунд."},

            "not_actor": {"en": "⛔ This person isn't an actor. Please try again.",
                          "ru": "⛔ Этот человек не является актером. Пожалуйста, попробуйте ещё раз."},

            "try_more": {"en": [u"⚡ Find other links for: ", "⏪ Main menu"],
                         "ru": [u"⚡ Найти другие связи для: ", "⏪ В главное меню"]},

            "same_act": {"en": "‼ You are trying to find a connection between the actor and himself. Please try again.",
                         "ru": "‼ Вы пытаетесь найти связь актера самого с собой. Пожалуйста, попробуйте еще раз."},

            "menu_phr": {"en": "📂 Main menu.",
                         "ru": u"📂 Вы были перемещены в главное меню."},

            "link_info": {"en": ["🎭 First actor: ", "\n🎭 Second actor: ", "🔥 *Bacon number*: ", " \n🌌 *Way*: "],
                          "ru": ["🎭 Первый актёр: ", "\n🎭 Второй актёр: ", "🔥 *Дистанция*: ", " \n🌌 *Путь*: "]},

            "err_info": {"en": "⛔ Something went wrong. Most likely this actor is not in our database. "
                               "Try again later.",
                         "ru": "⛔ Что-то пошло не так. Скорее всего, один из актеров ещё не внесён в нашу базу данных. "
                               "Пожалуйста, попробуйте позже."},

            "no_cnct": {"en": "🔒 Connection not found. Try changing one of the actors.",
                        "ru": "🔒 Связь не найдена. Попробуйте сменить одного из актеров."},

            "devs_info": {"en": devs_en,
                          "ru": devs_ru},
            }
