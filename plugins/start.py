# -*- coding: utf-8 -*-

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    bot.reply_to(message, "You are banned!")
    return
  if len(message.text.split()) > 1:
    if message.text.replace("/start ","",1) == "inlinem":
      bot.send_message(message.chat.id, "*Inline mode help!:* \n \nTo use inline mode, first mention the bots ID (@TheZigZagBot) in your message, then use one of theese syntaxes: \n \n💢echo <message> (_Echoes the message using HTML markup_) \n💢cal <ex> (_Calculator.. Easy as a pie_) \n💢hideit <message> (_Hides the message you enter! :D So its un-forwardable._) \n \nMore options comming *soon*!", parse_mode="Markdown")
      return
  markup = types.InlineKeyboardMarkup()
  markupib = types.InlineKeyboardButton("Help",callback_data='help')
  markupic = types.InlineKeyboardButton("Channel", url=CHANNEL_LINK)
  markup.add(markupib,markupic)
  markupid = types.InlineKeyboardButton("Show all cmds", callback_data='showit')
  markup.add(markupid)
  markupie = types.InlineKeyboardButton("Inline mode help", callback_data='inlinehelp')
  markup.add(markupie)
  
  if message.chat.type == "private":
    bot.reply_to(message, START_MSG.encode("utf-8"), reply_markup=markup, parse_mode="Markdown")
    redisserver.sadd('zigzag_members',message.from_user.id)
  else:
    bot.reply_to(message, START_MSG.encode("utf-8"), parse_mode="Markdown")
