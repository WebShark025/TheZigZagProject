@bot.message_handler(commands=['feedback', 'sendfeedback'])
def send_feedbackz(message):
  userlang = redisserver.get("settings:user:language:" + str(message.from_user.id))
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if userid not in messanger_list:
    bot.reply_to(message, language[userlang]["MESSANGER_JOIN_MSG"], parse_mode="Markdown")
    messanger_list.append(userid)
    return
