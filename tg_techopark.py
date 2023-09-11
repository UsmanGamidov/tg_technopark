import telebot as tg
from telebot import types
import requests
import json
from email_validate import validate, validate_or_fail
import re
import os
from datetime import datetime, timedelta
from api import *

bot = tg.TeleBot(tg_api)
admin_id = adminid
all_information = {}


# Получение токена
def get_token(message):
    try:
        url = "https://api.moyklass.com/v1/company/auth/getToken"

        payload = json.dumps({
            "apiKey": token_myclass
        })
        headers = {
            'Content-Type': 'application/json'
        }

        accessToken = requests.request("POST", url, headers=headers, data=payload)
        accessToken_py = json.loads(accessToken.text)

        return accessToken_py['accessToken']
    except BaseException as e:
        print(e)
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте позже")
        bot.send_message(admin_id, f"Что-то пошло не так, попробуйте позже, {e}")


# Наименование всех групп
def all_name_groups(message):
    try:
        all_name_groups = set()

        url = "https://api.moyklass.com/v1/company/courses?includeClasses=true"

        payload = {}
        headers = {
            'x-access-token': get_token(message)
        }

        response_all_gr = requests.request("GET", url, headers=headers, data=payload)
        response_all_gr_py = json.loads(response_all_gr.text)

        for i in range(1, len(response_all_gr_py)):
            for j in range(len(response_all_gr_py[i]["classes"])):
                temp = response_all_gr_py[i]["classes"][j]['name'].split()
                all_name_groups.add(temp[0])

        return all_name_groups
    except BaseException as e:
        print(e)
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте позже")
        bot.send_message(admin_id, f"Что-то пошло не так, попробуйте позже, {e}")


# Все группы
def all_groups(message):
    try:
        all_name_groups = set()

        url = "https://api.moyklass.com/v1/company/courses?includeClasses=true"

        payload = {}
        headers = {
            'x-access-token': get_token(message)
        }

        response_all_gr = requests.request("GET", url, headers=headers, data=payload)
        response_all_gr_py = json.loads(response_all_gr.text)

        for i in range(1, len(response_all_gr_py)):
            for j in range(len(response_all_gr_py[i]["classes"])):
                temp = response_all_gr_py[i]["classes"][j]['name'].split()
                try:
                    if temp[3] == 'и':
                        all_name_groups.add(
                            temp[0] + ' ' + temp[1] + ' ' + temp[2] + ' ' + temp[4] + ' ' + temp[6] + ' ' + temp[8])
                    else:
                        all_name_groups.add(temp[0] + ' ' + temp[1] + ' ' + temp[2] + ' ' + temp[4])
                except:
                    all_name_groups.add(temp[0] + ' ' + temp[1])

        return all_name_groups
    except BaseException as e:
        print(e)
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте позже")
        bot.send_message(admin_id, f"Что-то пошло не так, попробуйте позже, {e}")


