in_chat_with_support = []
@bot.message_handler(commands=['support'])
def support(message):
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if message.from_user.id not in in_chat_with_support:
    bot.reply_to(message, JOINED_MESSENGER_MSG, parse_mode="HTML")
    in_chat_with_support.append(message.from_user.id)
    bot.send_messagae("-" + str(SUPPORT_GP), "User " + str(message.from_user.id) + " - " + str(message.from_user.first_name) + str(message.from_user.first_name) + " joined the support chat!") 
  else:
    bot.reply_to(message, ALREADY_IN_MESSENGER_MSG, parse_mode="HTML")
@bot.message_handler(commands=['leave'])
def support(message):
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if message.from_user.id in in_chat_with_support:
    bot.reply_to(message, LEFT_MESSENGER_MSG, parse_mode="HTML")
    in_chat_with_support.remove(message.from_user.id)
    bot.send_messagae("-" + str(SUPPORT_GP), "User " + str(message.from_user.id) + " - " + str(message.from_user.first_name) + str(message.from_user.first_name) + " left the support chat.") 
  else:
    bot.reply_to(message, NOT_IN_MESSENGER_MSG, parse_mode="HTML")
# MESSAGE HANDLING SYSTEM IN MESSAGE_HANDLER PLUGIN
