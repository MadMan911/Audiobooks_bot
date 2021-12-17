from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackContext  # python-telegram-bot-raw
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove  # python-telegram-bot
import telebot
from gtts import gTTS  # gTTS
import random  # import random # import sys # import wx # import pygame # import os
import re
import os

botToken = '5015096329:AAHqxoNdAEXjD6Y3lqaXZIFfNnC7OLTYV9U'
bot = telebot.TeleBot(botToken, parse_mode=None)


@bot.message_handler(commands=['start'])
def id_of_chat(message):
    '''
    функция возвращает idчата
    нужно, чтобы чможно было отправить пользователю файл с книгой
    '''
    chat_id = message.chat.id
    return (chat_id)


def converter_txt_str():  # конвертер txt в str   кнопка не нужна
    '''
    конвертирует txt в строку
    '''
    text = open(r'C:\audio_book\1.txt', encoding='utf-8').read()
    text1 = re.split(r'\n', text)
    result = ''
    for ch in text1:
        ch += ' '
        result += ch
    return result[:-1]


def converter_str_mp3():  # конвертер str в mp3    кнопка не нужна
    '''
    взаимодействует с функцией convert_txt_str
    озвучивает txt файл и создает mp3
    '''
    audio = r'C:\audio_book\1.mp3'  # поменять имя файла на входящее
    language = 'ru'
    sp = gTTS(text=converter_txt_str(), lang=language, slow=False)
    sp.save(audio)


def main_menu(update, context: CallbackContext):
    update.message.reply_text('Добро пожаловать в главное меню.\n',
                              reply_markup=markup_main_menu)  # клавиатура главное меню


def start(update, context: CallbackContext):
    '''
    Запуск бота
    '''
    update.message.reply_text('Привет! Я бот с аудиокнигами.\n'
                              'Для получения инструкций нажмите на кнопку /help.',
                              reply_markup=markup_start)


def guess_game(update, context: CallbackContext):
    '''
    маленькая игра
    чтобы выиграть, вам понадобятся:
    -сила
    -ловкость
    -везение
    шутка, везения будет достаточно
    '''
    update.message.reply_text('Правила игры:\n'
                              'Я загадываю цвет: Черный или белый.\n'
                              'Вы должны его угадать, для этого нажмите на кнопку /black - черный или /white - белый.\n'
                              'Для получения инструкций нажмите на кнопку "/help".\n'
                              'Для возвращения в главное меню нажмите на кнопку "/main".',
                              reply_markup=markup_guess_game)


def game_colour(update, context: CallbackContext):
    a = [1, 2]
    random.seed(version=2)
    a = random.choice(a)
    if a == 1:
        a = 'white'
    else:
        a = 'black'
    otv = update.message.text.split('/')
    if a in otv:
        update.message.reply_text('Поздравляю! Вы угадали(;\n'
                                  'Хотите сыграть еще раз? Тогда нажимайте на кнопки /black или /white, я могу поменять цвет, а могу оставить.\n'
                                  'Хотите почитать правила? Тогда нажимайте /game. \n'
                                  'Если больше не хотите играть, нажимайте на /help(помощь) или /main(главное меню).',
                                  reply_markup=markup_black_white)
    else:
        update.message.reply_text('К сожалению, вы не угадали);\n'
                                  'Хотите сыграть еще раз? Тогда нажимайте на кнопки /black или /white,я могу поменять цвет, а могу оставить.\n'
                                  'Хотите почитать правила? Тогда нажимайте /game. \n'
                                  'Если больше не хотите играть, нажимайте на /help(помощь) или /main(главное меню).',
                                  reply_markup=markup_black_white)


def echo(update, context: CallbackContext):
    '''
    Это функция позволяет боту отвечать на разные приветствия, знаки препинания не имеют значения
    Если боту пишут сообщение, которое он не понимает, он отправляет ему ключевую фразу, с предложением перейти к командам
    '''
    simbs = '.,/!)([]{}'
    for i in range(len(simbs)):
        update.message.text = update.message.text.replace(simbs[i], '')
    hellos = ['привет', 'здорова', 'хеллоу', 'hello', 'hi', 'салам', 'хай', 'дороу', 'приветик', 'доброе утро',
              'добрый день', 'добрый вечер']
    hellos_bb = ['Привет!', 'Здравствуй!', 'Доброго времени суток!']
    if update.message.text.lower() in hellos:
        update.message.reply_text(random.choice(hellos_bb))
    else:
        update.message.reply_text('Я не вполне понимаю о чем вы. \n'
                                  'хотите увидеть мой функционал, напишите команду /help. \n',
                                  reply_markup=markup)


