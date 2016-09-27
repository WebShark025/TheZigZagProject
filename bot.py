import datetime
import os
import telebot
import logging
import sys
import urllib
import re
import redis
from shutil import copyfile
from telebot import types




### CONFIG AND LOCALE CHECK
if not os.path.exists("config.py"):
  copyfile("config.py.new", "config.py")
if not os.path.exists("locale.py"):
  copyfile("locale.py.new", "locale.py")
  
# REDIS SERVER. IF ITS DIFFRENT, CONFIG IT!
redisserver = redis.StrictRedis(host='localhost', port=6379, db=0)


reload(sys)  
sys.setdefaultencoding("utf-8")

execfile("locale.py")
execfile("config.py")

# LOGFILE
logfile = open("bot.log", "a")
time = datetime.datetime.now()
logfile.write("Bot Started: " + str(time) + " with ")
print("Bot started: " + str(time))
messanger_list = []
contacter_list = []


############################################################################
# START OF CODES. DO NOT EDIT ANYTHING IF YOU DONT KNOW WHAT ARE YOU DOING!#
############################################################################
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    bot.reply_to(message, "You are banned!")
    return
  markup = types.ReplyKeyboardMarkup()
  numbers = list(range(3, 3000, 3))
  numbers = [0] + numbers
  cline = 0
  linelength = len(START_BUTTONS)
  try:
    while (cline < linelength):
      itembtn = []
      cfrom = numbers[cline]
      cto = numbers[cline + 1]
      cline = cline + 1
      while (cfrom < cto):
        itembtn.append(START_BUTTONS[cfrom])
        cfrom = cfrom + 1
        if len(itembtn) == 3:
          markup.row(*itembtn)
  except:
    lolalola = 0
  
  if message.chat.type == "private":
    bot.reply_to(message, START_MSG.encode("utf-8"), reply_markup=markup, parse_mode="Markdown")
    redisserver.sadd('zigzag_members',message.from_user.id)
  else:
    bot.reply_to(message, START_MSG.encode("utf-8"), parse_mode="Markdown")

for plugin in enabled_plugins:
  execfile("plugins/" + plugin + ".py")

#@bot.message_handler(commands=['webshot'])
#def webshot_send(message):
#  userid = message.from_user.id
#  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
#  if banlist:
#    return
#  text = message.text.replace("/webshot ","")
#  urllib.urlretrieve("http://api.screenshotmachine.com/?key=b645b8&size=X&url={}".format(text), 'webshot.jpg')
#  bot.send_photo(message.chat.id, open('webshot.jpg'), caption=" " + WEBSHOT_CAPTION_MSG)

#@bot.message_handler(commands=['gpstats'])
#def echo_message(message):
#  userid = message.from_user.id
#  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
#  if banlist:
#    return
#  if message.chat.type == "supergroup":
#    if redisserver.sismember("zigzag_groups", message.chat.id):
#      gpmsgcount = list(redisserver.smembers(message.chat.id))
#      for messagess in allmembers:
#        bot.reply_to(message, GP_STATUS_MSG.format(messagess), parse_mode="HTML")
  
def message_replier(messages):
  for message in messages:
    userid = message.from_user.id
    banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
    if banlist:
      return
    if userid in messanger_list:
      bot.reply_to(message, MESSANGER_LEAVE_MSG, parse_mode="Markdown")
      messanger_list.remove(userid)
      bot.forward_message("-" + str(SUPPORT_GP), message.chat.id, message.message_id)
      return
    if REPLIER:
      if message.text in reply_message_list:
        bot.reply_to(message, reply_message_list.get(message.text), parse_mode="Markdown")
    if message.text == "Send feedback":
      bot.reply_to(message, MESSANGER_JOIN_MSG, parse_mode="Markdown")
      messanger_list.append(userid)
      return
#    if message.chat.type == "supergroup":
#      if redisserver.sismember("zigzag_groups", message.chat.id):
#        allargs = list(redisserver.smembers(message.chat.id))
#        allargs[0] = allargs[0] + 1
      
#    if message.text not in ENABLED_CMDS:
#      try:
#        if message.text.startswith("/"):
#          if len(message.text.split()) < 2:
#            bot.reply_to(message, COMMAND_NOT_FOUND, parse_mode="Markdown")
#      except:
#        lolalelellele = 0
# IDK WHY, BUT IN SOME CASES THEESE WOULD CAUSE CRASH :|
# COMMENTED OUT.

@bot.message_handler(func=lambda message: True, content_types=['new_chat_member'])
def user_greet(message):
  if GP_GREETING:
    if message.new_chat_member.id != bot.get_me().id:
      name = message.new_chat_member.first_name
      title = message.chat.title
      bot.send_message(message.chat.id, GP_GREETING_MSG.format(name,title).encode("utf-8"), parse_mode='Markdown')
  
  if message.new_chat_member.id == bot.get_me().id:
    inviter = message.from_user.id
    if inviter not in ADMINS_IDS:
      bot.send_message(message.chat.id, NON_ADMIN_ADDED_BOT_MSG.encode("utf-8"))
      bot.leave_chat(message.chat.id)
    else:
      bot.send_message(message.chat.id, BOT_JOINED_MSG)
#      groupargs = 0
#      redisserver.sadd(message.chat.id, groupargs)
#      redisserver.sadd("zigzag_groups", message.chat.id)
  
@bot.message_handler(func=lambda message: True, content_types=['left_chat_member'])
def user_greet(message):
  if GP_FAREWELL:
    name = message.left_chat_member.first_name
    title = message.chat.title
    bot.send_message(message.chat.id, GP_FAREWELL_MSG.format(name,title).encode("utf-8"), parse_mode='Markdown')
  
@bot.message_handler(func=lambda m: True, content_types=['contact'])
def contact_forwarder(contact):
  userid = contact.from_user.id
  if userid in contacter_list:
    bot.send_message("-" + str(SUPPORT_GP), CONTACT_RECIEVED_MSG.encode("utf-8"))
    bot.forward_message("-" + str(SUPPORT_GP), contact.chat.id, contact.message_id)
    bot.reply_to(contact, CONTACT_FORWARDED_MSG.encode("utf-8"))

logger = telebot.logger
if DEEP_LOGGING:
  print("Debugging enabled.")
  logfile.write("debugging enabled. \n")
  telebot.logger.setLevel(logging.DEBUG)
else:
  logfile.write("debugging disabled. \n")
  print("Debugging disabled.")

bot.set_update_listener(message_replier)

logfile.close()
bot.polling(none_stop=True, interval=0, timeout=3)
