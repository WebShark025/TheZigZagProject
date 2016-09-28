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
    bot.send_message("-" + str(SUPPORT_GP), "User " + str(message.from_user.id) + " - " + str(message.from_user.first_name) + str(message.from_user.first_name) + " joined the support chat!") 
  else:
    bot.reply_to(message, ALREADY_IN_MESSENGER_MSG, parse_mode="HTML")
@bot.message_handler(commands=['leave'])
def leave_support(message):
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if message.from_user.id in in_chat_with_support:
    bot.reply_to(message, LEFT_MESSENGER_MSG, parse_mode="HTML")
    in_chat_with_support.remove(message.from_user.id)
    bot.send_message("-" + str(SUPPORT_GP), "User " + str(message.from_user.id) + " - " + str(message.from_user.first_name) + str(message.from_user.first_name) + " left the support chat.") 
  else:
    bot.reply_to(message, NOT_IN_MESSENGER_MSG, parse_mode="HTML")
@bot.message_handler(commands=['force_user_leave'])
def forceleave(message):
  if message.from_user.id in ADMINS_IDS:
    if len(message.text.split()) < 2:
      bot.reply_to(message, "Dude, enter an ID.", parse_mode="Markdown")
      return
    userid = message.text.split()[1]
    if message.from_user.id in in_chat_with_support:
      bot.reply_to(message, "Kicked user from chat.", parse_mode="HTML")
      bot.send_message(userid, "You have forced to leave chat by admin.")
      in_chat_with_support.remove(userid)
    else:
      bot.reply_to(message, "User not in chat.")
  else:
    bot.send_message(message.chat.id, "You dont have permission.")
# MESSAGE HANDLING SYSTEM IN MESSAGE_HANDLER PLUGIN
