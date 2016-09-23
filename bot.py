import datetime
import telebot
from telebot import types

time = datetime.datetime.now()
print("Bot started: " + str(time))
TOKEN = '116144035:AAHVDjt5VX-5bKGGrbtw6QJPEZF4reJcIjc'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  markup = types.ReplyKeyboardMarkup()
  itembtna = types.KeyboardButton('/start')
  itembtnv = types.KeyboardButton('/help')
  markup.row(itembtna, itembtnv)
  bot.reply_to(message, "Hey, Hi!", reply_markup=markup)

@bot.message_handler(commands=['test', 'toast'])
def send_test(message):
  bot.send_message(message.chat.id, "LoL Test Msg")

@bot.message_handler(commands=['echo'])
def echo_message(message):
  if len(message.text.split()) < 2:
    bot.reply_to(message, "Please enter a text so I reply to it!")
  try:
    echo_msg = message.text.replace("/echo","",1)
    bot.reply_to(message, echo_msg)
  except:
    bot.send_message(messsage.chat.id, "Error occured.")
  
  
bot.polling(none_stop=True, interval=0, timeout=3)
