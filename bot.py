import telebot

TOKEN = '116144035:AAHVDjt5VX-5bKGGrbtw6QJPEZF4reJcIjc'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "Hey, Hi!")

bot.polling()
