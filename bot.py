import datetime
import os
import telebot
import logging
import sys
import urllib
from shutil import copyfile
from telebot import types


### CONFIG AND LOCALE CHECK
if not os.path.exists("config.py"):
  copyfile("config.py.new", "config.py")
if not os.path.exists("locale.py"):
  copyfile("locale.py.new", "locale.py")


reload(sys)  
sys.setdefaultencoding("utf-8")

execfile("locale.py")
execfile("config.py")


logfile = open("bot.log", "a")
time = datetime.datetime.now()
logfile.write("Bot Started: " + str(time) + " with ")
print("Bot started: " + str(time))
messanger_list = []
contacter_list = []


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
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
  else:
    bot.reply_to(message, START_MSG.encode("utf-8"), parse_mode="Markdown")

@bot.message_handler(commands=['test', 'toast'])
def send_test(message):
  bot.send_message(message.chat.id, TEST_MSG.encode("utf-8"))
  
@bot.message_handler(commands=['feedback', 'sendfeedback'])
def send_feedbackz(message):
  userid = message.from_user.id
  if userid not in messanger_list:
    bot.reply_to(message, MESSANGER_JOIN_MSG, parse_mode="Markdown")
    messanger_list.append(userid)
    return

@bot.message_handler(commands=['webshot'])
def webshot_send(message):
  text = message.text.replace("/webshot ","")
  urllib.urlretrieve("http://api.screenshotmachine.com/?key=b645b8&size=X&url={}".format(text), 'webshot.jpg')
  bot.send_photo(message.chat.id, open('webshot.jpg'), caption=" " + WEBSHOT_CAPTION_MSG)

@bot.message_handler(commands=['calc'])
def clac(m):
  text = m.text.replace("/calc ","")
  res = urllib.urlopen("http://api.mathjs.org/v1/?expr={}".format(text)).read()
  bot.send_message(m.chat.id, "_{}_ = `{}`".format(text,res), parse_mode="Markdown", disable_web_page_preview=True)

@bot.message_handler(commands=['id'])
def send_id(message):
  username = message.from_user.first_name.encode("utf-8")
  userid = message.from_user.id
  reply_msg = ID_MSG.encode("utf-8")
  gpid = message.chat.id
  if message.chat.type == "supergroup":
    reply_msg = reply_msg + INGP_ID_MSG.encode("utf-8")
  elif message.chat.type == "group":
    reply_msg = reply_msg + INGP_ID_MSG.encode("utf-8")
  bot.reply_to(message, reply_msg.format(username, userid, gpid), parse_mode="Markdown")

@bot.message_handler(commands=['sendcontact'])
def send_test(message):
  userid = message.from_user.id
  bot.send_message(message.chat.id, SHARE_CONTACT_MSG.encode("utf-8"))
  contacter_list.append(userid)
  

@bot.message_handler(commands=['echo'])
def echo_message(message):
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
