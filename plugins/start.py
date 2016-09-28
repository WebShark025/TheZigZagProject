
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    bot.reply_to(message, "You are banned!")
    return
  markup = types.InlineKeyboardMarkup()
  markupib = types.InlineKeyboardButton("Help",callback_data='help')
  markupic = types.InlineKeyboardButton("Channel", url=CHANNEL_LINK)
  markup.add(markupib,markupic)
  markupid = types.InlineKeyboardButton("Show all cmds", callback_data='showit')
  markup.add(markupid)
  
  if message.chat.type == "private":
    bot.reply_to(message, START_MSG.encode("utf-8"), reply_markup=markup, parse_mode="Markdown")
    redisserver.sadd('zigzag_members',message.from_user.id)
  else:
    bot.reply_to(message, START_MSG.encode("utf-8"), parse_mode="Markdown")
