# -*- coding: utf-8 -*-

@bot.message_handler(commands=['short', 'Short'])
def shortit(m):
  userid = m.from_user.id
  userlang = redisserver.get("settings:user:language:" + str(m.from_user.id))
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if len(m.text.replace("🔗 Link shortner", "", 1).split()) < 2:
    bot.reply_to(m, language[userlang]["SHORTNER_NEA_MSG"], parse_mode="Markdown")
    return
  text = m.text.replace("/short ","", 1).replace("🔗 Link shortner", "", 1)
  res = urllib.urlopen("http://r1z.ir/api.php?long={}".format(text).replace("+","%2B")).read()
  bot.send_message(m.chat.id, "Shorten link: `{}`".format(res), parse_mode="Markdown", disable_web_page_preview=True)
