# -*- coding: utf-8 -*-
import config
import telebot
from telebot import apihelper
from telebot import types

#apihelper.proxy = {'https':'https://212.129.8.156:8080'}
bot = telebot.TeleBot(config.token)
markup_start = types.ReplyKeyboardMarkup()
markup_start.row('\U0001F4D4О разработчике\U0001F4D4')
markup_start.row('\U0001F382Услуги\U0001F382')
markup_start.row('\U0001F6CEКонтакты\U0001F6CE')
markup_start.row('\U0001F525Как сделать заказ?\U0001F525')
@bot.message_handler(commands=['start'])
def start_mess(message):
    bot.send_message(message.chat.id,'Это демонстрационный бот. Вы можете заказать подобного связавшись со мной',reply_markup=markup_start)
@bot.message_handler(content_types=["text"])
def get_mess(message):
    if message.text == '\U0001F4D4О разработчике\U0001F4D4':
        bot.send_message(message.chat.id,'Привет, меня зовут Андрей и я занимаюсь разработкой Телеграм-ботов \nЕсли у вас есть вопросы - свяжитесь со мной! \U0001f525 ',reply_markup=markup_start)
    if message.text == '\U0001F6CEКонтакты\U0001F6CE':
        bot.send_message(message.chat.id,'Email: work.andrey0@gmail.com \nTelegram: @Llloyd',reply_markup=markup_start)
    if message.text == '\U0001F382Услуги\U0001F382':
        bot.send_message(message.chat.id,'Создание телеграмм бота для ответа на простые команды\n--Возможность добавления до 5 команд\n--Кастомные клавиатуры\n--Подключение дополнительных функций стороних сайтов(за дополнительную цену)',reply_markup=markup_start)
    if message.text == '\U0001F525Как сделать заказ?\U0001F525':
        bot.send_message(message.chat.id,'Вы можете сделать заказ на одной из бирж \n   Kwark -- <ссылка>\n   FL -- <ссылка>\nИли связавшись со мной через контакты',reply_markup=markup_start)
if __name__ == '__main__':
		bot.polling(none_stop=True)
