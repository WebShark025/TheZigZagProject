@bot.message_handler(commands=['echo'])
def echo_message(message):
  userlang = redisserver.get("settings:user:language:" + str(message.from_user.id))
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if SAFE_ECHO:
    if message.chat.type == "supergroup":
      bot.reply_to(message, language[userlang]["NO_ECHO_IN_SUPERGP_MSG"])
      return
  if len(message.text.split()) < 2:
    bot.reply_to(message, language[userlang]["ECHO_REPLY_MSG"], parse_mode="Markdown")
    return
  try:
    echo_msg = message.text.replace("/echo","",1)
    bot.reply_to(message, echo_msg, parse_mode="HTML")
  except:
    bot.send_message(message.chat.id, language[userlang]["ERROR_MSG"])

