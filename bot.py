import datetime
import telebot
import logging
from telebot import types

logfile = open("bot.log", "a")
time = datetime.datetime.now()
logfile.write("Bot Started: " + str(time) + " with ")
print("Bot started: " + str(time))

# CONFIG
TOKEN = '116144035:AAHVDjt5VX-5bKGGrbtw6QJPEZF4reJcIjc' # BOT TOKEN
DEEP_LOGGING = False # FOR DEBUGGING PURPOSES ONLY
SAFE_ECHO = False # DOONT REPLY TO MESSAGES SENT IN SUPER GROUPS TO PREVENT SPAM
ADMIN_ID = 98120772 # ID OF BOT'S ADMIN
REPLIER = True # Lol.. a simple reply-to-message system xD (using dictionaries)

#REPLY MESSAGES
reply_message_list = {"salam": "slm",
  "hi": "aleyke hi",
  "hello": "dorood",
}
# END OF CONFIG

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  markup = types.ReplyKeyboardMarkup()
  itembtna = types.KeyboardButton('/start')
  itembtnv = types.KeyboardButton('/help')
  markup.row(itembtna, itembtnv)
  if message.chat.type == "private":
    bot.reply_to(message, "Hey, Hi!", reply_markup=markup)
  else:
    bot.reply_to(message, "Hey, Hi!")

@bot.message_handler(commands=['test', 'toast'])
def send_test(message):
  bot.send_message(message.chat.id, "LoL Test Msg")

@bot.message_handler(commands=['sendcontact'])
def send_test(message):
  bot.send_message(message.chat.id, "Please share your contact to the bot.")
  

@bot.message_handler(commands=['echo'])
def echo_message(message):
  if SAFE_ECHO:
    if message.chat.type == "supergroup":
      bot.reply_to(message, "Unfortunately I wont reply to messages sent in a supergroup to prevent spamming.")
      return
  if len(message.text.split()) < 2:
    bot.reply_to(message, "Please enter a text so I reply to it!")
    return
  try:
    echo_msg = message.text.replace("/echo","",1)
    bot.reply_to(message, echo_msg)
  except:
    bot.send_message(messsage.chat.id, "Error occured.")
  
def message_replier(messages):
  for message in messages:
    if message.text in reply_message_list:
      bot.reply_to(message, reply_message_list.get(message.text))

def contact_forwarder(contact):
  for message in contact:
    if message.content_type = "contact":
      bot.reply_to(ADMIN_ID, message.chat.id, message.message.id)


logger = telebot.logger
if DEEP_LOGGING:
  print("Logging enabled.")
  logfile.write("logging enabled. \n")
  telebot.logger.setLevel(logging.DEBUG)
else:
  logfile.write("logging disabled. \n")
  print("Logging disabled.")

if REPLIER:
  bot.set_update_listener(message_replier)

bot.set_update_listener(contact_forwarder)
logfile.close()
bot.polling(none_stop=True, interval=0, timeout=3)
