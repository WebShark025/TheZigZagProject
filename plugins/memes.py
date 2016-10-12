@bot.message_handler(commands=['meme', 'Meme'])
def meme_image(message):
  userlang = redisserver.get("settings:user:language:" + str(message.from_user.id))
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if len(message.text.split("||")) < 3:
    bot.reply_to(message, language[userlang]["MEME_NEA_MSG"], parse_mode="Markdown")
    return
  args = message.text.replace("/meme ","").replace(" ", "%20").split("||")
#  bot.reply_to(message, "Processing..")
  urllib.urlretrieve("http://apimeme.com/meme?meme={}&top={}&bottom={}".format(args[0], args[1], args[2]), 'meme.jpg')
#  print("http://apimeme.com/meme?meme={}&top={}&bottom={}".format(args[0], args[1], args[2]))
  bot.send_chat_action(message.chat.id, "upload_photo")
  tm.sleep(2)
  bot.send_photo(message.chat.id, open('meme.jpg'), caption=" By the @TheZigZagBot")
