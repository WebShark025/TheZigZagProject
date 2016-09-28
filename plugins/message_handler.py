def message_replier(messages):
  for message in messages:
    userid = message.from_user.id
    banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
    if banlist:
      return
    if userid in messanger_list:
      bot.reply_to(message, MESSANGER_LEAVE_MSG, parse_mode="Markdown")
      messanger_list.remove(userid)
      bot.send_message("-" + str(SUPPORT_GP), "New feedback!:")
      bot.forward_message("-" + str(SUPPORT_GP), message.chat.id, message.message_id)
      return
    if REPLIER:
      if message.text in reply_message_list:
        bot.reply_to(message, reply_message_list.get(message.text), parse_mode="Markdown")
    if message.text == "Send feedback":
      bot.reply_to(message, MESSANGER_JOIN_MSG, parse_mode="Markdown")
      messanger_list.append(userid)
      return
    if userid in in_chat_with_support:
      bot.forward_message("-" + str(SUPPORT_GP), message.chat.id, message.message_id)
      return
    if message.from_user.id in ADMINS_IDS:
      if message.chat.id == -SUPPORT_GP:
        try:
          bot.forward_message(message.reply_to_message.forward_from.id, message.chat.id, message.message_id)
          bot.reply_to(message, "REPLY SENT")
        except:
          bot.reply_to(message, "ERROR SENDING?")
