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
