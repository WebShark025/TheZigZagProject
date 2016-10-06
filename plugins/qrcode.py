@bot.message_handler(commands=['qrcode'])
def meme_image(message):
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if len(message.text.split("||")) < 3:
    bot.reply_to(message, "Please, enter a text so I can convert it to QR code. \n\nFor example: `/qrcode http://sadeco.ir`, parse_mode="Markdown")
    return
  args = message.text.replace("/qrcode ","").replace(" ", "%20")
  bot.reply_to(message, "Processing..")
  urllib.urlretrieve("http://api.qrserver.com/v1/create-qr-code/?data={}&size=600x600".format(args), 'qrcode.png')
#  print("http://apimeme.com/meme?meme={}&top={}&bottom={}".format(args[0], args[1], args[2]))
  bot.send_photo(message.chat.id, open('qrcode.png'), caption=" QR Code by @TheZigZagBot")
