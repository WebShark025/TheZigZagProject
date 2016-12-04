@bot.message_handler(commands=['tocontact'])
def n_to_contact(message):
  userlang = redisserver.get("settings:user:language:" + str(message.from_user.id))
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if len(message.text.split("||")) < 2:
    bot.reply_to(message, "Not enough arguments! Please enter like this: \n`/tocontact +989121234567||WebShark25`", parse_mode="Markdown")
    return
  rlnumber = re.compile(r'^\+(?:\+?)?[0-9]\d{9,13}')
  args = message.text.replace("/tocontact ","").split("||")
  if rlnumber.search(args[0].replace(" ","")):
    bot.send_contact(message.chat.id, args[0].replace(" ",""), args[1])
  else:
    bot.reply_to(message, "Error sending. Phone number recieved in wrong format")
