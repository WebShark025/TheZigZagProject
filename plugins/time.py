@bot.message_handler(commands=['date', 'time'])
def time_message(message):
  time = str(datetime.datetime.now())
  bot.send_message(message.chat.id, TIME_MSG.format(time), parse_mode="HTML")
