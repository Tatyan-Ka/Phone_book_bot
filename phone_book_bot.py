# -*- coding: utf-8 -*-

import telebot
import file_work

bot = telebot.TeleBot('5561256183:AAHPFmqAlwTIVuPbs9p3Sx1cskN5tr8E0HI')  # @TeleBook0910_bot (PhoneBook_bot)

del_buttons = telebot.types.ReplyKeyboardRemove()

buttons1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons1.row(telebot.types.KeyboardButton('Показать все записи'),
             telebot.types.KeyboardButton('Экспорт в файл'))
buttons1.row(telebot.types.KeyboardButton('Импорт из файл'),
             telebot.types.KeyboardButton('Выход из программы'))

buttons2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons2.row(telebot.types.KeyboardButton('в строку'),
             telebot.types.KeyboardButton('в столбик'))


# buttons2.row(telebot.types.KeyboardButton('*'),
#              telebot.types.KeyboardButton('/'))


@bot.message_handler(commands=['log'])
def hello(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Лог программы\n',
                     reply_markup=del_buttons)
    bot.send_document(chat_id=msg.from_user.id, document=open('TestBot.log', 'rb'))


@bot.message_handler(content_types=['document'])
def get_file(msg: telebot.types.Message):
    file = bot.get_file(msg.document.file_id)
    downloaded_file = bot.download_file(file.file_path)
    with open(msg.document.file_name, 'wb') as f_out:
        f_out.write(downloaded_file)
    bot.register_next_step_handler(msg, file_work.import_file(msg.document.file_name, msg.caption))
    bot.send_message(chat_id=msg.from_user.id,
                     text=f'Файл {msg.document.file_name} импортирован в справочник',
                     reply_markup=buttons1)
    bot.register_next_step_handler(msg, answer)
    # Открываем и импортируем


@bot.message_handler(commands=['start'])
def hello(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Здравствуйте. Это телефонный справочник компании.\nВыберите действие:',
                     reply_markup=buttons1)
    bot.register_next_step_handler(msg, answer)  # ответ юзера будет обработан в функции answer


# @bot.message_handler()
def answer(msg: telebot.types.Message):
    if msg.text == 'Показать все записи':  # file_work.show_all(f)
        s = file_work.show_all('phone_book.txt')
        bot.send_message(chat_id=msg.from_user.id,
                         text=s,
                         reply_markup=buttons1)
        bot.register_next_step_handler(msg, answer)
    elif msg.text == 'Экспорт в файл':  # export_file(msg: telebot.types.Message)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Выберите формат:',
                         reply_markup=buttons2)
        bot.register_next_step_handler(msg, export_file)

    elif msg.text == 'Импорт из файл':  #
        # bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id, text='Загрузите файл для импорта в комментарии укажите формат: 1 - '
                                                        'в строку, 2 - в столбик')
    elif msg.text == 'Выход из программы':
        bot.send_message(chat_id=msg.from_user.id,
                         text='Пока-пока',
                         reply_markup=del_buttons)
        bot.stop_polling()

    else:
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id, text='Пожалуйста, используйте кнопки.')

        bot.send_message(chat_id=msg.from_user.id, text='Выберите действие:', reply_markup=buttons1)


# def complex_counter(msg: telebot.types.Message):
#     bot.send_message(chat_id=msg.from_user.id, text=msg.text.upper(),
#     reply_markup=telebot.types.ReplyKeyboardRemove())
#
#
# def rational_counter(msg: telebot.types.Message):
#     bot.send_message(chat_id=msg.from_user.id, text=msg.text.lower(),
#     reply_markup=telebot.types.ReplyKeyboardRemove())


def export_file(msg: telebot.types.Message):
    if msg.text == 'в строку':
        bot.register_next_step_handler(msg, file_work.export_file('export.txt', 'all', msg.text))
    else:
        bot.register_next_step_handler(msg, file_work.export_file('export.txt', 'all', msg.text))
    bot.send_message(chat_id=msg.from_user.id,
                     text='Справочник экспортирован в файл export.txt',
                     reply_markup=buttons1)
    bot.register_next_step_handler(msg, answer)


def import_file(msg: telebot.types.Message):
    if msg.text == 'в строку':
        bot.register_next_step_handler(msg, file_work.import_file('export.txt', 'all', msg.text))
    else:
        bot.register_next_step_handler(msg, file_work.import_file('export.txt', 'all', msg.text))
    bot.send_message(chat_id=msg.from_user.id,
                     text='Справочник экспортирован в файл export.txt',
                     reply_markup=buttons1)
    bot.register_next_step_handler(msg, answer)


bot.polling()
