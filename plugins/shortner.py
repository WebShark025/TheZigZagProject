@bot.message_handler(commands=['short'])
def shortit(m):
  userid = m.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if len(m.text.split()) < 2:
    bot.reply_to(m, "Please enter a link so I can short it.")
    return
  text = m.text.replace("/short ","", 1)
  res = urllib.urlopen("http://r1z.ir/api.php?long={}".format(text).replace("+","%2B")).read()
  bot.send_message(m.chat.id, "Shorten link: `{}`".format(res), parse_mode="Markdown", disable_web_page_preview=True)
