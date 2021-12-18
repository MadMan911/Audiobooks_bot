from telethon import TelegramClient, sync, events
from telethon.tl.functions.channels import GetMessagesRequest
import unittest
import time
from Token import api_Id, hash_Id



api_id= api_Id
api_hash = hash_Id
client = TelegramClient('session_name3', api_id, api_hash)

client.start()


class audiobook_test(unittest.TestCase):
    '''
    тесты для функций бота
    '''
    def test_start(self):
        try:
            client.send_message('@Assistant_with_audio_books_bot', '/start')
            time.sleep(2)
            messages = client.get_messages('@Assistant_with_audio_books_bot')
            for message in client.get_messages('@Assistant_with_audio_books_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'Привет! Я бот с аудиокнигами.'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)


    def test_hello(self):
        try:
            client.send_message('@Assistant_with_audio_books_bot', 'Привет')
            time.sleep(2)
            messages = client.get_messages('@Assistant_with_audio_books_bot')
            for message in client.get_messages('@Assistant_with_audio_books_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'Здравствуйте!'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True, f'Я не вполне понимаю о чем вы. \n''хотите увидеть мой функционал, напишите команду /help. \n')


    def test_help(self):
        try:
            client.send_message('@Assistant_with_audio_books_bot', '/help')
            time.sleep(2)
            messages = client.get_messages('@Assistant_with_audio_books_bot')
            for message in client.get_messages('@Assistant_with_audio_books_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text =f'список команд: \n''/help - вызывает список команд.\n''/game - вызывает список команд.\n''/audio - создает аудиокнигу.\n''/main - вызывает главное меню.'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)

    def test_game(self):
        try:
            client.send_message('@Assistant_with_audio_books_bot', '/game')
            time.sleep(2)
            messages = client.get_messages('@Assistant_with_audio_books_bot')
            for message in client.get_messages('@Assistant_with_audio_books_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'Правила игры:\n''Я загадываю цвет: Черный или белый.\n''Вы должны его угадать, для этого нажмите на кнопку /black - черный или /white - белый.\n''Для получения инструкций нажмите на кнопку "/help".\n''Для возвращения в главное меню нажмите на кнопку "/main".'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)

    def test_audio(self):
        try:
            client.send_message('@Assistant_with_audio_books_bot', '/audio')
            time.sleep(2)
            messages = client.get_messages('@Assistant_with_audio_books_bot')
            for message in client.get_messages('@Assistant_with_audio_books_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text=f'Если вы желаете превратить txt файл в аудио книгу, пришлите txt файл следующим сообщением.'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
