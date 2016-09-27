@bot.message_handler(commands=['sendcontact'])
def send_test(message):
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  userid = message.from_user.id
  bot.send_message(message.chat.id, SHARE_CONTACT_MSG.encode("utf-8"))
  contacter_list.append(userid)
