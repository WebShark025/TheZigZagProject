@bot.message_handler(commands=['lmgtfy', 'Lmgtfy'])
def lmgtfy_message(message):
  userlang = redisserver.get("settings:user:language:" + str(message.from_user.id))
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if len(message.text.split()) < 2:
    bot.reply_to(message, language[userlang]["LMGTFY_NEA_MSG"], parse_mode="Markdown")
    return
  textl = message.text.replace("/lmgtfy ","", 1).replace("/Lmgtfy ", "", 1).replace("+","%2B")
  rez = urllib.urlopen("http://r1z.ir/api.php?long=http://lmgtfy.com/?q={}".format(textl)).read()
  bot.send_message(message.chat.id, "Direct link: `{}`\n\nOr click on [this :D]({})".format(rez,rez), parse_mode="Markdown", disable_web_page_preview=True)
