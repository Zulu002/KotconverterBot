import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
number = 0
dokbot = telebot.TeleBot("5823350388:AAFQs-96R4kWQ7hDhDTc4Rtcuwmxb2BHKlE")


@dokbot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Docx')
    button_2 = types.KeyboardButton('Pdf')
    button_3 = types.KeyboardButton('Txt')
    markup.add(button_1, button_2, button_3)
    dokbot.send_message(message.chat.id,
                        f'Привет {message.from_user.first_name}, это бот, который конвертирует файл формата frx в выбранный тобою формат.')
    dokbot.send_message(message.chat.id, "Загружай файл.", reply_markup=markup)


@dokbot.message_handler(content_types=["document"])
def files(message):
    pass



@dokbot.message_handler(content_types=["text"])
def message_user(message):
    global number
    new_message = message.text.strip()
    if new_message == "Docx":
        number = 1
        dokbot.send_message(message.chat.id, 'Вы выбрали docx формат.')
        dokbot.send_document(message.chat.id, open("doc/Text.docx", "rb"))


    elif new_message == "Txt":
        number = 2
        dokbot.send_message(message.chat.id, 'Вы выбрали txt формат.')
        dokbot.send_document(message.chat.id, open("doc/Text.txt", "rb"))

    elif new_message == "Pdf":
        number = 3
        dokbot.send_message(message.chat.id, 'Вы выбрали pdf формат.')
        dokbot.send_document(message.chat.id, open("doc/Text.pdf", "rb"))


dokbot.polling(none_stop=True)