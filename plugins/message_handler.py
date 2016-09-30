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
    if message.chat.type == "private":
      if message.text == "Send feedback":
        send_feedbackz(message)
      if message.text == "Time":
        time_message(message)
      if message.text == "Link shortner":
        shortit(message)
      if message.text == "Send contact":
        send_contactt(message)
      if message.text == "Memes":
        meme_image(message)
      if message.text == "Id":
        send_id(message)
      if message.text == "Calculate":
        clac(message):
    if userid in in_chat_with_support:
      _hash = "anti_flood:user:" + str(userid)
      max_time = 10
      msgs = 0
      if redisserver.get(_hash):
        msgs = int(redisserver.get(_hash))
        max_msgs = 5 # msgs in
        max_time = 10 # seconds
        if msgs > max_msgs:
          in_chat_with_support.remove(userid)
          bot.send_message("-" + str(SUPPORT_GP), "User " + str(userid) + " Auto-kicked for spam.")
          bot.reply_to(message, KICKED_MESSENGER_MSG)
          return
      redisserver.setex(_hash, max_time, int(msgs)+1)
      if message.text == "/leave":
        return
      bot.forward_message("-" + str(SUPPORT_GP), message.chat.id, message.message_id)
      bot.reply_to(message, MESSAGE_SENT_MESSENGER_MSG)
      return
    if message.from_user.id in ADMINS_IDS:
      if message.chat.id == -SUPPORT_GP:
        try:
          bot.forward_message(message.reply_to_message.forward_from.id, message.chat.id, message.message_id)
          bot.reply_to(message, "REPLY SENT")
        except:
          bot.reply_to(message, "ERROR SENDING?")
