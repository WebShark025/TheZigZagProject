@bot.message_handler(commands=['meme'])
def meme_image(message):
  if len(message.text.split("||")) < 3:
    bot.reply_to(message, MEME_NEA_MSG, parse_mode="Markdown")
    return
  args = message.text.replace("/meme ","").replace(" ", "%20").split("||")
  bot.reply_to(message, "Processing..")
  urllib.urlretrieve("http://apimeme.com/meme?meme={}&top={}&bottom={}".format(args[0], args[1], args[2]), 'meme.jpg')
#  print("http://apimeme.com/meme?meme={}&top={}&bottom={}".format(args[0], args[1], args[2]))
  bot.send_photo(message.chat.id, open('meme.jpg'), caption=" By the @TheZigZagBot")
