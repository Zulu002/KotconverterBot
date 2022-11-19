import telebot
from telebot import types
import requests
import convertapi
from bs4 import BeautifulSoup
import converter

dokbot = telebot.TeleBot("5823350388:AAFQs-96R4kWQ7hDhDTc4Rtcuwmxb2BHKlE")


@dokbot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button_1 = types.KeyboardButton('Docx')
    button_2 = types.KeyboardButton('Pdf')
    button_3 = types.KeyboardButton('Txt')
    markup.add(button_1, button_2, button_3)
    dokbot.send_message(message.chat.id,
                        f'Привет {message.from_user.first_name}, это бот, который конвертирует файл формата frx в выбранный тобою формат.')
    dokbot.send_message(message.chat.id, "Загружай файл.")


@dokbot.message_handler(content_types=["document"])
def files(message):
    file_id_info = dokbot.get_file(message.document.file_name)
    downloaded_file = dokbot.download_file(file_id_info.file_path)
    name_file = dokbot.get_file(message.document.file_name)
    return message



@dokbot.message_handler(content_types=["text"])
def message_user(message):
    new_message = message.text.strip()
    if new_message == "Docx":
        dokbot.send_message(message.chat.id, 'Вы выбрали docx формат.')
        dokbot.send_message(message.chat.id, files)
    elif new_message == "Txt":
        dokbot.send_message(message.chat.id, 'Вы выбрали txt формат.')
        dokbot.send_message(message.chat.id, files)
    elif new_message == "Pdf":
        dokbot.send_message(message.chat.id, 'Вы выбрали pdf формат.')
        dokbot.send_message(message.chat.id, files)


dokbot.polling(none_stop=True)
