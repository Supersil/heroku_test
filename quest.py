import telebot
import config
import random
import time

from datetime import datetime
from telebot import types


bot = telebot.TeleBot(config.TOKEN)

logname = ''


def sendPic(task: int, path, chatId):
    pic = open(config.ResourcesPath + 'Task{}/'.format(task)
               + path, 'rb')
    bot.send_photo(chatId, pic)


def startQuest(chatId):
    markup = types.ReplyKeyboardRemove()
    bot.send_message(chatId, '''Поехали!
В этом задании тебе предстоит угадать названия трех мультиков, зашифрованных в эмодзи.
Одна картинка - один мультик🤪

Будь внимателен, друг! Все названия стостоят из двух слов.
''', parse_mode='html', reply_markup=markup)
    sendPic(1, '1.png', chatId)


def firstTaskComplete1(chatId):
    bot.send_message(chatId, 'Молодец! Осталось еще два мультика👍')
    sendPic(1, '2.png', chatId)


def firstTaskComplete2(chatId):
    bot.send_message(chatId, 'Ого! Ты явно хорошо разбираешься в мультиках🎓 Остался последний.\
')
    sendPic(1, '3.png', chatId)


def firstTaskComplete3(chatId):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("ВПЕРЁД")
    markup.add(item1)
    bot.send_message(chatId, '''\
Молодец! Следующее задание будет сложнее, но я уверена, что ты справишься😉
Если готов(а) продолжить нажми на кнопку ВПЕРЁД.
''', parse_mode='html', reply_markup=markup)


def firstTaskComplete4(chatId):
    markup = types.ReplyKeyboardRemove()
    bot.send_message(chatId, '''\
Нам встретилось целое облако цифр. Что же делать?😳
Чтобы пройти дальше, внимательно посмотри на картинку и найди все цифры, написанные зеленым цветом💚

Ответ на задание - сумма зеленых цифр😉.
''', parse_mode='html', reply_markup=markup)
    sendPic(2, 'nums.png', chatId)


def secondTaskComplete(chatId):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("ВПЕРЁД")
    markup.add(item1)
    bot.send_message(chatId, '''Ух ты! Здорово считаешь👍 Это правильный ответ.
Если готов(а) продолжить нажми на кнопку ВПЕРЁД.''', parse_mode='html', reply_markup=markup)


def secondTaskComplete2(chatId):
    markup = types.ReplyKeyboardRemove()
    bot.send_message(chatId, '''Для следующего задания тебе нужно включить звук🎧
Я перевернула песню известного персонажа мультика. Прослушай ее и угадай ИМЯ ГЕРОЯ.
В этом задании у тебя есть подсказка😉 Если хочешь ей воспользоваться, напиши в чат ПОДСКАЗКА.\
''', parse_mode='html', reply_markup=markup)
    audio = open(config.ResourcesPath + 'Task3/' + 'Maui_reverse.mp3', 'rb')
    bot.send_voice(chatId, audio)


def thirdTaskHint(chatId):
    bot.send_message(chatId, 'Могучий полубог, который поет песню про одно волшебное слово 🤫')


def thirdTaskComplete(chatId):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("ВПЕРЁД")
    markup.add(item1)
    audio = open(config.ResourcesPath + 'Task3/' + 'Maui_fragment.mp3', 'rb')
    bot.send_voice(chatId, audio)

    bot.send_message(chatId, '''Ты точно гений! Или скрываешь какую-то суперспособность😳 Верно, это песня Мауи из мультика "Моана"👏🏻 
Тебе осталось справиться с еще 2-мя заданиями.

Если готов(а) продолжить нажми на кнопку ВПЕРЁД.''', parse_mode='html', reply_markup=markup)


def thirdTaskComplete2(chatId):
    markup = types.ReplyKeyboardRemove()
    bot.send_message(chatId, '''
Следующее задание состоит из 4-х частей☝🏻
Внимательно посмотри на изображение ниже и напиши слово, которое обьединяет все три фрагмента на нем🔎\
''', parse_mode='html', reply_markup=markup)
    sendPic(4, '1.png', chatId)


def forthTaskComplete1(chatId):
    bot.send_message(chatId, 'Молодец!👍 У тебя отлично получается.')
    sendPic(4, '2.png', chatId)


def forthTaskComplete2(chatId):
    bot.send_message(chatId, 'Сказочный результат!👏🏻Справишься со следующей картинкой?')
    sendPic(4, '3.png', chatId)


def forthTaskComplete3(chatId):
    bot.send_message(chatId, 'Ого! Осталась всего одна картинка🤘')
    sendPic(4, '4.png', chatId)


