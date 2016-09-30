@bot.message_handler(commands=['date', 'time'])
def time_message(message):
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  time = str(datetime.datetime.now())
  bot.send_message(message.chat.id, TIME_MSG.format(time), parse_mode="HTML")
