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


@bot.message_handler(commands=['test', 'toast'])
def send_test(message):
  bot.send_message(message.chat.id, TEST_MSG.encode("utf-8"))
  
@bot.message_handler(commands=['members'])
def send_members(message):
  if message.from_user.id in ADMINS_IDS:
    bot.send_message(message.chat.id, "All members: " + str(redisserver.scard('zigzag_members')) + " \nBanned members: " + str(redisserver.scard('zigzag_banlist')), parse_mode="Markdown")
#    allmembers = list(redisserver.smembers('zigzag_members'))
#    bot.send_message(message.chat.id, "First member: " + str(allmembers[0]), parse_mode="Markdown")
  else:
    bot.send_message(message.chat.id, "You dont have permission.")
    
@bot.message_handler(commands=['bc'])
def bc_msg(message):
  if message.from_user.id in ADMINS_IDS:
    if len(message.text.split()) < 2:
      bot.reply_to(message, "What should I broadcast?")
      return
    bcmsg = message.text.replace("/bc ","")
    allmembers = list(redisserver.smembers('zigzag_members'))
    for userid in allmembers:
      bot.send_message(userid, bcmsg, parse_mode="HTML")
    bot.reply_to(message, "Successfully broadcasted!")
  else:
    bot.send_message(message.chat.id, "You dont have permission.")
  
@bot.message_handler(commands=['ban'])
def ban_user(message):
  if message.from_user.id in ADMINS_IDS:
    if len(message.text.split()) < 2:
      bot.reply_to(message, "Who should I ban?")
      return
    userid = message.text.split()[1]
    redisserver.sadd('zigzag_banlist', int(userid))
    bot.send_message(int(userid), BANNED_MSG, parse_mode="Markdown")
    bot.send_message(message.chat.id, "Banned user: " + str(userid), parse_mode="Markdown")
  else:
    bot.send_message(message.chat.id, "You dont have permission.")

@bot.message_handler(commands=['unban'])
def ban_user(message):
  if message.from_user.id in ADMINS_IDS:
    if len(message.text.split()) < 2:
      bot.reply_to(message, "Who should I unban?")
      return
    userid = message.text.split()[1]
    redisserver.srem('zigzag_banlist', int(userid))
    bot.send_message(int(userid), UNBANNED_MSG, parse_mode="Markdown")
    bot.send_message(message.chat.id, "Unbanned user: " + str(userid), parse_mode="Markdown")
  else:
    bot.send_message(message.chat.id, "You dont have permission.")
    
    
@bot.message_handler(commands=['feedback', 'sendfeedback'])
def send_feedbackz(message):
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if userid not in messanger_list:
    bot.reply_to(message, MESSANGER_JOIN_MSG, parse_mode="Markdown")
    messanger_list.append(userid)
    return

#@bot.message_handler(commands=['webshot'])
#def webshot_send(message):
#  userid = message.from_user.id
#  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
#  if banlist:
#    return
#  text = message.text.replace("/webshot ","")
#  urllib.urlretrieve("http://api.screenshotmachine.com/?key=b645b8&size=X&url={}".format(text), 'webshot.jpg')
#  bot.send_photo(message.chat.id, open('webshot.jpg'), caption=" " + WEBSHOT_CAPTION_MSG)

@bot.message_handler(commands=['calc'])
def clac(m):
  userid = m.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if len(m.text.split()) < 2:
    bot.reply_to(m, "How can i calculate null?")
    return
  text = m.text.replace("/calc ","")
  res = urllib.urlopen("http://api.mathjs.org/v1/?expr={}".format(text).replace("+","%2B")).read()
  bot.send_message(m.chat.id, "_{}_ = `{}`".format(text,res), parse_mode="Markdown", disable_web_page_preview=True)

@bot.message_handler(commands=['id'])
def send_id(message):
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  username = message.from_user.first_name.encode("utf-8")
  userid = message.from_user.id
  reply_msg = ID_MSG.encode("utf-8")
  gpid = message.chat.id
  if message.chat.type == "supergroup":
    reply_msg = reply_msg + INGP_ID_MSG.encode("utf-8")
  elif message.chat.type == "group":
    reply_msg = reply_msg + INGP_ID_MSG.encode("utf-8")
  try:
    repliedid = message.reply_to_message.from_user.id
    reply_msg = reply_msg + REPLIED_ID_MSG.encode("utf-8")
    bot.reply_to(message, reply_msg.format(username, userid, gpid, repliedid), parse_mode="Markdown")
    return
  except:
    adaadaadadadadadadada = "00"
    bot.reply_to(message, reply_msg.format(username, userid, gpid), parse_mode="Markdown")

@bot.message_handler(commands=['sendcontact'])
def send_test(message):
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  userid = message.from_user.id
  bot.send_message(message.chat.id, SHARE_CONTACT_MSG.encode("utf-8"))
  contacter_list.append(userid)
  

@bot.message_handler(commands=['echo'])
def echo_message(message):
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if SAFE_ECHO:
    if message.chat.type == "supergroup":
      bot.reply_to(message, NO_ECHO_IN_SUPERGP_MSG.encode("utf-8"))
      return
  if len(message.text.split()) < 2:
    bot.reply_to(message, ECHO_REPLY_MSG.encode("utf-8"), parse_mode="Markdown")
    return
  try:
    echo_msg = message.text.replace("/echo","",1)
    bot.reply_to(message, echo_msg)
  except:
    bot.send_message(messsage.chat.id, ERROR_MSG.encode("utf-8"))
  
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
