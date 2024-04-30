import telebot
from telebot import types

bot = telebot.TeleBot('6811508803:AAEY0iMsIPhV0XKyO-R4yECZqJrwNErra7o')

status = {}


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, '<b>Мы рады, что Вы заинтересовались нашей продукцией.</b>', parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Програмное обеспечение на 1 год')
    markup.add(item1)
    item2 = types.KeyboardButton('Програмное обеспечение на 5 лет')
    markup.add(item2)
    item3 = types.KeyboardButton('Оборудование')
    markup.add(item3)
    bot.send_message(message.chat.id, '<b>Выберите из всплывающих кнопок, что Вас интересует</b>', parse_mode='html', reply_markup=markup)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)


def send_answer(message):
    if status[message.from_user.id] == 1:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item5 = types.KeyboardButton('Regula Document Reader SDK 1 ГОД')
        markup.add(item5)
        item4 = types.KeyboardButton('Назад')
        markup.add(item4)
    if status[message.from_user.id] == 15:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Програмное обеспечение на 1 год')
        markup.add(item1)
        item2 = types.KeyboardButton('Програмное обеспечение на 5 лет')
        markup.add(item2)
        item3 = types.KeyboardButton('Оборудование')
        markup.add(item3)
        item4 = types.KeyboardButton('Назад')
        markup.add(item4)
        bot.send_message(message.chat.id, '<b>Выберите из всплывающих кнопок, что Вас интересует</b>',
                        parse_mode='html', reply_markup=markup)

        bot.send_message(message.chat.id, text=f"Выберите интересующие вас ПО.", reply_markup=markup)

    elif status[message.from_user.id] == 1:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item6 = types.KeyboardButton('Regula Document Reader SDK 1 ГОД')
        markup.add(item6)
        item4 = types.KeyboardButton('Назад')
        markup.add(item4)
        bot.send_message(message.chat.id, text=f"Выберите интересующие вас ПО.", reply_markup=markup)

    elif status[message.from_user.id] == 2:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item6 = types.KeyboardButton('Regula Document Reader SDK 5 ЛЕТ')
        markup.add(item6)
        item4 = types.KeyboardButton('Назад')
        markup.add(item4)
        bot.send_message(message.chat.id, text=f"Выберите интересующие вас ПО.", reply_markup=markup)

    elif status[message.from_user.id] == 3:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item7 = types.KeyboardButton('Считыватель документов «Регула» 7017')
        markup.add(item7)
        item8 = types.KeyboardButton('Считыватель документов «Регула» 7017.100')
        markup.add(item8)
        item9 = types.KeyboardButton('Считыватель документов «Регула» 7017.110')
        markup.add(item9)
        item10 = types.KeyboardButton('Считыватель документов «Регула» 7017.111')
        markup.add(item10)
        item11 = types.KeyboardButton('Считыватель документов «Регула» 7027')
        markup.add(item11)
        item12 = types.KeyboardButton('Считыватель документов «Регула» 7027.100')
        markup.add(item12)
        item13 = types.KeyboardButton('Считыватель документов «Регула» 7027.110')
        markup.add(item13)
        item14 = types.KeyboardButton('Считыватель документов «Регула» 7027.111')
        markup.add(item14)
        item15 = types.KeyboardButton('Считыватель документов «Регула» 7037')
        markup.add(item15)
        item4 = types.KeyboardButton('Назад')
        markup.add(item4)
        bot.send_message(message.chat.id, text=f"Выберите интересующий вас прибор.", reply_markup=markup)

    elif status[message.from_user.id] == 4:
        bot.send_message(message.chat.id, text='Программное обеспечение "Regula Document Reader SDK", OCR- W1 '
                                          '(Программное обеспечение для оптического распознавания символов: считывание '
                                          'информации из визуальной зоны документов (соответствующих и несоответствующих стандартам ICAO). '
                                          ' Cтоимость годовой лицензии 92 Евро, в т.ч. НДС-20%. Оплата в рублях по курсу ЦБ РФ на дату платежа.', )

    elif status[message.from_user.id] == 5:
        bot.send_message(message.chat.id, ' Программное обеспечение "Regula Document Reader SDK", OCR- W5 '
                                          '(Программное обеспечение для оптического распознавания символов:'
                                          'считывание информации из визуальной зоны документов (соответствующих и '
                                          'несоответствующих стандартам ICAO). Стоимость 5-ти летней  лицензии - 448 Евро, в т.ч. НДС-20%. Оплата в рублях по курсу ЦБ РФ на дату платежа.', )

    elif status[message.from_user.id] == 6:
        bot.send_photo(message.chat.id, photo=open('photo.jpeg', 'rb'), caption='Считыватель для полностраничного сканирования '
                                                                                'документов. Разрешение: 470 ppi. '
                                          'Источники света: только белый.Возможность совместной работы с ИСС Паспорт, '
                                          'Автодокументы и FDS. Цена 690 Евро, в т.ч. НДС-20%. Оплата в рублях по курсу ЦБ РФ на  дату платежа.', )

    elif status[message.from_user.id] == 7:
        bot.send_photo(message.chat.id, photo=open('photo.jpeg', 'rb'), caption='Считыватель для полностраничного сканирования документов. Разрешение: 470 ppi. '
                                          'Источники света: только белый.Возможность совместной работы с ИСС Паспорт, '
                                          'Автодокументы и FDS + ИК 870 нм. Цена 740 Евро, в т.ч. НДС-20%. Оплата в рублях по '
                                          'курсу ЦБ РФ на дату платежа.', )

    elif status[message.from_user.id] == 8:
        bot.send_photo(message.chat.id, photo=open('photo.jpeg', 'rb'), caption='Считыватель для полностраничного сканирования документов. Разрешение: 470 ppi. '
                                          'Источники света: только белый.Возможность совместной работы с ИСС Паспорт, '
                                              'Автодокументы и FDS + ИК 870 нм + УФ 365 нм. Цена 845 Евро', )

    elif status[message.from_user.id] == 9:
        bot.send_photo(message.chat.id, photo=open('photo.jpeg', 'rb'), caption='Считыватель для полностраничного сканирования документов. Разрешение: 470 ppi. '
                                          'Источники света: только белый.Возможность совместной работы с ИСС Паспорт, '
                                          'Автодокументы и FDS + ИК 870 нм + UV 365 нм + 3М. Цена 745 Евро, в т.ч. НДС-20%. Оплата в рублях '
                                          'по курсу ЦБ РФ на дату платежа.', )

    elif status[message.from_user.id] == 10:
        bot.send_photo(message.chat.id, photo=open('photo.jpeg', 'rb'), caption='Считыватель для полностраничного сканирования документов. Разрешение: 470 ppi. '
                                          'Источники света: только белый.Возможность совместной работы с ИСС Паспорт, '
                                          'Автодокументы и FDS + RFID. Цена 865 Евро, в т.ч. НДС-20%. Оплата в рублях по курсу ЦБ РФ на дату платежа.', )

    elif status[message.from_user.id] == 11:
        bot.send_photo(message.chat.id, photo=open('photo.jpeg', 'rb'), caption='Считыватель для полностраничного сканирования документов. Разрешение: 470 ppi. '
                                          'Источники света: только белый.Возможность совместной работы с ИСС Паспорт, '
                                          'Автодокументы и FDS + ИК 870 нм + RFID. Цена 910 Евро, в т.ч. НДС-20%. Оплата в рублях по курсу ЦБ РФ на дату платежа.', )

    elif status[message.from_user.id] == 12:
        bot.send_photo(message.chat.id, photo=open('photo.jpeg', 'rb'), caption='Считыватель для полностраничного сканирования документов. Разрешение: 470 ppi. '
                                          'Источники света: только белый.Возможность совместной работы с ИСС Паспорт, '
                                          'Автодокументы и FDS + ИК 870 нм + УФ 365 нм + RFID. Цена 1050 Евро, в т.ч. НДС-20%. Оплата в рублях по курсу ЦБ РФ на дату платежа.', )

    elif status[message.from_user.id] == 13:
        bot.send_photo(message.chat.id, photo=open('photo.jpeg', 'rb'), caption='Считыватель для полностраничного сканирования документов. Разрешение: 470 ppi. '
                                          'Источники света: только белый.Возможность совместной работы с ИСС Паспорт, '
                                          'Автодокументы и FDS +  ИК 870 нм + УФ 365 нм + 3М + RFID. Цена 1045 Евро, в т.ч. НДС-20%. Оплата в рублях по курсу ЦБ РФ на дату платежа.', )

    elif status[message.from_user.id] == 14:
        bot.send_photo(message.chat.id, photo=open('photo.jpeg', 'rb'), caption='Считыватель для полностраничного сканирования документов. Разрешение: 470 ppi. '
                                          'Источники света: только белый.Возможность совместной работы с ИСС Паспорт, '
                                          'Автодокументы и FDS + считыватель контактных карт + RFID. Цена 1045 Евро, в т.ч. НДС-20%. Оплата в рублях по курсу ЦБ РФ на дату платежа.', )