def forthTaskComplete4(chatId):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("ВПЕРЁД")
    markup.add(item1)
    bot.send_message(chatId, '''Отличный результат! Мы на финишной прямой💪 Осталось последнее пятое задание. Готов(а) подурачиться?
Если твой ответ ДА, жми кнопку ВПЕРЁД🔥 ''', parse_mode='html', reply_markup=markup)


def forthTaskComplete5(chatId):
    markup = types.ReplyKeyboardRemove()
    bot.send_message(chatId, 'На картинке изображены 8 смайликов с разными \
эмоциями. Повтори три любые из них и пришли фотографии в чат 😉 3, 2, 1... \
Начали!', parse_mode='html', reply_markup=markup)
    sendPic(5, 'Smiles.png', chatId)


def goodFinal(chatId):
    markup = types.ReplyKeyboardRemove()
    bot.send_message(chatId, '''️ У меня еще много интересных программ для тебя😉
Квесты, квизы, игры online и авторские программы.
Больше информации о программах ТУСА ПУПСА здесь 👉🏽http://tusapupsa.ru/ ''',
                     parse_mode='html', reply_markup=markup)


def badFinal(chatId):
    markup = types.ReplyKeyboardRemove()
    bot.send_message(chatId, '''🙈Спасибо, что сообщил. 
    Напиши, пожалуйста @help_quiz_bot, что \
не понравилось. Это поможет квестам ТУСА ПУПСА стать лучше и интереснее😉''',
                     parse_mode='html', reply_markup=markup)
# ОТБИВКА НА ОБРАТНУЮ СВЯЗЬ
# Спасибо за обратную связь! Твое сообщение уже летит ко мне😉 

@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("НАЧАТЬ!")
    markup.add(item1)
    print(message.from_user.first_name)
    print(message.chat.id)
    # log = open(logname, 'w')
    # user = message.from_user.username
    # log.write("Username: " + (user if user is not None else "") + "\n")
    # user = message.from_user.first_name
    # log.write("First name: " + (user if user is not None else "") + "\n")
    # user = message.from_user.last_name
    # log.write("Last name: " + (user if user is not None else "") + "\n")
    # log.write("Time: " + datetime.now().strftime("%d%m%Y_%H%M%S"))
    # log.close()
    user = message.from_user.username
    adminMsg = ("Username: @" + (user if user is not None else "") + "\n")
    user = message.from_user.first_name
    adminMsg += ("First name: " + (user if user is not None else "") + "\n")
    user = message.from_user.last_name
    adminMsg += ("Last name: " + (user if user is not None else "") + "\n")
    adminMsg += ("ID: " + str(message.chat.id) + "\n")
    bot.send_message(config.adminId, adminMsg)

    day = int(cur.strftime("%d"))
    if config.lastClear != day:
        config.state = {}
        config.lastClear = day 
        bot.send_message(config.adminId, "База данных очищена.")

    bot.send_message(message.chat.id, "Привет, " + message.from_user.first_name
                     + "!\n" + '''
Ты в чате квиз-бота ТУСА ПУПСА😉

Меня зовут Марьяша, я ведущая игровой #тусапупса_online и автор этого квиза.
Друг, если тебе меньше 6-ти, то для прохождения квиза нам может понадобиться помощь родителей.

Если квиз перестал работать, или бот не принимает ответ в котором ты уверен - пиши помощнику @help_quiz_bot

Готов(а) начать игру? Жми 👉🏽НАЧАТЬ.

Удачи!
''', parse_mode='html', reply_markup=markup)
    config.state[message.chat.id] = 0


