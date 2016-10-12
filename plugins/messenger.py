in_chat_with_support = []
waiting_support_approval = []

@bot.message_handler(commands=['support'])
def support(message):
  userlang = redisserver.get("settings:user:language:" + str(message.from_user.id))
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if message.from_user.id not in in_chat_with_support:
    if userid not in waiting_support_approval:
      bot.reply_to(message, language[userlang]["WAITING_APPROVAL_MESSENGER_MSG"], parse_mode="HTML")
      waiting_support_approval.append(message.from_user.id)
      bot.send_message("-" + str(SUPPORT_GP), "User " + str(message.from_user.id) + " - " + str(message.from_user.first_name) + str(message.from_user.first_name) + " is waiting for your approval to join the support chat!") 
    else:
      bot.reply_to(message, "Please wait. Your chat request hasnt been still manually accepted! \nIf you want to leave, type /leave")
      return
  else:
    bot.reply_to(message, language[userlang]["ALREADY_IN_MESSENGER_MSG"], parse_mode="HTML")
@bot.message_handler(commands=['leave'])
def leave_support(message):
  userlang = redisserver.get("settings:user:language:" + str(message.from_user.id))
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if message.from_user.id in in_chat_with_support:
    bot.reply_to(message, language[userlang]["LEFT_MESSENGER_MSG"], parse_mode="HTML")
    in_chat_with_support.remove(message.from_user.id)
    bot.send_message("-" + str(SUPPORT_GP), "User " + str(message.from_user.id) + " - " + str(message.from_user.first_name) + str(message.from_user.first_name) + " left the support chat.") 
  elif userid in waiting_support_approval:
    waiting_support_approval.remove(userid)
    bot.reply_to(message, language[userlang]["LEFT_MESSENGER_MSG"], parse_mode="HTML")
    bot.send_message("-" + str(SUPPORT_GP), "User " + str(message.from_user.id) + " - " + str(message.from_user.first_name) + str(message.from_user.first_name) + " left the support chat while waiting for approval")
  else:
    bot.reply_to(message, language[userlang]["NOT_IN_MESSENGER_MSG"], parse_mode="HTML")
@bot.message_handler(commands=['force_user_leave'])
def forceleave(message):
  if message.from_user.id in ADMINS_IDS:
    if len(message.text.split()) < 2:
      bot.reply_to(message, "Dude, enter an ID.", parse_mode="Markdown")
      return
    userid = int(message.text.split()[1])
    if userid in in_chat_with_support:
      bot.reply_to(message, "Kicked user from chat.", parse_mode="HTML")
      bot.send_message(userid, "You have forced to leave chat by admin.")
      in_chat_with_support.remove(userid)
    else:
      bot.reply_to(message, "User not in chat.")
  else:
    bot.send_message(message.chat.id, "You dont have permission.")
@bot.message_handler(commands=['accept_chat'])
def acceptchat(message):
  if message.from_user.id in ADMINS_IDS:
    if len(message.text.split()) < 2:
      bot.reply_to(message, "Dude, enter an ID.", parse_mode="Markdown")
      return
    userid = int(message.text.split()[1])
    userlang = redisserver.get("settings:user:language:" + str(userid))
    if userid in waiting_support_approval:
      bot.reply_to(message, "Accepted chat request", parse_mode="HTML")
      bot.send_message(userid, language[userlang]["ACCEPTED_MESSENGER_MSG"])
      waiting_support_approval.remove(userid)
      in_chat_with_support.append(userid)
    else:
      bot.reply_to(message, "User not in approval list")
  else:
    bot.send_message(message.chat.id, "You dont have permission.")
@bot.message_handler(commands=['deny_chat'])
def acceptchat(message):
  if message.from_user.id in ADMINS_IDS:
    if len(message.text.split()) < 2:
      bot.reply_to(message, "Dude, enter an ID.", parse_mode="Markdown")
      return
    userid = int(message.text.split()[1])
    userlang = redisserver.get("settings:user:language:" + str(userid))
    if userid in waiting_support_approval:
      bot.reply_to(message, "Denied chat request", parse_mode="HTML")
      bot.send_message(userid, language[userlang]["DENIED_MESSENGER_MSG"])
      waiting_support_approval.remove(userid)
    else:
      bot.reply_to(message, "User not in approval list")
  else:
    bot.send_message(message.chat.id, "You dont have permission.")
# MESSAGE HANDLING SYSTEM IN MESSAGE_HANDLER PLUGIN