@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == 'Програмное обеспечение на 1 год':
        status[message.from_user.id] = 1

    if message.text == 'Програмное обеспечение на 5 лет':
        status[message.from_user.id] = 2

    if message.text == 'Оборудование':
        status[message.from_user.id] = 3

    if message.text == "Regula Document Reader SDK 1 ГОД":
        status[message.from_user.id] = 4

    if message.text == "Regula Document Reader SDK 5 ЛЕТ":
        status[message.from_user.id] = 5

    if message.text == "Считыватель документов «Регула» 7017":
        status[message.from_user.id] = 6

    if message.text == "Считыватель документов «Регула» 7017.100":
        status[message.from_user.id] = 7

    if message.text == "Считыватель документов «Регула» 7017.110":
        status[message.from_user.id] = 8

    if message.text == "Считыватель документов «Регула» 7017.111":
        status[message.from_user.id] = 9

    if message.text == "Считыватель документов «Регула» 7027":
        status[message.from_user.id] = 10

    if message.text == "Считыватель документов «Регула» 7027.100":
        status[message.from_user.id] = 11

    if message.text == "Считыватель документов «Регула» 7027.110":
        status[message.from_user.id] = 12

    if message.text == "Считыватель документов «Регула» 7027.111":
        status[message.from_user.id] = 13

    if message.text == "Считыватель документов «Регула» 7037":
        status[message.from_user.id] = 14

    if message.text == "Назад":
        status[message.from_user.id] = 15

    send_answer(message)


bot.polling(non_stop=True)
