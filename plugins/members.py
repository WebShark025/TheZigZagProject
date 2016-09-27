@bot.message_handler(commands=['members'])
def send_members(message):
  if message.from_user.id in ADMINS_IDS:
    bot.send_message(message.chat.id, "All members: " + str(redisserver.scard('zigzag_members')) + " \nBanned members: " + str(redisserver.scard('zigzag_banlist')), parse_mode="Markdown")
#    allmembers = list(redisserver.smembers('zigzag_members'))
#    bot.send_message(message.chat.id, "First member: " + str(allmembers[0]), parse_mode="Markdown")
  else:
    bot.send_message(message.chat.id, "You dont have permission.")
