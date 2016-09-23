import datetime
import telebot

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
  bot.reply_to(message, "Hey, Hi!")

@bot.message_handler(commands=['test', 'toast'])
def send_test(message):
  bot.send_message(message.chat.id, "LoL Test Msg")

bot.polling(none_stop=True, interval=0, timeout=3)
