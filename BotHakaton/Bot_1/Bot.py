import telebot
from telebot import types

dokbot = telebot.TeleBot("5823350388:AAFQs-96R4kWQ7hDhDTc4Rtcuwmxb2BHKlE")

@dokbot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button_1 = types.KeyboardButton('Docx')
    button_2 = types.KeyboardButton('Pdf')
    button_3 = types.KeyboardButton('Txt')
    markup.add(button_1, button_2, button_3)
    dokbot.send_message(message.chat.id, f'Привет {message.from_user.first_name}, это бот, который конвертирует файл формата frx в выбранный тобою формат.', reply_markup=markup)


dokbot.polling(none_stop=True)