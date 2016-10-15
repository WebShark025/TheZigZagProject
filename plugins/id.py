@bot.message_handler(commands=['id', 'Id'])
def send_id(message):
  userlang = redisserver.get("settings:user:language:" + str(message.from_user.id))
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  username = message.from_user.first_name.encode("utf-8")
  userid = message.from_user.id
  reply_msg = language[userlang]["ID_MSG"]
  gpid = message.chat.id
  if message.chat.type == "supergroup":
    reply_msg = reply_msg + language[userlang]["INGP_ID_MSG"]
  elif message.chat.type == "group":
    reply_msg = reply_msg + language[userlang]["INGP_ID_MSG"]
  if message.forward_from:
    reply_msg = reply_msg + language[userlang]["FORWARDED_ID_MSG"].format(message.forward_from.id)
  if message.reply_to_message && message.reply_to_message.forward_from:
    reply_msg = reply_msg + language[userlang]["FORWARDED_ID_MSG"].format(message.reply_to_message.forward_from.id)
  try:
    repliedid = message.reply_to_message.from_user.id
    reply_msg = reply_msg + language[userlang]["REPLIED_ID_MSG"]
    bot.reply_to(message, reply_msg.format(username, userid, gpid, repliedid), parse_mode="Markdown")
    return
  except:
    adaadaadadadadadadada = "00"
    bot.reply_to(message, reply_msg.format(username, userid, gpid), parse_mode="Markdown")
