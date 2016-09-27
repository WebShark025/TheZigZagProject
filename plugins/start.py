
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
