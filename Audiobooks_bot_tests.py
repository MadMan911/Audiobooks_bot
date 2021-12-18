from telethon import TelegramClient, sync, events
from telethon.tl.functions.channels import GetMessagesRequest
import unittest
import time

api_id= int('5015096329:AAHqxoNdAEXjD6Y3lqaXZIFfNnC7OLTYV9U')
api_hash = ""
client = TelegramClient('session_name', api_id, api_hash)

client.start()


class audiobook_test(unittest.TestCase):
    def test_start(self):
        try:
            client.send_message('@Assistant_with_audio_books_bot', '/start')
            time.sleep(2)
            messages = client.get_messages('@Assistant_with_audio_books_bot')
            for message in client.get_messages('@Assistant_with_audio_books_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'Привет! Я бот с аудиокнигами.\n''Для получения инструкций нажмите на кнопку /help.'
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
            text = f'вы можете:\n''вернуться в главное меню /menu.\n''вызвать список комданд    /help.\n''сделать еще одну аудиокнигу. Для этого пришлите мне еще один txt файл.'
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

    def test_echo(self):
        try:
            messages = client.get_messages('@Assistant_with_audio_books_bot', limit=1)
            for message in client.get_messages('@Assistant_with_audio_books_bot', limit=1):
                if not (message.endswith(".txt")):
                    m=message.message
                    r=message
            self.assertEqual(len(messages), 1)
            text=f'Ваша аудиокнига + r'
            self.assertRegex(m,text)
        except:
            self.assertFalse(True)
