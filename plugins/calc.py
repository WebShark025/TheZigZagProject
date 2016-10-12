# -*- coding: utf-8 -*-

@bot.message_handler(commands=['calc', 'Calc'])
def clac(m):
  userid = m.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if len(m.text.replace("✒️ Calculate", "", 1).split()) < 2:
    bot.reply_to(m, CALC_NEA_MSG, parse_mode="Markdown")
    return
  text = m.text.replace("/calc ","")
  res = urllib.urlopen("http://api.mathjs.org/v1/?expr={}".format(text).replace("+","%2B")).read()
  bot.send_message(m.chat.id, "_{}_ = `{}`".format(text,res), parse_mode="Markdown", disable_web_page_preview=True)