@bot.message_handler(content_types=['text'])
def text_answer(message):
    if not message.chat.id in config.state:
        return
    if config.state[message.chat.id] == 0:
        if message.chat.type == 'private':
            if message.text == 'НАЧАТЬ!':
                startQuest(message.chat.id)
                config.state[message.chat.id] = 1
                return

    elif config.state[message.chat.id] == 1:
        if message.chat.type == 'private':
            if message.text.lower() == 'холодное сердце':
                firstTaskComplete1(message.chat.id)
                config.state[message.chat.id] = 2
                return

    elif config.state[message.chat.id] == 2:
        if message.chat.type == 'private':
            if message.text.lower() == 'король лев':
                firstTaskComplete2(message.chat.id)
                config.state[message.chat.id] = 3
                return

    elif config.state[message.chat.id] == 3:
        if message.chat.type == 'private':
            if message.text.lower() == 'щенячий патруль':
                firstTaskComplete3(message.chat.id)
                config.state[message.chat.id] = 30
                return

    elif config.state[message.chat.id] == 30:
        if message.chat.type == 'private':
            if message.text.lower() == 'вперёд':
                firstTaskComplete4(message.chat.id)
                config.state[message.chat.id] = 4
                return

    elif config.state[message.chat.id] == 4:
        if message.chat.type == 'private':
            if message.text.lower() == '30':
                secondTaskComplete(message.chat.id)
                config.state[message.chat.id] = 40
                return

    elif config.state[message.chat.id] == 40:
        if message.chat.type == 'private':
            if message.text.lower() == 'вперёд':
                secondTaskComplete2(message.chat.id)
                config.state[message.chat.id] = 5
                return

    elif config.state[message.chat.id] == 5:
        if message.chat.type == 'private':
            if message.text.lower() == 'подсказка':
                thirdTaskHint(message.chat.id)
                return
            if message.text.lower() == 'мауи':
                thirdTaskComplete(message.chat.id)
                config.state[message.chat.id] = 50
                return

    elif config.state[message.chat.id] == 50:
        if message.chat.type == 'private':
            if message.text.lower() == 'вперёд':
                thirdTaskComplete2(message.chat.id)
                config.state[message.chat.id] = 6
                return

    elif config.state[message.chat.id] == 6:
        if message.chat.type == 'private':
            if message.text.lower() == 'погода':
                forthTaskComplete1(message.chat.id)
                config.state[message.chat.id] = 7
                return

    elif config.state[message.chat.id] == 7:
        if message.chat.type == 'private':
            if message.text.lower() == 'сказка':
                forthTaskComplete2(message.chat.id)
                config.state[message.chat.id] = 8
                return

    elif config.state[message.chat.id] == 8:
        if message.chat.type == 'private':
            if message.text.lower() == 'дождь':
                forthTaskComplete3(message.chat.id)
                config.state[message.chat.id] = 9
                return

    elif config.state[message.chat.id] == 9:
        if message.chat.type == 'private':
            if message.text.lower() == 'игрушка':
                forthTaskComplete4(message.chat.id)
                config.state[message.chat.id] = 90
                return

    elif config.state[message.chat.id] == 90:
        if message.chat.type == 'private':
            if message.text.lower() == 'вперёд':
                forthTaskComplete5(message.chat.id)
                config.state[message.chat.id] = 10
                return

    elif config.state[message.chat.id] == 13:
        if message.chat.type == 'private':
            adminMsg = "\n\nКвест пройден!!!\n"
            adminMsg += message.text
            user = message.from_user.username
            adminMsg += ("Username: @" + (user if user is not None else "") + "\n")
            user = message.from_user.first_name
            adminMsg += ("First name: " + (user if user is not None else "") + "\n")
            user = message.from_user.last_name
            adminMsg += ("Last name: " + (user if user is not None else "") + "\n")
            adminMsg += ("ID: " + str(message.chat.id) + "\n")
            bot.send_message(config.adminId, adminMsg)
            if message.text.lower() == 'классный квест!':
                goodFinal(message.chat.id)
                return
            if message.text.lower() == 'мне было скучно':
                badFinal(message.chat.id)
                return

    if message.text.lower() == 'сброс':
        welcome(message)
        return

    bot.send_message(message.chat.id, 'Это не совсем то, чего я жду. Попроси \
родителей проверить правильность 😢')


@bot.message_handler(content_types=['photo'])
def photo_answer(message):
    if not message.chat.id in config.state:
        return
    if config.state[message.chat.id] == 10:
        if message.chat.type == 'private':
            bot.send_message(message.chat.id, 'У тебя отлично получается! \
Оталось две фотографии.')
            config.state[message.chat.id] = 11
            return

    if config.state[message.chat.id] == 11:
        if message.chat.type == 'private':
            bot.send_message(message.chat.id, 'Вот это сходство! С нетерпением\
 жду третью фотографию ❤️')
            config.state[message.chat.id] = 12
            return

    if config.state[message.chat.id] == 12:
        if message.chat.type == 'private':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Классный квест!")
            item2 = types.KeyboardButton("Мне было скучно")
            markup.add(item1, item2)
            bot.send_message(message.chat.id, '🔥 Это было круто. У тебя \
отлично получилось справиться с разными заданиями👏 Тебе понравился квиз? Кликни на кнопку с подходящим вариантом.',
                             parse_mode='html', reply_markup=markup)
            config.state[message.chat.id] = 13
            return

    bot.send_message(message.chat.id, 'Это не совсем то, чего я жду. Попроси \
родителей проверить правильность ответа😢')


cur = datetime.now()
logname = cur.strftime("LOGS/%d%m%Y_%H%M%S") + ".log"

while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)
        # log = open(logname, 'w')
        # log.write("Exception " + datetime.now().strftime("%d%m%Y_%H%M%S"))
        # log.close()
        time.sleep(15)
        continue
