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

