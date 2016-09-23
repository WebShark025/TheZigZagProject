import datetime
import telebot

time = datetime.datetime.now()
print("Bot started: " + str(time))
TOKEN = '116144035:AAHVDjt5VX-5bKGGrbtw6QJPEZF4reJcIjc'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "Hey, Hi!")

@bot.message_handler(commands=['test', 'toast'])
def send_test(message):
  bot.send_message(message.chat, "LoL Test Msg")

bot.polling()