@bot.message_handler(commands=['info'])
def info(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        robotics = types.KeyboardButton('Робототехника')
        programming = types.KeyboardButton('Программирование')
        modeling = types.KeyboardButton('3 D моделирование')
        adobe_after = types.KeyboardButton('Создание анимации и видеоэффектов в Adobe After Effects')
        digital_art = types.KeyboardButton('Digital art')
        sites = types.KeyboardButton('Создание сайтов')
        bots = types.KeyboardButton('Боты на Python')
        blockchain = types.KeyboardButton('Технология блокчейн')
        html_css_javascript = types.KeyboardButton('Frontend-разработчик: сайты на HTML/CSS/JavaScript')
        markup.add(robotics, programming, modeling, adobe_after, digital_art,
                   sites, bots, blockchain, html_css_javascript)
        msg = bot.send_message(message.chat.id, 'Выберите направление про которое хотите узнать дополнительную '
                                                'информацию(из предоставленных вариантов)',
                               reply_markup=markup)
        bot.register_next_step_handler(msg, direction)
    except BaseException as e:
        print(e)
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте позже")
        bot.send_message(admin_id, f"Что-то пошло не так, попробуйте позже, {e}")


def second_info(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        robotics = types.KeyboardButton('Робототехника')
        programming = types.KeyboardButton('Программирование')
        modeling = types.KeyboardButton('3 D моделирование')
        adobe_after = types.KeyboardButton('Создание анимации и видеоэффектов в Adobe After Effects')
        digital_art = types.KeyboardButton('Digital art')
        sites = types.KeyboardButton('Создание сайтов')
        bots = types.KeyboardButton('Боты на Python')
        blockchain = types.KeyboardButton('Технология блокчейн')
        html_css_javascript = types.KeyboardButton('Frontend-разработчик: сайты на HTML/CSS/JavaScript')
        markup.add(robotics, programming, modeling, adobe_after, digital_art,
                   sites, bots, blockchain, html_css_javascript)
        msg = bot.send_message(message.chat.id, 'Если желает е можете узнать и про другие направления'
                                                'информацию(из предоставленных вариантов)',
                               reply_markup=markup)
        bot.register_next_step_handler(msg, direction)
    except BaseException as e:
        print(e)
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте позже")
        bot.send_message(admin_id, f"Что-то пошло не так, попробуйте позже, {e}")


def direction(message):
    try:
        if message.text != '/start':
            if message.text != '/application':
                if message.text != '/info':
                    if message.text == 'Робототехника':
                        photo = 'https://abakus-center.ru/img/blog/robototehnika-1.jpg'
                        bot.send_photo(message.chat.id, photo,
                                       caption='Робототехника — прикладная наука, занимающаяся разработкой '
                                               'автоматизированных технических систем и являющаяся важнейшей технической '
                                               'основой развития производства.',
                                       reply_markup=types.ReplyKeyboardRemove())
                        second_info(message)
                    elif message.text == 'Программирование':
                        photo = 'https://timeweb.com/media/articles/0001/08/thumb_7309_articles_standart.jpeg'
                        bot.send_photo(message.chat.id, photo,
                                       caption='Программирование — процесс создания компьютерных программ. По выражению '
                                               'одногоиз основателей языков программирования Никлауса Вирта «Программы '
                                               '= алгоритмы + структуры данных».Программирование основывается на '
                                               'использовании языков программирования, на которых записываются исходные '
                                               'тексты программ.',
                                       reply_markup=types.ReplyKeyboardRemove())
                        second_info(message)
                    elif message.text == '3 D моделирование':
                        photo = 'https://websoftex.ru/wp-content/uploads/2019/09/1563523359_3d-model-min-938x576.png'
                        bot.send_photo(message.chat.id, photo,
                                       caption='3D-моделирование — процесс создания трёхмерной модели объекта. Задача '
                                               '3D-моделирования — разработать зрительный объёмный образ желаемого объекта.'
                                               'При этом модель может как соответствовать объектам из реального мира '
                                               '(автомобили, здания, ураган, астероид), так и быть полностью абстрактной '
                                               '(проекция четырёхмерного фрактала).',
                                       reply_markup=types.ReplyKeyboardRemove())
                        second_info(message)
                    elif message.text == 'Создание анимации и видеоэффектов в Adobe After Effects':
                        photo = 'https://helpx.adobe.com/content/dam/help/images/en/keyboardshortcut.png'
                        bot.send_photo(message.chat.id, photo,
                                       caption='Создание анимации и видеоэффектов в Adobe After Effects - Широко '
                                               'применяется в обработке отснятого видеоматериала (цветокоррекция, '
                                               'постпродакшн), при создании рекламных роликов, музыкальных клипов, в '
                                               'производстве анимации (для телевидения и web), титров для художественных '
                                               'и телевизионных фильмов, а также для целого ряда других задач, в '
                                               'которых требуется использование цифровых ...',
                                       reply_markup=types.ReplyKeyboardRemove())
                        second_info(message)
                    elif message.text == 'Digital art':
                        photo = 'https://www.vectornator.io/blog/content/images/2022/12/Cover-history-and-' \
                                'future-of-digital-art.jpg'
                        bot.send_photo(message.chat.id, photo,
                                       caption='Компьютерное искусство (Digital art), а также цифровое искусство, '
                                               'диджитальное искусство — направление в медиаискусстве, основанное на '
                                               'использовании информационных (компьютерных) технологий, результатом '
                                               'являются художественные произведения в цифровой форме.',
                                       reply_markup=types.ReplyKeyboardRemove())
                        second_info(message)
                    elif message.text == 'Создание сайтов':
                        photo = 'https://i0.wp.com/levashove.ru/wp-content/uploads/2019/03/wikipedia-tools-alternatives.jpg'
                        bot.send_photo(message.chat.id, photo,
                                       caption='Веб-разработка — процесс создания веб-сайта или веб-приложения. '
                                               'Основными этапами процесса являются веб-дизайн, вёрстка страниц, '
                                               'программирование на стороне клиента и сервера, а также '
                                               'конфигурирование веб-сервера.',
                                       reply_markup=types.ReplyKeyboardRemove())
                        second_info(message)
                    elif message.text == 'Боты на Python':
                        photo = 'https://yar.coddyschool.com/upload/iblock/1ef/bots_min.png'
                        bot.send_photo(message.chat.id, photo,
                                       caption='Бот — специальная программа для совершения различных рутинных операций.',
                                       reply_markup=types.ReplyKeyboardRemove())
                        second_info(message)
                    elif message.text == 'Технология блокчейн':
                        photo = 'https://dit.urfu.ru/fileadmin/user_upload/site_15560/blog/BA.jpg'
                        bot.send_photo(message.chat.id, photo,
                                       caption='Блокчейн — выстроенная по определённым правилам непрерывная '
                                               'последовательная цепочка блоков (связный список), содержащих информацию. '
                                               'Связь между блоками обеспечивается не только нумерацией, но и тем, что '
                                               'каждый блок содержит свою собственную хеш-сумму и хеш-сумму предыдущего '
                                               'блока. Изменение любой информации в блоке изменит его хеш-сумму. '
                                               'Чтобы соответствовать правилам построения цепочки, изменения хеш-суммы '
                                               'нужно будет записать в следующий блок, что вызовет изменения уже его '
                                               'собственной хеш-суммы. При этом предыдущие блоки не затрагиваются. Если '
                                               'изменяемый блок последний в цепочке, то внесение изменений может не '
                                               'потребовать существенных усилий. Но если после изменяемого блока уже '
                                               'сформировано продолжение, то изменение может оказаться крайне трудоёмким '
                                               'процессом. Дело в том, что обычно копии цепочек блоков хранятся на '
                                               'множестве разных компьютеров независимо друг от друга.',
                                       reply_markup=types.ReplyKeyboardRemove())
                        second_info(message)
                    elif message.text == 'Frontend-разработчик: сайты на HTML/CSS/JavaScript':
                        photo = 'https://avatars.dzeninfra.ru/get-zen_doc/167204/pub_598a74d69d5cb3f1b5db4b9a_' \
                                '598a757f256d5cf399979348/scale_1200'
                        bot.send_photo(message.chat.id, photo,
                                       caption='Фронтенд (англ. frontend) — презентационная часть информационной или '
                                               'программной системы, её пользовательский интерфейс и связанные с ним '
                                               'компоненты; применяется в соотношении с базисной частью системы, её '
                                               'внутренней реализацией, называемой в этом случае бэкендом (англ. backend).',
                                       reply_markup=types.ReplyKeyboardRemove())
                        second_info(message)
                else:
                    info(message)
            else:
                application(message)
        else:
            start(message)
    except BaseException as e:
        print(e)
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте позже")
        bot.send_message(admin_id, f"Что-то пошло не так, попробуйте позже, {e}")


@bot.message_handler(commands=['help', 'start'])
def start(message):
    try:
        if message.from_user.last_name:
            mess = f'Здравствуйте, *{message.from_user.first_name} {message.from_user.last_name}*'
        else:
            mess = f'Здравствуйте, *{message.from_user.first_name}*'
        bot.send_message(message.chat.id, f' {mess} !\n'
                                          ' Я TechnoParkBot, если хотите узнать информацию про направления нажмите '
                                          '"/info", для отправки заявления введите команду '
                                          '"/application" и как только сможет администратор с вами свяжется',
                         parse_mode='Markdown', reply_markup=types.ReplyKeyboardRemove())
    except BaseException as e:
        print(e)
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте позже")
        bot.send_message(admin_id, f"Что-то пошло не так, попробуйте позже, {e}")


@bot.message_handler(commands=['application'])
def application(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        answer = types.KeyboardButton('Прекратить')
        markup.add(answer)
        msg = bot.send_message(message.chat.id, 'ФИО родителя(полностью)<b>*</b>', parse_mode='html',
                               reply_markup=markup)
        bot.register_next_step_handler(msg, name_of_the_parent)
    except BaseException as e:
        print(e)
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте позже")
        bot.send_message(admin_id, f"Что-то пошло не так, попробуйте позже, {e}")


def name_of_the_parent(message):
    try:
        text = message.text.split(' ')
        if message.text != '/application':
            if message.text != '/start':
                if message.text != '/info':
                    if message.text != 'Прекратить':
                        if len(text) == 3 or len(text) == 2:
                            all_information["ФИО родителя"] = message.text
                            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                            answer = types.KeyboardButton('Прекратить')
                            markup.add(answer)
                            msg = bot.send_message(message.chat.id, 'ФИО ребенка(полностью)<b>*</b>', parse_mode='html',
                                                   reply_markup=markup)
                            bot.register_next_step_handler(msg, children)
                        else:
                            bot.send_message(message.chat.id, 'Вы ввели неправильные данные')
                            application(message)
                    else:
                        bot.send_message(message.chat.id, 'Удачки', reply_markup=types.ReplyKeyboardRemove())
                else:
                    info(message)
            else:
                start(message)
        else:
            application(message)
    except BaseException as e:
        print(e)
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте позже")
        bot.send_message(admin_id, f"Что-то пошло не так, попробуйте позже, {e}")


def name_of_the_children(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        answer = types.KeyboardButton('Прекратить')
        markup.add(answer)
        msg = bot.send_message(message.chat.id, 'ФИО ребенка(полностью)<b>*</b>', parse_mode='html',
                               reply_markup=markup)
        bot.register_next_step_handler(msg, children)
    except BaseException as e:
        print(e)
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте позже")
        bot.send_message(admin_id, f"Что-то пошло не так, попробуйте позже, {e}")


def children(message):
    try:
        text = message.text.split(' ')
        if message.text != '/application':
            if message.text != '/start':
                if message.text != '/info':
                    if message.text != 'Прекратить':
                        if len(text) == 3 or len(text) == 2:
                            all_information["ФИО ребенка"] = message.text
                            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                            answer = types.KeyboardButton('Прекратить')
                            markup.add(answer)
                            msg = bot.send_message(message.chat.id, 'Электронная почта', parse_mode='html',
                                                   reply_markup=markup)
                            bot.register_next_step_handler(msg, email)
                        else:
                            bot.send_message(message.chat.id, 'Вы ввели неправильные данные')
                            name_of_the_children(message)
                    else:
                        bot.send_message(message.chat.id, 'Удачки', reply_markup=types.ReplyKeyboardRemove())
                else:
                    info(message)
            else:
                start(message)
        else:
            application(message)
    except BaseException as e:
        print(e)
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте позже")
        bot.send_message(admin_id, f"Что-то пошло не так, попробуйте позже, {e}")


def email_check(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        answer = types.KeyboardButton('Прекратить')
        markup.add(answer)
        msg = bot.send_message(message.chat.id, 'Электронная почта', parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(msg, email)
    except BaseException as e:
        print(e)
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте позже")
        bot.send_message(admin_id, f"Что-то пошло не так, попробуйте позже, {e}")


def email(message):
    try:
        if message.text != '/application':
            if message.text != '/start':
                if message.text != '/info':
                    if message.text != 'Прекратить':
                        email_validate = validate(
                            email_address=message.text,
                            check_format=True,
                            check_blacklist=True,
                            check_dns=True,
                            dns_timeout=10,
                            check_smtp=True,
                            smtp_timeout=10,
                            smtp_debug=False)
                        if email_validate:
                            all_information['email'] = message.text
                            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                            answer = types.KeyboardButton('Прекратить')
                            markup.add(answer)
                            msg = bot.send_message(message.chat.id, 'Номер телефона родителя<b>*</b>',
                                                   parse_mode='html',
                                                   reply_markup=markup)
                            bot.register_next_step_handler(msg, date_birth)
                        else:
                            bot.send_message(message.chat.id, 'Проверте верна ли введена почта')
                            email_check(message)
                    else:
                        bot.send_message(message.chat.id, 'Удачки', reply_markup=types.ReplyKeyboardRemove())
                else:
                    info(message)
            else:
                start(message)
        else:
            application(message)
    except BaseException as e:
        print(e)
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте позже")
        bot.send_message(admin_id, f"Что-то пошло не так, попробуйте позже, {e}")


def parent_number(message):
    try:
        msg = bot.send_message(message.chat.id, 'Номер телефона родителя<b>*</b>', parse_mode='html')
        bot.register_next_step_handler(msg, date_birth)
    except BaseException as e:
        print(e)
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте позже")
        bot.send_message(admin_id, f"Что-то пошло не так, попробуйте позже, {e}")


def date_birth(message):
    try:
        if message.text != '/application':
            if message.text != '/start':
                if message.text != '/info':
                    if message.text != 'Прекратить':
                        result = re.match(
                            r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$',
                            message.text)
                        if result:
                            all_information["Номер телефона родителя"] = message.text
                            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                            answer = types.KeyboardButton('Прекратить')
                            markup.add(answer)
                            msg = bot.send_message(message.chat.id, 'Возраст ребенка<b>*</b>', parse_mode='html',
                                                   reply_markup=markup)
                            bot.register_next_step_handler(msg, age_child1)
                        else:
                            bot.send_message(message.chat.id, 'Вы ввели неправильные данные')
                            parent_number(message)
                    else:
                        bot.send_message(message.chat.id, 'Удачки', reply_markup=types.ReplyKeyboardRemove())
                else:
                    info(message)
            else:
                start(message)
        else:
            application(message)
    except BaseException as e:
        print(e)
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте позже")
        bot.send_message(admin_id, f"Что-то пошло не так, попробуйте позже, {e}")


def age_child(message):
    try:
        msg = bot.send_message(message.chat.id, 'Возраст ребенка<b>*</b>', parse_mode='html')
        bot.register_next_step_handler(msg, age_child1)
    except BaseException as e:
        print(e)
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте позже")
        bot.send_message(admin_id, f"Что-то пошло не так, попробуйте позже, {e}")


def age_child1(message):
    try:
        age = message.text
        if message.text != '/application':
            if message.text != '/start':
                if message.text != '/info':
                    if message.text != 'Прекратить':
                        if age.isdigit() and int(age) < 70:
                            if int(age) >= 6:
                                all_information["Возраст ребенка"] = message.text
                                markup = types.InlineKeyboardMarkup(row_width=1)
                                for i in all_name_groups(message):
                                    callback_button = types.InlineKeyboardButton(i, callback_data=i)
                                    markup.add(callback_button)
                                bot.send_message(message.chat.id, "Программа обучения", reply_markup=markup)
                            else:
                                bot.send_message(message.chat.id, 'Ваш ребенок слишком мал')
                        else:
                            bot.send_message(message.chat.id, 'Вы ввели неправильные данные')
                            age_child(message)
                    else:
                        bot.delete_message(message.chat.id, message.message_id - 0)
                        bot.send_message(message.chat.id, 'Удачки', reply_markup=types.ReplyKeyboardRemove())
                else:
                    info(message)
            else:
                start(message)
        else:
            application(message)
    except BaseException as e:
        print(e)
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте позже")
        bot.send_message(admin_id, f"Что-то пошло не так, попробуйте позже {e}")


@bot.callback_query_handler(func=lambda call: True)
def call_back_main(call):
    try:
        for i in all_name_groups(call.message):
            if call.data == i:
                all_information["Программа обучения"] = i
                new_program(call.message, i)
        for i in all_groups(call.message):
            temp = i.split()
            if call.data == temp[0] + '' + temp[1]:
                all_information["День недели"] = temp[1]
                new_program_time(call.message, temp)
                break
        for i in all_groups(call.message):
            temp = i.split()
            if len(temp) == 6:
                if call.data == temp[0] + ' ' + temp[1] + ' ' + temp[2]:
                    all_information['Время'] = f'{temp[2]} группа: {temp[4]}'
                    confidentiality(call.message)
                elif call.data == temp[0] + ' ' + temp[1] + ' ' + temp[3]:
                    all_information['Время'] = f'{temp[3]} группа: {temp[5]}'
                    confidentiality(call.message)
            else:
                if call.data == temp[0] + ' ' + temp[1] + ' ' + temp[2]:
                    all_information['Время'] = f'{temp[2]} группа: {temp[3]}'
                    confidentiality(call.message)
        if call.data == "yes_confidentiality":
            if call.message.text != 'Прекратить':
                markup = types.InlineKeyboardMarkup(row_width=1)
                fio = all_information["ФИО родителя"]
                accept = types.InlineKeyboardButton('Принять заявку', callback_data='!' + fio)
                with open(f'/tg_techno/main/application/{fio}.txt', 'w', encoding='utf-8') as f:
                    f.write('\n'.join(list(all_information.values())) + '\n')
                    f.write(call.message.chat.first_name + '\n')
                    f.write(call.message.chat.username + '\n')
                markup.add(accept)
                bot.send_message(admin_id, f"Поступила заявка от *{call.message.chat.first_name}* ! \n"
                                           f"Его username = @{call.message.chat.username} \n"
                                           f"Заявка: \n"
                                           f"ФИО родителя: *{fio}* \n"
                                           f"ФИО ребенка: *{all_information['ФИО ребенка']}* \n"
                                           f"email: *{all_information['email']}* \n"
                                           f"Номер родителя: *{all_information['Номер телефона родителя']}* \n"
                                           f"Возраст ребенка: *{all_information['Возраст ребенка']}* \n"
                                           f"Программа обучения: *{all_information['Программа обучения']}*\n"
                                           f"День недели: *{all_information['День недели']}* \n"
                                           f"Время: *{all_information['Время']}* \n",
                                 parse_mode='Markdown', reply_markup=markup)
                bot.delete_message(call.message.chat.id, call.message.message_id - 0)
                bot.send_message(call.message.chat.id, f'Спасибо ваша заявка принята. В ближайшее время вам напишет '
                                                       f'администратор и уточнит все детали обучения\n'
                                                       f'Ваша заявка: \n'
                                                       f"ФИО родителя: *{all_information['ФИО родителя']}* \n"
                                                       f"ФИО ребенка: *{all_information['ФИО ребенка']}* \n"
                                                       f"email: *{all_information['email']}* \n"
                                                       f"Номер родителя: *{all_information['Номер телефона родителя']}* \n"
                                                       f"Возраст ребенка: *{all_information['Возраст ребенка']}* \n"
                                                       f"Программа обучения: *{all_information['Программа обучения']}*\n"
                                                       f"День недели: *{all_information['День недели']}* \n"
                                                       f"Время: *{all_information['Время']}* \n",
                                 parse_mode='Markdown', reply_markup=types.ReplyKeyboardRemove())
            else:
                bot.delete_message(call.message.chat.id, call.message.message_id - 0)
                bot.send_message(call.message.chat.id, 'Удачки', reply_markup=types.ReplyKeyboardRemove())
        elif '!' in call.data:
            accept_fuc(call.message, call.data[1:])
        elif call.data == "no_confidentiality":
            bot.delete_message(call.message.chat.id, call.message.message_id - 0)
            bot.send_message(call.message.chat.id, "Удачи", parse_mode='html')
    except BaseException as e:
        print(e)
        bot.send_message(call.message.chat.id, "Что-то пошло не так, попробуйте позже")
        bot.send_message(admin_id, f"Что-то пошло не так, попробуйте позже {e}")


def new_program(message, name_group):
    try:
        if message.text != '/application':
            if message.text != '/start':
                if message.text != '/info':
                    if message.text != 'Прекратить':
                        markup = types.InlineKeyboardMarkup(row_width=1)
                        temp_check_list = []
                        for i in all_groups(message):
                            temp = i.split()
                            if name_group == temp[0]:
                                if temp[1] not in temp_check_list:
                                    temp_check_list.append(temp[1])
                                    callback = types.InlineKeyboardButton(temp[1], callback_data=temp[0] + '' + temp[1])
                                    markup.add(callback)
                        bot.send_message(message.chat.id, "В какой день вам удобно?", reply_markup=markup)
                        bot.delete_message(message.chat.id, message.message_id - 0)
                    else:
                        bot.delete_message(message.chat.id, message.message_id - 0)
                        bot.send_message(message.chat.id, 'Удачки', reply_markup=types.ReplyKeyboardRemove())
                else:
                    info(message)
            else:
                start(message)
        else:
            application(message)
    except BaseException as e:
        print(e)
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте позже")
        bot.send_message(admin_id, f"Что-то пошло не так, попробуйте позже {e}")


def new_program_time(message, all_info_group):
    try:
        if message.text != '/application':
            if message.text != '/start':
                if message.text != '/info':
                    if message.text != 'Прекратить':
                        markup = types.InlineKeyboardMarkup(row_width=1)
                        for i in all_groups(message):
                            temp = i.split()
                            if len(temp) == 6:
                                if temp[0] == all_info_group[0] and temp[1] == all_info_group[1]:
                                    callback = types.InlineKeyboardButton(f'{temp[2]} группа: {temp[4]}',
                                                                          callback_data=temp[0] + ' ' + temp[1] + ' ' +
                                                                                        temp[2])
                                    callback_2 = types.InlineKeyboardButton(f'{temp[3]} группа: {temp[5]}',
                                                                            callback_data=temp[0] + ' ' + temp[
                                                                                1] + ' ' +
                                                                                          temp[3])
                                    markup.add(callback, callback_2)
                            elif len(temp) == 4:
                                if temp[0] == all_info_group[0] and temp[1] == all_info_group[1]:
                                    callback = types.InlineKeyboardButton(f'{temp[2]} группа: {temp[3]}',
                                                                          callback_data=temp[0] + ' ' + temp[1] + ' ' +
                                                                                        temp[2])
                                    markup.add(callback)
                        bot.delete_message(message.chat.id, message.message_id - 0)
                        bot.send_message(message.chat.id, "В какую группу вам удобно?(урок: 90мин)",
                                         reply_markup=markup)
                    else:
                        bot.delete_message(message.chat.id, message.message_id - 0)
                        bot.send_message(message.chat.id, 'Удачки', reply_markup=types.ReplyKeyboardRemove())
                else:
                    info(message)
            else:
                start(message)
        else:
            application(message)
    except BaseException as e:
        print(e)
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте позже")
        bot.send_message(admin_id, f"Что-то пошло не так, попробуйте позже {e}")


def accept_fuc(message, fio):
    # try:
        temp_info = []
        with open(f'/tg_techno/main/application/{fio}.txt', 'r', encoding='utf-8') as f:
            for i in f:
                temp_info.append(i.split('\n')[0])

        # Списко учеников

        url = "https://api.moyklass.com/v1/company/users"

        payload = {}
        headers = {
            'x-access-token': get_token(message)
        }

        response_students = requests.request("GET", url, headers=headers, data=payload)
        response_students_py = json.loads(response_students.text)
        students_list = []

        for i in range(0, len(response_students_py['users'])):
            students_list.append(response_students_py['users'][i]['name'])

        # Добовление ученика

        if temp_info[1] not in students_list:
            url = "https://api.moyklass.com/v1/company/users"

            payload = json.dumps({
                "name": temp_info[1],
                "email": temp_info[2],
                "phone": temp_info[3],
                "advSourceId": 129625,
                "createSourceId": 1,
                "clientStateId": 96785,
                "filials": [
                    23686
                ],
                "responsibles": [
                    106149
                ],
                "attributes": [
                    {
                        "attributeId": 2,
                        "value": temp_info[0]
                    },
                    {
                        "attributeId": 14,
                        "value": "true"
                    }
                ],
            })
            headers = {
                'x-access-token': get_token(message),
                'Content-Type': 'application/json'
            }

            response_add_in_group = requests.request("POST", url, headers=headers, data=payload)
            response_add_in_group_py = json.loads(response_add_in_group.text)
            print(response_add_in_group_py)

            # Добавлени в группу

            # Получение id группу
            url = "https://api.moyklass.com/v1/company/courses?includeClasses=true"

            payload = {}
            headers = {
                'x-access-token': get_token(message)
            }

            response_id_group = requests.request("GET", url, headers=headers, data=payload)
            response_id_group_py = json.loads(response_id_group.text)

            id_gruppa = 0
            all_name_groups = set()
            for i in range(1, len(response_id_group_py)):
                for j in range(len(response_id_group_py[i]["classes"])):
                    temp = response_id_group_py[i]["classes"][j]['name'].split()
                    try:
                        if temp[3] == 'и':
                            temp_element = temp[0] + ' ' + temp[1] + ' ' + temp[2] + ' ' + temp[4] + ' ' + temp[
                                6] + ' ' + \
                                           temp[8]
                            all_name_groups.add(temp_element)
                        else:
                            temp_element = temp[0] + ' ' + temp[1] + ' ' + temp[2] + ' ' + temp[4]
                            all_name_groups.add(temp_element)
                    except:
                        temp_element = temp[0] + ' ' + temp[1]
                        all_name_groups.add(temp_element)
                    temp_element_ls = temp_element.split()
                    if temp_element_ls[0] == temp_info[5] and temp_element_ls[1] == temp_info[6] \
                            and f'{temp_element_ls[2]} группа: {temp_element_ls[3]}' == temp_info[7]:
                        id_gruppa = response_id_group_py[i]["classes"][j]['id']

            url = "https://api.moyklass.com/v1/company/joins"
            print(1)
            payload = json.dumps({
                "userId": response_add_in_group_py['id'],
                "classId": id_gruppa,
                "price": 0,
                "statusId": 42106,
                "autoJoin": True,
                "managerId": 106149,
                "advSourceId": 129626,
                "createSourceId": 1,
                "params": {
                    "invoice": {
                        "autoCreate": True,
                        "createRule": "setStatus",
                        "joinStateId": [],
                        "payDateDays": 3,
                        "payDateType": "retative"
                    }
                }
            })
            print(2)
            headers = {
                'Content-Type': 'application/json',
                'x-access-token': get_token(message)
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            bot.edit_message_text(chat_id=admin_id, message_id=message.message_id, text=
            f'*Заявка успешно ПРИЯНЯТА ✅❗✅❗✅* \n'
            f'Поступила заявка от *{temp_info[8]}* ! \n'
            f'Его username = @{temp_info[9]} \n'
            f'Заявка: \n'
            f'ФИО родителя: *{temp_info[0]}* \n'
            f'ФИО ребенка: *{temp_info[1]}* \n'
            f'email: *{temp_info[2]}* \n'
            f'Номер родителя: *{temp_info[3]}* \n'
            f'Возраст ребенка: *{temp_info[4]}* \n'
            f'Программа обучения: *{temp_info[5]}*\n'
            f'День недели: *{temp_info[6]}* \n'
            f'Время: *{temp_info[7]}* \n', parse_mode='Markdown')
            os.remove(f'/tg_techno/main/application/{fio}.txt')
        else:
            bot.send_message(admin_id, 'Данный ребенок уже есть в базе')
            os.remove(f'/tg_techno/main/application/{fio}.txt')
    # except BaseException as e:
    #     print(e)
    #     print(1)
    #     bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте позже")
    #     bot.send_message(admin_id, f"Что-то пошло не так, попробуйте позже {e}")


def confidentiality(message):
    try:
        markup = types.InlineKeyboardMarkup()
        yes = types.InlineKeyboardButton('Да', callback_data='yes_confidentiality')
        no = types.InlineKeyboardButton('Нет', callback_data='no_confidentiality')
        markup.add(yes, no)
        bot.delete_message(message.chat.id, message.message_id - 0)
        bot.send_message(message.chat.id,
                         "Я внимательно ознакомился и согласен с Политикой", parse_mode='html', reply_markup=markup)
    except BaseException as e:
        print(e)
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте позже")
        bot.send_message(admin_id, f"Что-то пошло не так, попробуйте позже {e}")


@bot.message_handler(content_types=['text'])
def text(message):
    try:
        bot.send_message(message.chat.id, 'Вы хотите отправить Заявку?\nТогда нажмите сюда "/application"')
    except BaseException as e:
        print(e)
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте позже")
        bot.send_message(admin_id, f"Что-то пошло не так, попробуйте позже {e}")


bot.polling(none_stop=True)
