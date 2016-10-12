# -*- coding: utf-8 -*-

@bot.message_handler(commands=['qrcode', 'Qrcode'])
def qr_image(message):
  userlang = redisserver.get("settings:user:language:" + str(message.from_user.id))
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if len(message.text.replace("◻️ QR Code", "", 1).split()) < 2:
    bot.reply_to(message, language[userlang]["QRCODE_NEA_MSG"], parse_mode="Markdown")
    return
  argus = message.text.replace("/qrcode ","").replace(" ", "%20")
  bot.reply_to(message, "Processing..")
  urllib.urlretrieve("http://api.qrserver.com/v1/create-qr-code/?data={}&size=600x600".format(argus), 'qrcode.png')
#  print("http://apimeme.com/meme?meme={}&top={}&bottom={}".format(args[0], args[1], args[2]))
  bot.send_photo(message.chat.id, open('qrcode.png'), caption=" QR Code by @TheZigZagBot")
