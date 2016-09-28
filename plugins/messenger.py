in_chat_with_support = []
@bot.message_handler(commands=['support'])
def support(message):
  if message.from_user.id not in in_chat_with_support:
    bot.reply_to(message, JOINED_MESSENGER_MSG, parse_mode="HTML")
    in_chat_with_support.append(message.from_user.id)
  else:
    bot.reply_to(message, ALREADY_IN_MESSENGER_MSG, parse_mode="HTML")
@bot.message_handler(commands=['leave'])
def support(message):
  if message.from_user.id in in_chat_with_support:
    bot.reply_to(message, LEFT_MESSENGER_MSG, parse_mode="HTML")
    in_chat_with_support.remove(message.from_user.id)
  else:
    bot.reply_to(message, NOT_IN_MESSENGER_MSG, parse_mode="HTML")
# MESSAGE HANDLING SYSTEM IN MESSAGE_HANDLER PLUGIN
