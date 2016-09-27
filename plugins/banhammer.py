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

