import os
from telebot import TeleBot
import telebot
from telebot import types
import time

ddr = "0"
you = "0"
bot = telebot.TeleBot('токен_бота'); # Создай бота в @BotFather и возьми оттуда токен бота #

keyboard1 = types.ReplyKeyboardMarkup(True,False)
keyboard1.row('Старт', 'Стоп','Статус','Ребут кнопок')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	ddr = message.text
	you = message.from_user.id
	if str(you) == "твой_телеграм_айди":
		if message.text.lower() == "старт":
			bot.send_message(message.from_user.id, "Буст запущен!",reply_markup=keyboard1)
			os.system("node bot.js")
		elif message.text.lower() == "стоп":
			bot.send_message(message.from_user.id, "Буст завершен!",reply_markup=keyboard1)
			os.system("killall node")
			print(time.asctime(time.localtime()))
		elif message.text.lower() == "статус": # проверка бота&буста на работоспособность #
			bot.send_message(message.from_user.id, "Онлайн.",reply_markup=keyboard1)
			#os.system("killall node")
	else:
		bot.send_message(message.from_user.id,"Отказано в доступе")# на случай если кто то напишет вашему боту не имея доступа #
try:
 bot.polling(none_stop=True, interval=0)
except Exception:
 pass
input()

## ПО ВСЕМ ВОПРОСАМ t.me/xeroweroskillopium ##    ## ПО ВСЕМ ВОПРОСАМ t.me/xeroweroskillopium ##
## ПО ВСЕМ ВОПРОСАМ t.me/xeroweroskillopium ##    ## ПО ВСЕМ ВОПРОСАМ t.me/xeroweroskillopium ##
## ПО ВСЕМ ВОПРОСАМ t.me/xeroweroskillopium ##    ## ПО ВСЕМ ВОПРОСАМ t.me/xeroweroskillopium ##