def help(update, context: CallbackContext):
    '''
    Команда для тех, кто хочет ближе познакомиться с функционалом бота
    Выводит основные команды, которые понимает бот
    '''
    update.message.reply_text('список команд: \n'
                              '/help - вызывает список команд.\n'
                              '/game - вызывает список команд.\n'
                              '/audio - создает аудиокнигу.\n'
                              '/main - вызывает главное меню.',
                              reply_markup=markup_help)


def txt_in_audio(update, context: CallbackContext):
    '''
    Команда для тех, кто хочет ближе познакомиться с функционалом бота
    Выводит все команды, которые понимает бот
    '''
    update.message.reply_text(
        'Если вы желаете превратить txt файл в аудио книгу, пришлите txt файл следующим сообщением.',
        reply_markup=markup)


def echo_document(update, context: CallbackContext):
    '''
    функция обрабатывает
    '''
    file = context.bot.get_file(update.message.document)
    file.download(r'C:\audio_book\1.txt')
    converter_str_mp3()
    name = update.message.document.file_name.split('.')[:-1]
    a = ['C:/audio_book/'] + name + ['.mp3']
    direct = ''.join(a)
    os.rename(r'C:\audio_book\1.mp3', direct)
    # with open(r'C:\audio_book\1.mp3') as f:
    #     f.save(direct)
    update.message.reply_text(
        'Ваша аудиокнига ' + '"' + update.message.document.file_name + '"',
        reply_markup=markup)
    bot.send_audio(id_of_chat(update.message), audio=open(direct, 'rb'))
    os.remove(r'C:\audio_book\1.txt')
    os.remove(direct)
    update.message.reply_text('вы можете:\n'
                              'вернуться в главное меню /menu.\n'
                              'вызвать список комданд    /help.\n'
                              'сделать еще одну аудиокнигу. Для этого пришлите мне еще один txt файл.',
                              reply_markup=markup)


def echo_document_not_txt(update, context: CallbackContext):
    '''
    функция обрабатывает сообщения с не txt документами, которые присылает пользователь.
    Просит прислать txt документ
    '''
    update.message.reply_text(
        'Извините, но вы прислали не txt файл.\n'
        'Пришлите, пожалуйста txt файл',
        reply_markup=markup)


botToken = '5015096329:AAHqxoNdAEXjD6Y3lqaXZIFfNnC7OLTYV9U'
updater = Updater(botToken)

dp = updater.dispatcher

reply_keyboard = [['/help', '/main']]
first_keyboard = [['/help']]
main_menu_keyboard = [['/help', '/game'],
                      ['/audio']]
game_menu_keyboard = [['/black', '/white'],
                      ['/main', '/help']]
help_keyboard = [['/help', '/game'],
                 ['/audio', '/main']]
blackwhite = [['/black', '/white'],
              ['/game'],
              ['/help', '/main']]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
markup_start = ReplyKeyboardMarkup(first_keyboard, one_time_keyboard=False)
markup_main_menu = ReplyKeyboardMarkup(main_menu_keyboard, one_time_keyboard=False)
markup_guess_game = ReplyKeyboardMarkup(game_menu_keyboard, one_time_keyboard=False)
markup_help = ReplyKeyboardMarkup(help_keyboard, one_time_keyboard=False)
markup_black_white = ReplyKeyboardMarkup(blackwhite, one_time_keyboard=False)

dp.add_handler(CommandHandler('start', start))
dp.add_handler(CommandHandler('help', help))
dp.add_handler(CommandHandler('audio', txt_in_audio))
dp.add_handler(CommandHandler('main', main_menu))
dp.add_handler(CommandHandler('game', guess_game))
dp.add_handler(CommandHandler('white', game_colour))
dp.add_handler(CommandHandler('black', game_colour))

# разные фильтры: текста, txt, не txt
text_handler = MessageHandler(Filters.text, echo)
dp.add_handler(text_handler)
document_handler = MessageHandler(Filters.document.mime_type("text/plain"), echo_document)
dp.add_handler(document_handler)
document_handler = MessageHandler(Filters.document, echo_document_not_txt)
dp.add_handler(document_handler)

if __name__ == '__main__':
    updater.start_polling()
    updater.idle()
