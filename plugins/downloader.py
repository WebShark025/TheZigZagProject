# -*- coding: utf-8 -*-

inl = []

@bot.message_handler(commands=['Download', 'download'])
def dler(m):
  userid = m.from_user.id
  banlist = redisserver.sismember('banlist', '{}'.format(userid))
  if banlist:
    return
  if len(m.text.split()) < 2:
    bot.reply_to(m, DOWNLOADER_NEA_MSG, parse_mode="Markdown")
    return
  if userid in inl:
    bot.send_message(m.chat.id, DOWNLOADER_WAIT_MSG, parse_mode="Markdown")
    return
  inl.append(userid)
  _hash = "anti_flood:user:" + str(userid)
  max_time = 10
  msgs = 0
  if redisserver.get(_hash):
    msgs = int(redisserver.get(_hash))
    max_msgs = 4 # msgs in
    max_time = 60 # seconds
    if msgs > max_msgs:
      bot.send_message(m.chat.id, "You have exceeded the limit of 3 files per minute. \n\nPlease wait until the limit lifts up.")
#      bot.send_message(SUDO_ID, "یوزر " + str(m.from_user.id) + " بدلیل کرم کون داشتن بن شد.")
#      redisserver.sadd('banlist', int(userid))
      inl.remove(userid)
      return
  redisserver.setex(_hash, max_time, int(msgs)+1)
  try:
#  if True:
    text = m.text.replace("/download ","").replace("/Download ", "")
    filename = os.path.basename(text)
    bot.send_message(m.chat.id, DOWNLOADER_DL_MSG, parse_mode="Markdown")
    fl = urllib.urlopen(text)
    meta = fl.info()
    try:
      size = meta.getheaders("Content-Length")[0]
      if int(size) > 30000000:
#        print(size)
        bot.send_message(m.chat.id, DOWNLOADER_OVERSIZE_MSG, parse_mode="Markdown")
        inl.remove(userid)
        return
    except:
      pass
    urllib.urlretrieve(text, filename)
    bot.send_message(m.chat.id, DOWNLOADER_UP_MSG, parse_mode="Markdown")
    bot.send_chat_action(m.chat.id, "upload_document")
    try:
      bot.send_document(m.chat.id, open(filename))
    except:
      bot.send_message(m.chat.id, DOWNLOADER_OVERSIZE_MSG, parse_mode="Markdown")
    os.remove(filename)
  except:
    bot.send_message(m.chat.id, DOWNLOADER_ERROR_MSG, parse_mode="Markdown")
  inl.remove(userid)
