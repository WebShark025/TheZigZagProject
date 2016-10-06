@bot.message_handler(commands=['bc'])
def bc_msg(message):
  if message.from_user.id in ADMINS_IDS:
    if len(message.text.split()) < 2:
      bot.reply_to(message, "What should I broadcast?")
      return
    bcmsg = message.text.replace("/bc ","")
    allmembers = list(redisserver.smembers('zigzag_members'))
    for userid in allmembers:
      rc = 0
      try:
        bot.send_message(userid, bcmsg, parse_mode="HTML")
        rc = rc + 1
        blocklist = redisserver.sismember('zigzag_blocked', '{}'.format(userid))
        if blocklist:
          redisserver.srem('zigzag_blocked', userid)
      except:
        redisserver.sadd('zigzag_blocked',userid)
    bot.reply_to(message, "Successfully broadcasted to " + str(rc) + " users!")
  else:
    bot.send_message(message.chat.id, "You dont have permission.")

