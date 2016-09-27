@bot.message_handler(func=lambda message: True, content_types=['new_chat_member'])
def user_greet(message):
  if GP_GREETING:
    if message.new_chat_member.id != bot.get_me().id:
      name = message.new_chat_member.first_name
      title = message.chat.title
      bot.send_message(message.chat.id, GP_GREETING_MSG.format(name,title).encode("utf-8"), parse_mode='Markdown')
  
  if message.new_chat_member.id == bot.get_me().id:
    inviter = message.from_user.id
    if inviter not in ADMINS_IDS:
      bot.send_message(message.chat.id, NON_ADMIN_ADDED_BOT_MSG.encode("utf-8"))
      bot.leave_chat(message.chat.id)
    else:
      bot.send_message(message.chat.id, BOT_JOINED_MSG)
#      groupargs = 0
#      redisserver.sadd(message.chat.id, groupargs)
#      redisserver.sadd("zigzag_groups", message.chat.id)
  
@bot.message_handler(func=lambda message: True, content_types=['left_chat_member'])
def user_greet(message):
  if GP_FAREWELL:
    name = message.left_chat_member.first_name
    title = message.chat.title
    bot.send_message(message.chat.id, GP_FAREWELL_MSG.format(name,title).encode("utf-8"), parse_mode='Markdown')
  
@bot.message_handler(func=lambda m: True, content_types=['contact'])
def contact_forwarder(contact):
  userid = contact.from_user.id
  if userid in contacter_list:
    bot.send_message("-" + str(SUPPORT_GP), CONTACT_RECIEVED_MSG.encode("utf-8"))
    bot.forward_message("-" + str(SUPPORT_GP), contact.chat.id, contact.message_id)
    bot.reply_to(contact, CONTACT_FORWARDED_MSG.encode("utf-8"))
